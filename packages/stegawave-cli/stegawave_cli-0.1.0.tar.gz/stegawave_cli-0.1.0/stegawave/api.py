# stegawave/api.py
import requests
from typing import Optional, Dict, Any, List
from datetime import datetime
import json
from .config import config
from .exceptions import StegawaveError, AuthenticationError

class StegawaveAPI:
    def __init__(self):
        self.base_url = config.api_url.rstrip('/')
        
    def _get_headers(self) -> Dict[str, str]:
        if not config.api_key:
            raise AuthenticationError("API key not configured. Run 'stegawave configure' first.")
        return {
            "x-api-key": config.api_key,
            "Content-Type": "application/json"
        }

    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = self._get_headers()
        
        if "headers" in kwargs:
            headers.update(kwargs["headers"])
            del kwargs["headers"]

        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
            return response.json() if response.content else None
        except requests.exceptions.RequestException as e:
            if hasattr(e.response, 'json'):
                try:
                    error_data = e.response.json()
                    raise StegawaveError(error_data.get('error', str(e)))
                except json.JSONDecodeError:
                    pass
            raise StegawaveError(str(e))

    def list_events(self, status: Optional[str] = None) -> List[Dict[str, Any]]:
        params = {"status": status} if status else None
        return self._request("GET", "/events", params=params)

    def create_event(self, name: str, start_time: datetime, end_time: datetime, 
                    ip_whitelist: Optional[List[str]] = None) -> Dict[str, Any]:
        data = {
            "eventName": name,
            "startTime": start_time.isoformat(),
            "endTime": end_time.isoformat(),
            "ipWhitelist": ip_whitelist or []
        }
        return self._request("POST", "/create-event", json=data)

    def get_event(self, event_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/events/{event_id}")

    def update_event(self, event_id: str, **kwargs) -> Dict[str, Any]:
        data = {k: v for k, v in kwargs.items() if v is not None}
        return self._request("POST", f"/update-event", json=data)

    def delete_event(self, event_id: str) -> None:
        self._request("POST", f"/delete-event")

    def reset_event(self, event_id: str) -> None:
        self._request("POST", f"/reset-event")


    # we need to upload the file using the upload metyhods in the backend


    def decode_file(self, event_id: str, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            return self._request("POST", f"", files=files)

    def get_results(self, event_id: str) -> Dict[str, Any]:
        return self._request("POST", f"/get-decoder-results")  # we need to pass the event id in the body

    def list_ad_breaks(self, event_id: str) -> List[Dict[str, Any]]:
        return self._request("GET", f"/getAdBreaks?eventID={event_id}")

    def schedule_ad_break(self, event_id: str, start_time: datetime, duration: int) -> Dict[str, Any]:
        data = {
            "startTime": start_time.isoformat(),
            "duration": duration
        }
        return self._request("POST", f"/scheduleAd", json=data)

api = StegawaveAPI()