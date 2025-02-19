import pytest

pytestmark = pytest.mark.asyncio


async def test_list_sources(api_client):
    """Test list_sources() API call."""
    response = await api_client.sources.list_sources()

    assert isinstance(response, dict)
    assert "sources" in response and isinstance(response["sources"], list)
    assert "count" in response and isinstance(response["count"], int)

    if response["sources"]:  # If results exist, validate structure of first entry
        first_config = response["sources"][0]
        required_fields = [
            "slug",
        ]

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"
