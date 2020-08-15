
from src.db.mappers import map_to_city, map_to_weather_info

def test_map_to_city(test_json):
    city = map_to_city(test_json)

    assert city.name == "Moscow"
    assert city.lat_coord == 55.7522
    assert city.lon_coord == 37.6156

def test_map_to_weather_info(test_json):

    weather_info = map_to_weather_info(test_json)

    assert len(weather_info) == 40
    assert weather_info[0].city_api_id == 524901
    assert weather_info[0].dt == 1485799200


