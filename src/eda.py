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

# Property Type Distribution
property_counts = df["property_type"].value_counts().head(10)

plt.figure(figsize=(10,6))
property_counts.plot(kind="bar")

plt.title("Top 10 Property Types")
plt.xlabel("Property Type")
plt.ylabel("Number of Listings")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/property_type_distribution.png")

plt.show()

# Top 10 Neighbourhoods
plt.figure(figsize=(10, 6))

df["neighbourhood_cleansed"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Neighbourhoods")
plt.xlabel("Neighbourhood")
plt.ylabel("Number of Listings")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/top_neighbourhoods.png")

plt.show()



# Price by Room Type
plt.figure(figsize=(10, 6))

df.boxplot(column="price", by="room_type")

plt.title("Price Distribution by Room Type")
plt.suptitle("")  # Remove default title
plt.xlabel("Room Type")
plt.ylabel("Price")

plt.tight_layout()

plt.savefig("reports/price_by_roomtype_boxplot.png")

plt.show()


# Correlation Matrix
plt.figure(figsize=(10, 8))

columns = [
    "price",
    "bedrooms",
    "beds",
    "accommodates",
    "review_scores_rating",
    "availability_365",
    "occupancy_rate"
]

corr = df[columns].corr()

plt.imshow(corr)

plt.colorbar()

plt.xticks(range(len(columns)), columns, rotation=90)

plt.yticks(range(len(columns)), columns)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("reports/correlation_matrix.png")

plt.show()


# Occupancy Rate Distribution
plt.figure(figsize=(10, 6))

plt.hist(df["occupancy_rate"], bins=20)

plt.title("Occupancy Rate Distribution")
plt.xlabel("Occupancy Rate")
plt.ylabel("Number of Listings")

plt.tight_layout()

plt.savefig("reports/occupancy_rate_distribution.png")

plt.show()


# Estimated Revenue Distribution
plt.figure(figsize=(10, 6))

plt.hist(df["estimated_revenue_l365d"], bins=30)

plt.title("Estimated Revenue Distribution")
plt.xlabel("Estimated Revenue")
plt.ylabel("Number of Listings")

plt.tight_layout()

plt.savefig("reports/revenue_distribution.png")

plt.show()


# Professional Host Analysis
plt.figure(figsize=(8, 6))

df.groupby("professional_host")["price"].mean().plot(kind="bar")

plt.title("Average Price by Host Type")
plt.xlabel("Professional Host")
plt.ylabel("Average Price")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("reports/professional_host_analysis.png")

plt.show()