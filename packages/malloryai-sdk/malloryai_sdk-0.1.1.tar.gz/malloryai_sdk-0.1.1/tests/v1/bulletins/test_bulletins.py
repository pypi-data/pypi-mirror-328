import pytest

pytestmark = pytest.mark.asyncio


async def test_list_bulletins(api_client):
    """Test list_bulletins() API call."""
    response = await api_client.bulletins.list_bulletins(limit=5)

    assert isinstance(response, dict)
    assert "data" in response and isinstance(response["data"], list)
    assert "total" in response and isinstance(response["total"], int)
    assert "offset" in response and isinstance(response["offset"], int)
    assert "limit" in response and isinstance(response["limit"], int)

    if response["data"]:  # If results exist, validate structure of first entry
        first_config = response["data"][0]
        required_fields = [
            "uuid",
            "created_at",
            "updated_at",
            "title",
            "formats",
            "content",
        ]

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"


async def test_get_bulletin(api_client):
    """Test get_bulletin() API call."""
    bulletin = await api_client.bulletins.list_bulletins(limit=1)
    response = await api_client.bulletins.get_bulletin(bulletin["data"][0]["uuid"])

    assert isinstance(response, dict)
    required_fields = [
        "id",
        "uuid",
        "report_type",
        "created_at",
        "updated_at",
        "title",
        "formats",
        "content",
    ]
    for field in required_fields:
        assert field in response, f"Missing expected field: {field}"
