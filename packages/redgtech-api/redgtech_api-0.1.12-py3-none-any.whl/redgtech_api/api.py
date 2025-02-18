import aiohttp
import logging

_LOGGER = logging.getLogger(__name__)

API_URL = "https://redgtech-dev.com"

class RedgtechAPI:
    def __init__(self, token=None):
        self._token = token
        self._session = None

    async def _get_session(self):
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self):
        if self._session:
            await self._session.close()

    async def login(self, email, password):
        url = f"{API_URL}/home_assistant/login"
        session = await self._get_session()
        async with session.post(url, json={'email': email, 'password': password}) as response:
            response.raise_for_status()
            data = await response.json()
            self._token = data.get('access_token')
            return self._token

    async def get_data(self):
        url = f"{API_URL}/home_assistant?access_token={self._token}"
        session = await self._get_session()
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()

    async def set_switch_state(self, endpoint_id, state):
        id_part, after_id = endpoint_id.split("-", 1)
        number_channel = after_id[-1]
        type_channel = ''.join(char for char in after_id if char.isalpha())
        state_char = 'l' if state else 'd'
        value = f"{number_channel}{state_char}" if type_channel == "AC" else f"{type_channel}{number_channel}*{state_char}*"
        url = f"{API_URL}/home_assistant/execute/{id_part}?cod=?{value}"
        headers = {"Authorization": f"{self._token}"}
        session = await self._get_session()
        async with session.get(url, headers=headers) as response:
            return response.status == 200
    
    async def set_light_brightness(self, endpoint_id, brightness):
        id_part, after_id = endpoint_id.split("-", 1)
        number_channel = after_id[-1]
        type_channel = ''.join(char for char in after_id if char.isalpha())
        brightness_value = round((brightness / 255) * 100)
        value = f"{type_channel}{number_channel}*{brightness_value}*"
        url = f"{API_URL}/home_assistant/execute/{id_part}?cod=?{value}"
        headers = {"Authorization": f"{self._token}"}
        async with self._session.get(url, headers=headers) as response:
            return response.status == 200