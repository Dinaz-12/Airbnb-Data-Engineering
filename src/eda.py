import pandas as pd
import matplotlib.pyplot as plt

# Load featured dataset
df = pd.read_csv("data/processed/featured_listings.csv")

print("Dataset Loaded Successfully")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

#Price Distribution
plt.figure(figsize=(8,5))
plt.hist(df["price"], bins=30)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Listings")

plt.savefig("reports/price_distribution.png")
plt.show()


#Room Type Distribution
plt.figure(figsize=(8,5))

df["room_type"].value_counts().plot(kind="bar")

plt.title("Room Type Distribution")
plt.xlabel("Room Type")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("reports/room_type_distribution.png")
plt.show()


#Average Price by Room Type
avg_price = df.groupby("room_type")["price"].mean()

plt.figure(figsize=(8,5))

avg_price.plot(kind="bar")

plt.title("Average Price by Room Type")
plt.ylabel("Average Price")

plt.tight_layout()

plt.savefig("reports/average_price_room_type.png")
plt.show()