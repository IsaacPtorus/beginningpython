import sqlite3

conn = sqlite3.connect("MyEmployees.db")
print("Connection successful")

data = conn.execute("SELECT * FROM MyEmployees")
for employee in data:
    print("ID: ", employee[0])
    print("FIRSTNAME: ", employee[1])
    print("LASTNAME: ", employee[2])
    print("AGE: ", employee[3])
    print("SALARY: ", employee[4])
    print("POSITION: ", employee[5])

print("successfully fetched data")
conn.close()