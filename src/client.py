from aiohttp import ClientSession


class WeatherAPIClient:

    request_url = "{0}/data/2.5/forecast?id={1}&appid={2}"

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    async def get_weather_info(self, city_id: str) -> dict:
        """
        Retrieve weather information about city by his id
        """
        async with ClientSession() as session:
            async with session.get(
                self.request_url.format(self.base_url, city_id, self.api_key)
            ) as response:

                return await response.json()
