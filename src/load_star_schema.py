import duckdb

con = duckdb.connect("database/airbnb.duckdb")

print("Loading Star Schema...")

# ------------------------
# Dimension Host
# ------------------------

con.execute("""
INSERT INTO dim_host
SELECT DISTINCT
host_id,
host_name,
host_location,
host_is_superhost,
host_listings_count
FROM listings
""")

# ------------------------
# Dimension Location
# ------------------------

con.execute("""
INSERT INTO dim_location
SELECT DISTINCT
ROW_NUMBER() OVER() AS location_id,
neighbourhood_cleansed,
latitude,
longitude
FROM listings
""")

# ------------------------
# Dimension Review
# ------------------------

con.execute("""
INSERT INTO dim_review
SELECT DISTINCT
ROW_NUMBER() OVER() AS review_id,
review_scores_rating,
reviews_per_month,
number_of_reviews
FROM listings
""")

# ------------------------
# Fact Table
# ------------------------

con.execute("""
INSERT INTO fact_listings

SELECT DISTINCT

id,
host_id,

NULL,
NULL,

price,

occupancy_rate,

estimated_revenue_l365d

FROM listings
""")

print("✅ Star Schema Loaded")

for table in [
    "dim_host",
    "dim_location",
    "dim_review",
    "fact_listings"
]:

    count = con.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(table, count)

con.close()