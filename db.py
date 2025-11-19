from sqlalchemy import create_engine
from pathlib import Path

def get_engine():
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    db_path = data_dir / "datawarehouse.db"
    db_url = f"sqlite:///{db_path}"
    return create_engine(db_url, echo=False, future=True)
