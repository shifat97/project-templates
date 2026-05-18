import requests
from typing import Any, Dict, Optional
from config.settings import settings
from utils.logger import log_response

class BaseClient:
    def __init__(self, base_url: str = settings.FULL_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = settings.TIMEOUT

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            json=json,
            headers=headers,
            timeout=self.timeout,
            **kwargs
        )
        log_response(response)
        return response

    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("DELETE", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("PATCH", endpoint, **kwargs)
