import psycopg2 as pg


conn = pg.connect("dbname=harrykd user=postgres")

cur = conn.cursor()

cur.execute("SELECT * from notes")

records = cur.fetchall()

for record in records:
    print(record)

cur.close()

conn.close()



