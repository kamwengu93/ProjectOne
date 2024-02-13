import sqlite3
conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")

conn.execute("UPDATE EMPLOYEE SET SALARY = 500000.00 WHERE ID = 5")
conn.commit()


cursor = conn.execute("SELECT * FROM EMPLOYEE")
for row in cursor:
    print("ID :", row[0])
    print("NAME :", row[1])
    print("AGE :", row[2])
    print("SALARY :", row[3])

print("Update done successfully")
conn.close()