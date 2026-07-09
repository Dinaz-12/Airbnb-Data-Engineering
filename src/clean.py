import pandas as pd
from pathlib import Path

# Project Paths
RAW_DATA = Path("data/raw")
PROCESSED_DATA = Path("data/processed")

# Create processed folder if it doesn't exist
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

# Load listings dataset
listings = pd.read_csv(RAW_DATA / "listings.csv")

print("✅ Listings dataset loaded successfully!")
print(listings.shape)


#Missing Values Analysis
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)

missing = listings.isnull().sum()

missing = missing[missing > 0].sort_values(ascending=False)

print(missing)


#Duplicate Check
print("\n" + "=" * 50)
print("DUPLICATE RECORDS")
print("=" * 50)

duplicates = listings.duplicated().sum()

print(f"Duplicate Rows: {duplicates}")


#Check Data Types
print("\n" + "=" * 50)
print("DATA TYPES")
print("=" * 50)

print(listings.dtypes)

#Check Price Column
print("\n" + "=" * 50)
print("PRICE SAMPLE")
print("=" * 50)

print(listings["price"].head(10))


# Add Cleaning Code
print("\n" + "=" * 50)
print("DATA CLEANING")
print("=" * 50)

# 1. Remove columns with 100% missing values
empty_columns = listings.columns[listings.isnull().all()]

print(f"Removing {len(empty_columns)} completely empty columns...")

listings.drop(columns=empty_columns, inplace=True)

# 2. Clean Price Column
listings["price"] = (
    listings["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

listings["price"] = pd.to_numeric(
    listings["price"],
    errors="coerce"
)

# 3. Remove records with missing prices
before = len(listings)

listings = listings.dropna(subset=["price"])

after = len(listings)

print(f"Removed {before-after} rows with missing prices.")

# 4. Remove invalid prices
listings = listings[listings["price"] > 0]

print("Price column cleaned successfully.")

#Save Clean Dataset
from pathlib import Path

processed_path = Path("data/processed")
processed_path.mkdir(parents=True, exist_ok=True)

output_file = processed_path / "clean_listings.csv"

listings.to_csv(output_file, index=False)

print(f"\n✅ Clean dataset saved successfully!")
print(f"Location : {output_file}")

print("\nFinal Dataset Shape:")
print(listings.shape)