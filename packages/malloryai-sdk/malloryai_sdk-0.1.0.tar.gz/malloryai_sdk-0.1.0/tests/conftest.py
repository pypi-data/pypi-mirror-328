import os
import pytest
import logging
from dotenv import load_dotenv
from malloryai.sdk.api.v1.api import MalloryAPIClient

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("MALLORY_API_KEY", "test_api_key")


@pytest.fixture
def api_client():
    """Fixture to initialize MalloryAPIClient with test API key."""
    logger = logging.getLogger("test_logger")
    return MalloryAPIClient(api_key=API_KEY, logger=logger)
