from typing import List, Dict, Any

from malloryai.sdk.api.v1.decorators.sorting import validate_sorting
from malloryai.sdk.api.v1.http_client import HttpClient


class DetectionSignaturesClient:
    """Client for managing detection signatures."""

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    @validate_sorting
    async def list_detection_signatures(
        self,
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
    ) -> List[Dict[str, Any]]:
        """
        List detection signatures.
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :return: List of detection signatures.
        """
        params = {"offset": offset, "limit": limit, "sort": sort, "order": order}
        return await self.http_client.get("/detection_signatures", params=params)

    async def get_detection_signature(self, identifier: str) -> Dict[str, Any]:
        """
        Get a detection signature.
        :param identifier: Detection signature identifier.
        :return: Detection signature.
        """
        return await self.http_client.get(f"/detection_signatures/{identifier}")
