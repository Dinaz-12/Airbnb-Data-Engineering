import duckdb

con = duckdb.connect("database/airbnb.duckdb")

print(con.execute("DESCRIBE fact_listings").fetchdf())

con.close()