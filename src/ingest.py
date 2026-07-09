import pandas as pd

RAW_DATA = "data/raw"

listings = pd.read_csv(f"{RAW_DATA}/listings.csv")
calendar = pd.read_csv(f"{RAW_DATA}/calendar.csv")
reviews = pd.read_csv(f"{RAW_DATA}/reviews.csv")
neighbourhoods = pd.read_csv(f"{RAW_DATA}/neighbourhoods.csv")

print("✅ All datasets loaded successfully!")

print("\nListings Shape:", listings.shape)
print("Calendar Shape:", calendar.shape)
print("Reviews Shape:", reviews.shape)
print("Neighbourhoods Shape:", neighbourhoods.shape)

print("\nFirst 5 rows of Listings:")
print(listings.head())