import pytest
from playwright.sync_api import APIRequestContext


@pytest.mark.api
def test_get_all_brands_list(api_context: APIRequestContext) -> None:
    """Verify that the brands list endpoint returns a valid brands collection."""
    response = api_context.get("/api/brandsList")

    assert response.status == 200

    response_body = response.json()

    assert response_body["responseCode"] == 200
    assert "brands" in response_body
    assert len(response_body["brands"]) > 0
