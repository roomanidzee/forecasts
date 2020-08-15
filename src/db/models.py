import sqlalchemy

metadata = sqlalchemy.MetaData()

cities = sqlalchemy.Table(
    "cities",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=50)),
    sqlalchemy.Column("lat_coord", sqlalchemy.Float),
    sqlalchemy.Column("lon_coord", sqlalchemy.Float),
    sqlalchemy.Column("country", sqlalchemy.String(length=50))
)

weather_info = sqlalchemy.Table(
    "weather_info",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("city_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("dt", sqlalchemy.Integer),
    sqlalchemy.Column("dt_txt", sqlalchemy.String(length=100)),
    sqlalchemy.Column("temp", sqlalchemy.Float),
    sqlalchemy.Column("temp_min", sqlalchemy.Float),
    sqlalchemy.Column("temp_max", sqlalchemy.Float),
    sqlalchemy.Column("pressure", sqlalchemy.Float),
    sqlalchemy.Column("sea_level", sqlalchemy.Float),
    sqlalchemy.Column("grnd_level", sqlalchemy.Float),
    sqlalchemy.Column("humidity", sqlalchemy.Integer),
    sqlalchemy.Column("wind_speed", sqlalchemy.Float),
    sqlalchemy.Column("wind_degree", sqlalchemy.Float)
)
