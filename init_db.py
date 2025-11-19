from sqlalchemy import create_engine, text
from pathlib import Path

def init_db():
    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "data" / "datawarehouse.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    engine = create_engine(f"sqlite:///{db_path}", echo=False, future=True)

    ddl = """
    CREATE TABLE IF NOT EXISTS dim_city (
        city_id INTEGER PRIMARY KEY,
        city_name TEXT NOT NULL,
        lat REAL,
        lon REAL
    );

    CREATE TABLE IF NOT EXISTS fact_weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        dt TEXT,
        temp_k REAL,
        humidity INTEGER,
        wind_speed REAL,
        weather_description TEXT,
        source TEXT,
        FOREIGN KEY (city_id) REFERENCES dim_city(city_id)
    );
    """

    with engine.begin() as conn:
        for stmt in ddl.strip().split(";"):
            if stmt.strip():
                conn.execute(text(stmt))

    print("Base de données initialisée")

if __name__ == "__main__":
    init_db()
