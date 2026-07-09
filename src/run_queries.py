import duckdb

con = duckdb.connect("database/airbnb.duckdb")

queries = [
    ("Query 1", "SELECT COUNT(*) AS total_listings FROM listings;"),
    ("Query 2", "SELECT ROUND(AVG(price),2) AS average_price FROM listings;"),
    ("Query 3", """
        SELECT room_type,
               COUNT(*) AS total_listings,
               ROUND(AVG(price),2) AS average_price
        FROM listings
        GROUP BY room_type
        ORDER BY average_price DESC;
    """)
]

for title, query in queries:
    print(f"\n===== {title} =====")
    print(con.execute(query).fetchdf())

con.close()