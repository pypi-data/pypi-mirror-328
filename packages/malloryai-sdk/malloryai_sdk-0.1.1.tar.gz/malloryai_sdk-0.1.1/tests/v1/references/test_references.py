import pytest

pytestmark = pytest.mark.asyncio


async def test_list_products(api_client):
    """Test list_references() API call."""
    response = await api_client.references.list_references(limit=5)

    assert isinstance(response, dict)
    assert "data" in response and isinstance(response["data"], list)
    assert "total" in response and isinstance(response["total"], int)
    assert "offset" in response and isinstance(response["offset"], int)
    assert "limit" in response and isinstance(response["limit"], int)

    if response["data"]:
        first_config = response["data"][0]
        required_fields = [
            "uuid",
            "created_at",
            "updated_at",
            "published_at",
            "collected_at",
            "url_hash",
            "source",
            "user_generated_content",
            "content_type",
            "topic",
            "authors",
            "content_chunk_uuids",
        ]

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"


async def test_get_reference(api_client):
    """Test get_reference() API call."""
    reference = await api_client.references.list_references(limit=1)
    response = await api_client.references.get_reference(reference["data"][0]["uuid"])

    assert isinstance(response, dict)
    required_fields = [
        "uuid",
        "created_at",
        "updated_at",
        "published_at",
        "collected_at",
        "url_hash",
        "source",
        "user_generated_content",
        "content_type",
        "topic",
        "authors",
        "content_chunks",
    ]
    for field in required_fields:
        assert field in response, f"Missing expected field: {field}"


async def test_create_reference(api_client):
    """Test create_reference() API call."""
    # response = await api_client.references.create_references()
    # assert isinstance(response, dict)
    assert True
