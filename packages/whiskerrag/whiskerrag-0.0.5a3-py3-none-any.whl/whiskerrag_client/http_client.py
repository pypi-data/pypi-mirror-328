from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

import httpx
from pydantic import BaseModel


class BaseClient(ABC):
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    @abstractmethod
    async def _request(
        self,
        method: str,
        endpoint: str,
        *,
        json: Union[Dict[str, Any], List[Dict[str, Any]], None] = None,
        params: Optional[Union[Dict[str, Any], List[tuple[str, Any]]]] = None,
    ) -> Any:
        pass


class HttpClient(BaseClient):
    def __init__(self, base_url: str, token: str):
        super().__init__(base_url, token)
        self.client = httpx.AsyncClient()

    async def _request(
        self,
        method: str,
        endpoint: str,
        *,
        json: Union[Dict[str, Any], List[Dict[str, Any]], None] = None,
        params: Optional[Union[Dict[str, Any], List[tuple[str, Any]]]] = None,
        **kwargs: Dict[str, Any],
    ) -> Any:
        url = f"{self.base_url}{endpoint}"
        request_kwargs = {
            "method": method,
            "url": url,
            "headers": self.headers,
        }
        if json is not None:
            if isinstance(json, BaseModel):
                request_kwargs["json"] = json.model_dump(exclude_none=True)
            elif isinstance(json, (dict, list)):
                request_kwargs["json"] = json  # type: ignore
            else:
                raise ValueError(f"Unsupported JSON type: {type(json)}")
        for key, value in kwargs.items():
            if key not in request_kwargs:
                request_kwargs[key] = value

        async with self.client as client:
            response = await client.request(
                method=method,
                url=url,
                json=json,
                params=params,
                **kwargs,  # type: ignore
            )
            response.raise_for_status()
            return response.json()

    async def close(self) -> None:
        await self.client.aclose()
