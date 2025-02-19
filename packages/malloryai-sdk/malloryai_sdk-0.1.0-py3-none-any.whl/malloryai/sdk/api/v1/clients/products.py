from typing import List, Dict, Any, Optional

from malloryai.sdk.api.v1.decorators.sorting import validate_sorting
from malloryai.sdk.api.v1.http_client import HttpClient


class ProductsClient:
    """Client for managing products."""

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    @validate_sorting(sort_pattern="^(name|created_at|updated_at)$")
    async def list_products(
        self,
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
        filter_by: str = "",
    ) -> List[Dict[str, Any]]:
        """
        List all products.
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :param filter_by: Filter by field.
        :return: List of products.
        """
        params = {
            "offset": offset,
            "limit": limit,
            "sort": sort,
            "order": order,
            "filter": filter_by,
        }
        return await self.http_client.get("/products", params=params)

    async def get_product(self, identifier: str) -> Dict[str, Any]:
        """
        Fetch a product by its identifier.
        :param identifier: The unique UUID of the technology product to retrieve.
        :return: The product.
        """
        return await self.http_client.get(f"/products/{identifier}")

    @validate_sorting(sort_pattern="^(name|created_at|updated_at)$")
    async def search_products(
        self,
        search_type: Optional[str] = "",
        product: Optional[str] = "",
        vendor: Optional[str] = "",
        cpe: Optional[str] = "",
        type: Optional[str] = "",
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
    ) -> List[Dict[str, Any]]:
        """
        Search for products.
        :param search_type:  Options: 'standard' (default), 'did_you_mean'.
        :param product: The product name to search for.
        :param vendor: The vendor name to search for.
        :param cpe: The CPE to search for.
        :param type: The type of the product (e.g., application (default), operating system).
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :return: List of products.
        """
        payload = {
            "vendor": vendor,
            "product": product,
            "cpe": cpe,
            "type": type,
            "search_type": search_type,
        }
        params = {"offset": offset, "limit": limit, "sort": sort, "order": order}
        return await self.http_client.post(
            "/products/search", json=payload, params=params
        )
