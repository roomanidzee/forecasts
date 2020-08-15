from src.db.classes import City, WeatherInfo
from src.utils import convert
from typing import List


def map_to_city(input_val: dict) -> City:
    """Convert part of input json to City class"""

    return City(
        name=input_val["city"]["name"],
        lat_coord=input_val["city"]["coord"]["lat"],
        lon_coord=input_val["city"]["coord"]["lon"],
        country=input_val["city"]["country"],
    )

def map_to_weather_info(input_val: dict) -> List[WeatherInfo]:
    """Convert part of input json to list of WeatherInfo classes"""

    input_list = input_val['list']
    city_api_id = input_val['city']['id']

    return [
        WeatherInfo(
            city_api_id=city_api_id,
            dt=elem['dt'],
            dt_txt=elem['dt_txt'],
            temp=convert(elem['main']['temp']),
            temp_min=convert(elem['main']['temp_min']),
            temp_max=convert(elem['main']['temp_max']),
            pressure=elem['main']['pressure'],
            sea_level=elem['main']['sea_level'],
            grnd_level=elem['main']['grnd_level'],
            humidity=elem['main']['humidity'],
            wind_speed=elem['wind']['speed'],
            wind_degree=elem['wind']['deg']
        )
        for elem in input_list
    ]


