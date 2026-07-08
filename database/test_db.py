import sqlite3

conn = sqlite3.connect("database/hobbyfi.db")
cursor = conn.cursor()

print("USERS")
for row in cursor.execute("SELECT * FROM users"):
    print(row)

print("\nREVENUE")
for row in cursor.execute("SELECT * FROM revenue"):
    print(row)

conn.close()