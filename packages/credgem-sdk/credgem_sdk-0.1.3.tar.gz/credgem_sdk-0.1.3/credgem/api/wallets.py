from typing import Dict, Any, Optional, List, NamedTuple
from datetime import datetime
from enum import Enum

from .base import BaseAPI
from ..models import WalletResponse, Balance


class PaginatedResponse(NamedTuple):
    data: List[Any]
    page: int
    page_size: int
    total_count: int


class WalletStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class WalletsAPI(BaseAPI):
    async def create(
        self,
        name: str,
        description: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> WalletResponse:
        payload = {
            "name": name,
        }
        if description is not None:
            payload["description"] = description
        if context is not None:
            payload["context"] = context

        response = await self._post("/wallets", json=payload, response_model=None)
        # Ensure description is properly set in the response
        if description is not None and "description" not in response:
            response["description"] = description
        return WalletResponse.from_dict(response)

    async def get(self, wallet_id: str) -> WalletResponse:
        response = await self._get(f"/wallets/{wallet_id}", response_model=None)
        return WalletResponse.from_dict(response)

    async def list(self, page: int = 1, page_size: int = 50) -> PaginatedResponse:
        params = {"page": page, "page_size": page_size}
        response = await self._get("/wallets", params=params, response_model=None)
        return PaginatedResponse(
            data=[
                WalletResponse.from_dict(wallet) for wallet in response.get("data", [])
            ],
            page=response.get("page", page),
            page_size=response.get("page_size", page_size),
            total_count=response.get("total_count", 0),
        )

    async def update(
        self,
        wallet_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> WalletResponse:
        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if context is not None:
            payload["context"] = context

        response = await self._put(
            f"/wallets/{wallet_id}", json=payload, response_model=None
        )
        return WalletResponse.from_dict(response)

    async def delete(self, wallet_id: str) -> None:
        await self._delete(f"/wallets/{wallet_id}", response_model=None)
