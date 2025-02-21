from __future__ import annotations
from typing import Any, Dict
import requests
from outerport.resources.base_resource import BaseResource


class SettingsResource(BaseResource):
    def update(self, user_id: int, settings_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update user settings.
        """
        url = f"{self.client.base_url}/api/v0/settings"
        headers = self.client._json_headers()
        payload = {"user_id": user_id, "settings_data": settings_data}
        resp = requests.put(url, headers=headers, json=payload)
        resp.raise_for_status()
        return resp.json()

    def retrieve(self, user_id: int) -> Dict[str, Any]:
        """
        Get user settings by user_id.
        """
        url = f"{self.client.base_url}/api/v0/settings"
        headers = self.client._json_headers()
        params = {"user_id": user_id}
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        return resp.json()
