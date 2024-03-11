import sqlite3
con = sqlite3.connect("ces.db")

cur = con.cursor()

cur.execute("select * from students")

res = cur.execute("SELECT * FROM students")
whathappen = res.fetchone()

print(whathappen)
