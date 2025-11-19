from src.init_db import init_db
from src.extract_api import extract_api
from src.extract_csv import extract_csv
from src.transform import transform, prepare_for_load
from src.load import load_dim_city, load_fact_weather

def run():
    init_db()
    weather = extract_api()
    cities = extract_csv()
    merged = transform(weather, cities)
    prepared = prepare_for_load(merged)
    load_dim_city(cities)
    load_fact_weather(prepared)
    print("ETL terminé")

if __name__ == "__main__":
    run()
