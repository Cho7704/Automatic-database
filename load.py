from sqlalchemy import text
from src.db import get_engine

def load_dim_city(cities_df):
    engine = get_engine()
    with engine.begin() as conn:
        for _, row in cities_df.iterrows():
            stmt = text("""
                INSERT OR REPLACE INTO dim_city (city_id, city_name, lat, lon)
                VALUES (:city_id, :city_name, :lat, :lon)
            """)
            conn.execute(stmt, dict(row))
    print("dim_city chargée")

def load_fact_weather(df):
    engine = get_engine()
    with engine.begin() as conn:
        for _, row in df.iterrows():
            stmt = text("""
                INSERT INTO fact_weather (city_id, dt, temp_k, humidity, wind_speed, weather_description, source)
                VALUES (:city_id, :dt, :temp_k, :humidity, :wind_speed, :weather_description, :source)
            """)
            conn.execute(stmt, dict(row))
    print("fact_weather chargée")
