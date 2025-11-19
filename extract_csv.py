from pathlib import Path
import pandas as pd

def extract_csv():
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "data" / "cities.csv"
    df = pd.read_csv(csv_path)
    print("Données CSV extraites :", df.shape)
    return df
