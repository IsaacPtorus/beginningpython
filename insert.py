import sqlite3

conn = sqlite3.connect("MyEmployees.db")
print("Connection successful")

conn.execute("INSERT INTO MyEmployees VALUES (1,'Mark','Makau',38,100000.00,'Manager')")
conn.execute("INSERT INTO MyEmployees VALUES (2,'Janet','Odipo',28,30000.00,'Manager')")
conn.execute("INSERT INTO MyEmployees VALUES (3,'Osman','Masudi',32,40000.00,'Manager')")
conn.execute("INSERT INTO MyEmployees VALUES (4,'Jackson','Chwele',43,41000.00,'Manager')")
conn.execute("INSERT INTO MyEmployees VALUES (6,'Opiyo','Andayi',26,35000.00,'Manager')")
conn.execute("INSERT INTO MyEmployees VALUES (7,'Ichungwah','Kimani',37,10000.00,'Manager')")

conn.commit()
print("Successfully inserted value into the table")
