from pathlib import Path
from typing import Any, Dict, Literal, Optional

import os
import time
import json
import asyncio
import httpx
from contextlib import asynccontextmanager
from functools import wraps


from eeclient.export.image import image_to_asset, image_to_drive
from eeclient.logger import logger
from eeclient.exceptions import EEClientError, EERestException
from eeclient.tasks import get_task, get_task_by_name, get_tasks
from eeclient.typing import GEEHeaders, SepalHeaders
from eeclient.async_data import (
    create_folder,
    get_asset,
    get_assets_async,
    get_info,
    get_map_id,
)
from eeclient.export.table import table_to_asset, table_to_drive

SEPAL_HOST = os.getenv("SEPAL_HOST")
if not SEPAL_HOST:
    raise ValueError("SEPAL_HOST environment variable not set")
EARTH_ENGINE_API_URL = "https://earthengine.googleapis.com/v1alpha"
SEPAL_API_DOWNLOAD_URL = f"https://{SEPAL_HOST}/api/user-files/download/?path=%2F.config%2Fearthengine%2Fcredentials"
VERIFY_SSL = not (
    SEPAL_HOST == "host.docker.internal" or SEPAL_HOST == "danielg.sepal.io"
)


def parse_cookie_string(cookie_string):
    cookies = {}
    for pair in cookie_string.split(";"):
        key_value = pair.strip().split("=", 1)
        if len(key_value) == 2:
            key, value = key_value
            cookies[key] = value
    return cookies


def should_retry(exception: Exception) -> bool:
    """Check if the exception is due to rate limiting"""
    if isinstance(exception, EERestException):
        return exception.code == 429
    return False


def sync_wrapper(async_func):
    """Decorator to run async functions synchronously when needed"""

    @wraps(async_func)
    def wrapper(*args, **kwargs):
        return asyncio.run(async_func(*args, **kwargs))

    return wrapper


class AsyncEESession:
    def __init__(self, sepal_headers: SepalHeaders):
        """Session that handles two scenarios to set the headers for the Earth Engine API

        It can be initialized with the headers sent by SEPAL or with the credentials and project

        """
        self.expiry_date = 0
        self.retry_count = 0
        self.max_retries = 3

        self.sepal_headers = sepal_headers
        self.sepal_cookies = parse_cookie_string(sepal_headers["cookie"][0])
        self.sepal_user_data = json.loads(sepal_headers["sepal-user"][0])  # type: ignore
        self.sepal_username = self.sepal_user_data["username"]

        if not self.sepal_user_data["googleTokens"]:
            raise EEClientError(
                "Authentication required: Please authenticate via sepal. See https://docs.sepal.io/en/latest/setup/gee.html."
            )

        self.project_id = self.sepal_user_data["googleTokens"]["projectId"]
        if not self.project_id:
            raise EEClientError(
                "No project ID found in the user data. Please authenticate select a project."
            )

        self._async_client = None

        # Initialize credentials from the initial tokens
        self._initialize_credentials()

        # Maybe do a test? and check that the session is valid
        # if not I will get this error:
        # httpx.HTTPStatusError: Client error '401 Unauthorized' for url 'https://danielg.sepal.io/api/user-files/listFiles/?path=%2F&extensions='

    def get_assets_folder(self) -> str:
        return f"projects/{self.project_id}/assets/"

    def _initialize_credentials(self):
        """Initialize credentials from the initial Google tokens"""
        _google_tokens = self.sepal_user_data.get("googleTokens")
        if not _google_tokens:
            raise EEClientError(
                "Authentication required: Please authenticate via sepal."
            )
        self.expiry_date = _google_tokens["accessTokenExpiryDate"]
        self._credentials = {
            "access_token": _google_tokens["accessToken"],
            "access_token_expiry_date": _google_tokens["accessTokenExpiryDate"],
            "project_id": _google_tokens["projectId"],
            "sepal_user": self.sepal_username,
        }

    def is_expired(self) -> bool:
        """Returns if a token is about to expire"""
        return (self.expiry_date / 1000) - time.time() < 60

    def get_current_headers(self) -> GEEHeaders:
        """Get current headers without refreshing credentials"""
        if not self._credentials:
            raise EEClientError("No credentials available")

        access_token = self._credentials["access_token"]
        return {
            "x-goog-user-project": str(self.project_id),
            "Authorization": f"Bearer {access_token}",
            "Username": str(self.sepal_username),
        }

    async def get_headers(self) -> GEEHeaders:
        """Async method to get headers, refreshing credentials if needed"""
        if self.is_expired():
            await self.set_credentials()
        return self.get_current_headers()

    @asynccontextmanager
    async def get_client(self):
        """Context manager for an HTTP client using the current headers.
        A new client is created each time to ensure fresh headers."""

        timeout = httpx.Timeout(connect=60.0, read=300.0, write=60.0, pool=60.0)
        headers = await self.get_headers()
        async_client = httpx.AsyncClient(headers=headers, timeout=timeout)  # type: ignore
        try:
            yield async_client
        finally:
            await async_client.aclose()

    async def set_credentials(self) -> None:
        """
        Refresh credentials asynchronously.
        Uses its own HTTP client (thus bypassing get_headers) to avoid recursion.
        """
        logger.debug(
            "Token is expired or about to expire; attempting to refresh credentials."
        )
        attempt = 0
        credentials_url = SEPAL_API_DOWNLOAD_URL

        # Prepare cookies for authentication.
        sepal_cookies = httpx.Cookies()
        sepal_cookies.set(
            "SEPAL-SESSIONID", self.sepal_cookies.get("SEPAL-SESSIONID", "")
        )

        last_status = None

        while attempt < self.max_retries:
            attempt += 1
            try:
                async with httpx.AsyncClient(
                    cookies=sepal_cookies,
                    verify=VERIFY_SSL,
                ) as client:
                    logger.debug(f"Attempt {attempt} to refresh credentials.")
                    response = await client.get(credentials_url)

                last_status = response.status_code

                if response.status_code == 200:
                    self._credentials = response.json()
                    self.expiry_date = self._credentials["access_token_expiry_date"]
                    self.project_id = self._credentials["project_id"]
                    logger.debug(
                        f"Successfully refreshed credentials !{self._credentials}."
                    )
                    return
                else:
                    logger.debug(
                        f"Attempt {attempt}/{self.max_retries} failed with status code: {response.status_code}."
                    )
            except Exception as e:
                logger.error(
                    f"Attempt {attempt}/{self.max_retries} encountered an exception: {e}"
                )
            await asyncio.sleep(2**attempt)  # Exponential backoff

        raise ValueError(
            f"Failed to retrieve credentials after {self.max_retries} attempts, last status code: {last_status}"
        )

    async def rest_call(
        self,
        method: Literal["GET", "POST"],
        url: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        max_attempts: int = 4,
        initial_wait: float = 1,
        max_wait: float = 60,
    ) -> Dict[str, Any]:
        """Async REST call with retry logic"""

        async def _make_request():
            try:
                async with self.get_client() as client:
                    url_with_project = self.set_url_project(url)
                    logger.debug(f"Making async {method} request to {url_with_project}")
                    response = await client.request(
                        method, url_with_project, json=data, params=params
                    )

                    if response.status_code >= 400:
                        if "application/json" in response.headers.get(
                            "Content-Type", ""
                        ):
                            error_data = response.json().get("error", {})
                            logger.debug(f"Request failed with error: {error_data}")
                            raise EERestException(error_data)
                        else:
                            error_data = {
                                "code": response.status_code,
                                "message": response.reason_phrase,
                            }
                            logger.debug(f"Request failed with error: {error_data}")
                            raise EERestException(error_data)

                    return response.json()

            except EERestException as e:
                return e

        attempt = 0
        while attempt < max_attempts:
            result = await _make_request()
            if isinstance(result, EERestException):
                if result.code in [429, 401]:

                    error = ""
                    attempt += 1
                    wait_time = min(initial_wait * (2**attempt), max_wait)

                    if result.code == 429:
                        error = "Rate limit exceeded"

                    if result.code == 401:
                        # This happens when the credentials change during the session
                        error = "Unauthorized"
                        await self.set_credentials()

                    logger.debug(
                        f"{error}. Attempt {attempt}/{max_attempts}. "
                        f"Waiting {wait_time} seconds..."
                    )
                    await asyncio.sleep(wait_time)
                else:
                    raise result
            else:
                return result

        raise EERestException(
            {
                "code": 429,
                "message": "Max retry attempts reached: "
                + str(result.message),  # type: ignore
            }
        )

    def set_url_project(self, url: str) -> str:
        """Set the API URL with the project id"""

        return url.format(
            earth_engine_api_url=EARTH_ENGINE_API_URL, project=self.project_id
        )

    @property
    def operations(self):
        # Return an object that bundles operations, passing self as the session.
        return _Operations(self)

    @property
    def export(self):
        return _Export(self)

    @property
    def tasks(self):
        return _Tasks(self)


class _Operations:
    def __init__(self, session):
        self._session = session

    async def get_assets_async(self, folder: str):
        return await get_assets_async(
            self._session,
            folder=folder,
        )

    def get_info(self, ee_object=None, workloadTag=None, serialized_object=None):
        return asyncio.run(
            get_info(
                self._session,
                ee_object,
                workloadTag,
                serialized_object,
            )
        )

    def get_map_id(self, ee_image, vis_params={}, bands=None, format=None):
        return asyncio.run(
            get_map_id(self._session, ee_image, vis_params, bands, format)
        )

    def get_asset(self, ee_asset_id):
        return asyncio.run(get_asset(self._session, ee_asset_id))

    def create_folder(self, folder: str):
        return asyncio.run(create_folder(self._session, folder))


class _Export:
    def __init__(self, session):
        self._session = session

    def table_to_drive(self, collection, **kwargs):
        return asyncio.run(table_to_drive(self._session, collection, **kwargs))

    def table_to_asset(self, collection, **kwargs):
        return asyncio.run(table_to_asset(self._session, collection, **kwargs))

    def image_to_drive(self, image, **kwargs):
        return asyncio.run(image_to_drive(self._session, image, **kwargs))

    def image_to_asset(self, image, **kwargs):
        return asyncio.run(image_to_asset(self._session, image, **kwargs))


class _Tasks:
    def __init__(self, session):
        self._session = session

    async def get_tasks(self):
        return await get_tasks(self._session)

    async def get_task(self, task_id):
        return await get_task(self._session, task_id)

    async def get_task_by_name(self, asset_name):
        return await get_task_by_name(self._session, asset_name)
