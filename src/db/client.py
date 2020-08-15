import sqlalchemy
from typing import List
from src.db.models import metadata, cities, weather_info
from src.db.classes import City, WeatherInfo
from databases import Database, DatabaseURL


class DBClient:
    """Client for interacting with cities and weather tables"""

    def __init__(self, db_url: str, create_tables: bool = False):
        self.db_url = db_url

        if create_tables:
            engine = sqlalchemy.create_engine(self.db_url)
            metadata.create_all(engine)

    async def insert_city(self, city: City):
        async with Database(self.db_url) as database:
            async with database.transaction():

                query = cities.insert()
                return await database.execute(query, city.__dict__)

    async def insert_weather_info(self, weather_input: List[WeatherInfo]):

        async with Database(self.db_url) as database:
            async with database.transaction():
                query = weather_info.insert()
                return await database.execute_many(
                    query, [elem.__dict__ for elem in weather_input]
                )

    async def select_cities(self) -> List[dict]:
        async with Database(self.db_url) as database:
            query = cities.select()
            return await database.fetch_all(query)    
    
    async def select_weather_info(self) -> List[dict]:
        async with Database(self.db_url) as database:
            query = weather_info.select()
            return await database.fetch_all(query)
