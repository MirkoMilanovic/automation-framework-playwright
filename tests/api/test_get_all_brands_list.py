import logging

import pytest
from playwright.sync_api import APIRequestContext

from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


@pytest.mark.api
def test_get_all_brands_list(api_context: APIRequestContext) -> None:
    """Verify that the brands list endpoint returns a valid brands collection."""
    logger.info("Sending request to /api/brandsList endpoint")

    response = api_context.get("/api/brandsList")

    logger.info(f"Received response with status: {response.status}")

    assert response.status == 200

    response_body = response.json()

    assert response_body["responseCode"] == 200
    assert "brands" in response_body
    assert len(response_body["brands"]) > 0

    logger.info("Brands API test completed successfully")
