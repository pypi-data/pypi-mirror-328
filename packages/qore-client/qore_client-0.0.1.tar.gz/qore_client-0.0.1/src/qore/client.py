from typing import Any, Dict, Optional

import requests
from requests import Response


class QoreClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_data(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        response: Response = requests.get(
            f"https://api.qore.ai/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {self.api_key}"},
        )

        response.raise_for_status()
        return response.json()
