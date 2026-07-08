import sqlite3

conn = sqlite3.connect("database/hobbyfi.db")
cursor = conn.cursor()

#USER
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    sport TEXT,
    membership TEXT,
    trial_end TEXT
)
""")

#REVENUE
cursor.execute("""
CREATE TABLE IF NOT EXISTS revenue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL
)
""")


conn.commit()
conn.close()

print("Database Created Successfully!")