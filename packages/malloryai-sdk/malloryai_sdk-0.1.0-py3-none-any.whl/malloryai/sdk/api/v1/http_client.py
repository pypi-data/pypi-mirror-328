import aiohttp
from typing import Optional, Dict, Any
import logging

from malloryai.sdk.api.v1.exceptions.exception import APIError
from malloryai.sdk.api.v1.exceptions.not_found import NotFoundError
from malloryai.sdk.api.v1.exceptions.validation import ValidationError


class HttpClient:
    """Handles HTTP interactions with the API with enhanced logging."""

    BASE_URL = "https://api.mallory.ai/v1"

    def __init__(self, api_key: str, logger: Optional[logging.Logger] = None):
        """
        Initialize the HTTP client with API key and set up headers.

        :param api_key: Authentication API key for the Mallory API
        """
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self.logger = logger or logging.getLogger(__name__)
        self.logger.info(
            f"HttpClient initialized with API key (last 4 chars: {api_key[-4:]})"
        )

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """
        Perform an HTTP GET request with optional query parameters.

        :param endpoint: API endpoint to call
        :param params: Optional query parameters
        :return: Parsed JSON response
        """
        full_url = f"{self.BASE_URL}{endpoint}"
        self.logger.info(f"GET request to {full_url}")
        self.logger.debug(f"GET request params: {params}")

        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(full_url, params=params) as response:
                    self.logger.info(f"GET response status: {response.status}")
                    return await self._handle_response(response)
        except aiohttp.ClientError as e:
            self.logger.error(f"Network error during GET request: {e}")
            raise

    async def post(
        self,
        endpoint: str,
        json: Dict[str, Any],
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        Perform an HTTP POST request with JSON payload.

        :param endpoint: API endpoint to call
        :param json: JSON payload to send
        :param params: Optional query parameters
        :return: Parsed JSON response
        """
        full_url = f"{self.BASE_URL}{endpoint}"
        self.logger.info(f"POST request to {full_url}")
        self.logger.debug(f"POST request payload: {json}")

        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.post(full_url, json=json, params=params) as response:
                    self.logger.info(f"POST response status: {response.status}")
                    return await self._handle_response(response)
        except aiohttp.ClientError as e:
            self.logger.error(f"Network error during POST request: {e}")
            raise

    async def _handle_response(self, response: aiohttp.ClientResponse) -> Any:
        """
        Handle the API response, logging details and raising APIError if needed.

        :param response: aiohttp ClientResponse object
        :return: Parsed JSON response if successful
        :raises APIError: If the response status is not 200
        """
        try:
            response_text = await response.text()
            self.logger.debug(f"Response body: {response_text}")

            if response.status == 200:
                return await response.json()
            elif response.status == 404:
                self.logger.error(
                    f"Not Found Error - Status: {response.status}, Message: {response_text}"
                )
                raise NotFoundError(response_text)
            elif response.status == 422:
                self.logger.error(
                    f"Validation Error - Status: {response.status}, Message: {response_text}"
                )
                raise ValidationError(response_text)
            else:
                self.logger.error(
                    f"API Error - Status: {response.status}, Message: {response_text}"
                )
                raise APIError(response.status, response_text)
        except Exception as e:
            self.logger.error(f"Error processing response: {e}")
            raise
