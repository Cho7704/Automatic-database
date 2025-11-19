import pandas as pd

def transform(weather_df, cities_df):
    if "city" in weather_df.columns and "city_name" not in weather_df.columns:
        weather_df = weather_df.rename(columns={"city": "city_name"})
    merged = pd.merge(weather_df, cities_df, on="city_name", how="left")
    merged["dt"] = pd.to_datetime(merged["dt"]).astype(str)
    print("Fusion OK :", merged.shape)
    return merged

def prepare_for_load(df):
    df = df.copy()
    if "temp_c" in df.columns:
        df["temp_k"] = df["temp_c"].astype(float) + 273.15
    cols = ["city_id","dt","temp_k","humidity","wind_speed","weather_description","source"]
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df = df[cols]
    return df
