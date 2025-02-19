from typing import List, Dict, Any

from malloryai.sdk.api.v1.decorators.sorting import validate_sorting
from malloryai.sdk.api.v1.http_client import HttpClient


class ReferencesClient:
    """Client for managing references."""

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    @validate_sorting(
        sort_pattern="^(published_at|collected_at|created_at|updated_at)$"
    )
    async def list_references(
        self,
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
        filter_by: str = "",
    ) -> List[Dict[str, Any]]:
        """
        List references.
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :param filter_by: Filter by field.
        :return: List of references.
        """
        params = {
            "offset": offset,
            "limit": limit,
            "sort": sort,
            "order": order,
            "filter": filter_by,
        }
        return await self.http_client.get("/references", params=params)

    async def get_reference(self, identifier: str) -> Dict[str, Any]:
        """
        Get a reference by identifier.
        :param identifier: Reference identifier.
        :return: Reference.
        """
        return await self.http_client.get(f"/references/{identifier}")

    async def create_references(self, urls: List[str]) -> List[Dict[str, Any]]:
        """
        Create references from URLs.
        :param urls: URLs to create references from.
        :return: References.
        """
        return await self.http_client.post("/references", json={"urls": urls})
