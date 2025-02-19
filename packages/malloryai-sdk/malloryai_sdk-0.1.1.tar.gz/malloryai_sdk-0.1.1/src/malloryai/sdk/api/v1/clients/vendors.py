from typing import List, Dict, Any

from malloryai.sdk.api.v1.decorators.sorting import validate_sorting
from malloryai.sdk.api.v1.http_client import HttpClient


class VendorsClient:
    """Client for managing vendors."""

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    @validate_sorting(sort_pattern="^(name|created_at|updated_at)$")
    async def list_vendors(
        self,
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
        filter: str = "",
    ) -> List[Dict[str, Any]]:
        """
        List vendors.
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :param filter: Filter by field.
        :return: List of vendors.
        """
        params = {
            "offset": offset,
            "limit": limit,
            "sort": sort,
            "order": order,
            "filter": filter,
        }
        return await self.http_client.get("/vendors", params=params)

    async def get_vendor(self, identifier: str) -> Dict[str, Any]:
        """Fetch a vendor by its identifier."""
        return await self.http_client.get(f"/vendors/{identifier}")
