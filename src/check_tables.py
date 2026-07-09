import duckdb

con = duckdb.connect("database/airbnb.duckdb")

tables = con.execute("SHOW TABLES").fetchall()

print("Tables in database:")

for table in tables:
    print(table[0])

con.close()