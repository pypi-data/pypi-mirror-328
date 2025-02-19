import pytest

pytestmark = pytest.mark.asyncio


async def test_list_content_chunks(api_client):
    """Test list_content_chunks() API call."""
    response = await api_client.content_chunks.list_content_chunks(limit=5)

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
            "analyzed_at",
            "hash",
            "content_type",
            "reference_uuid",
            "reference_url_hash",
        ]

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"


async def test_get_content_chunk(api_client):
    """Test get_content_chunk() API call."""
    content_chunk = await api_client.content_chunks.list_content_chunks(limit=1)
    response = await api_client.content_chunks.get_content_chunk(
        content_chunk["data"][0]["uuid"]
    )

    assert isinstance(response, dict)
    required_fields = [
        "uuid",
        "created_at",
        "updated_at",
        "analyzed_at",
        "hash",
        "content_type",
        "reference_uuid",
        "extracted_content",
        "analysis_object",
    ]
    for field in required_fields:
        assert field in response, f"Missing expected field: {field}"
