import duckdb

con = duckdb.connect("database/airbnb.duckdb")

with open("sql/00_star_schema.sql", "r") as f:
    sql = f.read()

con.execute(sql)

print("✅ Star Schema Tables Created Successfully")

tables = con.execute("SHOW TABLES").fetchall()

print("\nTables in Database:")

for table in tables:
    print(table[0])

con.close()