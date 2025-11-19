import json
from pathlib import Path
import pandas as pd

def extract_api():
    project_root = Path(__file__).resolve().parents[1]
    mock_path = project_root / "data" / "mock_weather.json"
    with open(mock_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df["dt"] = pd.to_datetime(df["dt"]).astype(str)
    print("Données API extraites :", df.shape)
    return df
