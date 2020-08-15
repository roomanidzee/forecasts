from tests import async_adapter
from pathlib import Path
from src.db.client import DBClient
from src.db.classes import City, WeatherInfo
from src.db.mappers import map_to_weather_info

@async_adapter
async def test_city_queries(test_database_url):

    db_client = DBClient(test_database_url, True)

    await db_client.insert_city(City('test', 1.0, 1.0, 'test'))
    await db_client.insert_city(City('test1', 2.0, 2.0, 'test1'))

    results = await db_client.select_cities()

    assert results[0].name == 'test'
    assert results[1].name == 'test1'

@async_adapter
async def test_weather_queries(test_database_url, test_json):

    db_client = DBClient(test_database_url, False)
    weather_info = map_to_weather_info(test_json)

    await db_client.insert_weather_info(weather_info)

    results = await db_client.select_weather_info()

    assert len(results) == 40

    assert results[0].city_api_id == 524901
    assert results[0].dt == 1485799200

