import requests
import asyncio

from datetime import datetime

from .utils import encode_base64

INGESTOR_URL = 'https://events.userlens.io'

class EventTracker:
    def __init__(self, write_code, requests_timeout=5):
        if not write_code:
            raise ValueError('Error in userlens-sdk-py: Error in write_code is required')
        
        if requests_timeout <= 0:
            raise ValueError('Error in userlens-sdk-py: requests_timeout must be greater than 0')

        self.write_code = encode_base64(write_code)
        self.requests_timeout = requests_timeout
    
    def _validate_traits(self, traits):
        return isinstance(traits, dict) and bool(traits)

    def identify(self, user_id, traits):
        if not user_id:
            raise ValueError('Error in userlens-sdk-py: user_id is required')
        
        if not self._validate_traits(traits):
            raise ValueError('Error in userlens-sdk-py: traits is required and must be a non-empty dictionary of traits')

        payload = {
            "type": "identify",
            "userId": user_id,
            "traits": traits,
        }
        headers = {
            "Authorization": f"Basic {self.write_code}",
        }

        response = requests.post(
            f"{INGESTOR_URL}/event", 
            json=payload, 
            headers=headers, 
            timeout=self.requests_timeout
        )

        if response.status_code != 200:
            raise ValueError(f'Error in userlens-sdk-py: {response.json()}')

        return "User identified successfully"

    def track(self, user_id, event_name, traits = None):
        if not user_id:
            raise ValueError('Error in userlens-sdk-py: user_id is required')
        
        if not event_name:
            raise ValueError('Error in userlens-sdk-py: event_name is required')

        payload = {
            "type": "track",
            "userId": user_id,
            "event": event_name,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "source": "userlens-sdk-py"
        }
        headers = {
            "Authorization": f"Basic {self.write_code}",
        }

        response = requests.post(
            f"{INGESTOR_URL}/event", 
            json=payload, 
            headers=headers, 
            timeout=self.requests_timeout
        )

        # log response json
        print(f"response from track: {response.json()}")

        if response.status_code != 200:
            raise ValueError(f'Error in userlens-sdk-py: {response.json()}')
        
        if traits:
            self.identify(user_id, traits)
        
        return "Event tracked successfully"
    
    def async_identify(self, user_id, traits):
        """Asynchronous version of identify() using httpx."""
        try:
            loop = asyncio.get_running_loop()
            loop.create_task(self._async_identify(user_id, traits))
        except RuntimeError:
            asyncio.ensure_future(self._async_identify(user_id, traits))

    def async_track(self, user_id, event_name, traits):
        """Asynchronous version of track() using httpx."""
        try:
            loop = asyncio.get_running_loop()
            loop.create_task(self._async_track(user_id, event_name, traits))
        except RuntimeError:
            asyncio.ensure_future(self._async_track(user_id, event_name, traits))

    async def _async_identify(self, user_id, traits):
        try:
            import httpx
        except ImportError:
            raise ImportError(
                "httpx is required for async usage. Install it with:\n"
                "pip install userlens-sdk-py[async]"
            )

        if not user_id:
            raise ValueError('Error in userlens-sdk-py: user_id is required')
        
        if not self._validate_traits(traits):
            raise ValueError('Error in userlens-sdk-py: traits is required and must be a non-empty dictionary of traits')

        payload = {
            "type": "identify",
            "userId": user_id,
            "traits": traits,
        }
        headers = {
            "Authorization": f"Basic {self.write_code}",
        }

        async with httpx.AsyncClient(timeout=self.requests_timeout) as client:
            try:
                response = await client.post(f"{INGESTOR_URL}/event", json=payload, headers=headers)
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                raise ValueError(f"HTTP error in userlens-sdk-py: {e.response.text}")
            except httpx.RequestError as e:
                raise ValueError(f"Request failed in userlens-sdk-py: {str(e)}")

        if response.status_code != 200:
            raise ValueError(f'Error in userlens-sdk-py: {response.json()}')

        return "User identified successfully"

    async def _async_track(self, user_id, event_name, traits = None):
        try:
            import httpx
        except ImportError:
            raise ImportError(
                "httpx is required for async usage. Install it with:\n"
                "pip install userlens-sdk-py[async]"
            )

        if not user_id:
            raise ValueError('Error in userlens-sdk-py: user_id is required')
        
        if not event_name:
            raise ValueError('Error in userlens-sdk-py: event_name is required')

        payload = {
            "type": "track",
            "userId": user_id,
            "event": event_name,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "source": "userlens-sdk-py"
        }
        headers = {
            "Authorization": f"Basic {self.write_code}",
        }

        async with httpx.AsyncClient(timeout=self.requests_timeout) as client:
            try:
                response = await client.post(f"{INGESTOR_URL}/event", json=payload, headers=headers)
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                raise ValueError(f"HTTP error in userlens-sdk-py: {e.response.text}")
            except httpx.RequestError as e:
                raise ValueError(f"Request failed in userlens-sdk-py: {str(e)}")

        if response.status_code != 200:
            raise ValueError(f'Error in userlens-sdk-py: {response.json()}')

        if traits:
            await self._async_identify(user_id, traits)

        return "Event tracked successfully"
