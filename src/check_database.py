import duckdb

con = duckdb.connect("database/airbnb.duckdb")

print(
    con.execute(
        "SELECT * FROM listings LIMIT 5"
    ).fetchdf()
)

con.close()