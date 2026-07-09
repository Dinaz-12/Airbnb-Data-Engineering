import pandas as pd
from pathlib import Path

# Load cleaned dataset
df = pd.read_csv("data/processed/clean_listings.csv")

print("=" * 50)
print("DATA VALIDATION")
print("=" * 50)

# Price validation
invalid_price = df[df["price"] <= 0]
print(f"Invalid Prices : {len(invalid_price)}")

# Latitude validation
invalid_lat = df[(df["latitude"] < -90) | (df["latitude"] > 90)]
print(f"Invalid Latitude : {len(invalid_lat)}")

# Longitude validation
invalid_lon = df[(df["longitude"] < -180) | (df["longitude"] > 180)]
print(f"Invalid Longitude : {len(invalid_lon)}")

# Duplicate validation
print(f"Duplicate Rows : {df.duplicated().sum()}")

print("\n✅ Validation Completed Successfully")