import duckdb
import pandas as pd

print("Connecting to DuckDB...")

# Connect to database
con = duckdb.connect("database/airbnb.duckdb")

# Load dataset
df = pd.read_csv("data/processed/featured_listings.csv")

# Create table
con.execute("""
CREATE OR REPLACE TABLE listings AS
SELECT * FROM df
""")

# Verify
count = con.execute("SELECT COUNT(*) FROM listings").fetchone()[0]

print(f"✅ Database created successfully!")
print(f"Total Rows: {count}")

con.close()