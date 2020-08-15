import pytest
import json
from tests import async_adapter
from pathlib import Path
from src.client import WeatherAPIClient

test_file_path = (
    Path(__file__).parent / Path("resources") / Path("response_example.json")
)


with open(str(test_file_path), "r") as file:
    json_data = file.read().replace("\n", "")


@pytest.mark.server(
    url="/data/2.5/forecast",
    response=json.loads(json_data),
    method="GET",
)
@async_adapter
async def test_client_weather_retrieve():

    api_client = WeatherAPIClient('http://localhost:5000', 'test')

    response = await api_client.get_weather_info('1')

    assert isinstance(response, dict)

    assert response['message'] == 0.0036
    assert len(response['list']) == 40
