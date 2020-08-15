from dataclasses import dataclass


@dataclass
class City:
    name: str
    lat_coord: float
    lon_coord: float
    country: str

@dataclass
class WeatherInfo:
    city_api_id: int
    dt: int
    dt_txt: str
    temp: float
    temp_min: float
    temp_max: float
    pressure: float
    sea_level: float
    grnd_level: float
    humidity: int
    wind_speed: float
    wind_degree: float
