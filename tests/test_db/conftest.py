import pytest
import json

from pathlib import Path


@pytest.fixture()
def test_json():
    file_path = str(
        Path(__file__).parent.parent / Path("resources") / Path("response_example.json")
    )

    with open(str(file_path), "r") as file:
        json_data = file.read().replace("\n", "")
    
    return json.loads(json_data)

@pytest.fixture()
def test_database_url():

    file_path = str(
        Path(__file__).parent.parent / Path("resources") / Path("test.db")
    )

    return 'sqlite:////{0}'.format(file_path)
