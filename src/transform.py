import pandas as pd
from pathlib import Path

# Load cleaned dataset
df = pd.read_csv("data/processed/clean_listings.csv")

print("✅ Clean dataset loaded")
print(df.shape)


#Check Columns
print("\nColumns:")
for column in df.columns:
    print(column)


print("\n" + "=" * 50)
print("FEATURE ENGINEERING")
print("=" * 50)

# 1. Price Per Bedroom
df["price_per_bedroom"] = df["price"] / df["bedrooms"]

# 2. Occupancy Rate (0 - 1)
df["occupancy_rate"] = (
    (365 - df["availability_365"]) / 365
).round(2)

# 3. Revenue Per Available Day
df["revenue_per_available_day"] = (
    df["estimated_revenue_l365d"] / 365
).round(2)

# 4. Reviews Per Year
df["reviews_per_year"] = (
    df["reviews_per_month"] * 12
).round(2)

# 5. Professional Host Flag
df["professional_host"] = (
    df["host_listings_count"] > 1
)

print("✅ Feature engineering completed.")


# Handle Missing Values
# Replace infinite values
df.replace([float("inf"), float("-inf")], pd.NA, inplace=True)

# Fill missing values
df["price_per_bedroom"] = df["price_per_bedroom"].fillna(df["price"])

df["reviews_per_year"] = df["reviews_per_year"].fillna(0)

df["occupancy_rate"] = df["occupancy_rate"].fillna(0)

df["revenue_per_available_day"] = df["revenue_per_available_day"].fillna(0)


#Verify New Features
print("\nNew Features")

print(
    df[
        [
            "price",
            "bedrooms",
            "price_per_bedroom",
            "occupancy_rate",
            "reviews_per_year",
            "professional_host"
        ]
    ].head()
)

# Save Dataset
output = Path("data/processed/featured_listings.csv")

df.to_csv(output, index=False)

print(f"\n✅ Feature engineered dataset saved to {output}")

print("\nFinal Shape")
print(df.shape)