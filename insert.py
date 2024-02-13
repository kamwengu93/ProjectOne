import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE VALUES (1,'FAITH KARIMI',34, 34000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (2,'MERCY KANIMI',24, 20500.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (3,'BEN KEINO',28, 29500.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (4,'AGNES OLOO',48, 140000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (5,'MARTIN OPIYO',58, 40000.00)")

conn.commit()
print("Employee inserted successfully")
conn.close()