import sqlite3
from datetime import date, timedelta

conn = sqlite3.connect("database/hobbyfi.db")
cursor = conn.cursor()


today = date.today()
yesterday = today - timedelta(days=1)
two_days = today - timedelta(days=2)
three_days = today - timedelta(days=3)

users = [
    ("Rahul Sharma", "rahul@gmail.com", "Badminton", "Trial", str(today + timedelta(days=7))),
    ("Priya Singh", "priya@gmail.com", "Football", "Premium", str(today + timedelta(days=180))),
    ("Aman Verma", "aman@gmail.com", "Cricket", "Gold", str(today + timedelta(days=120))),
    ("Riya Gupta", "riya@gmail.com", "Badminton", "Premium", str(today + timedelta(days=90))),
    ("Arjun Kumar", "arjun@gmail.com", "Tennis", "Trial", str(today + timedelta(days=14))),
    ("Neha Sharma", "neha@gmail.com", "Swimming", "Gold", str(today + timedelta(days=60))),
    ("Karan Patel", "karan@gmail.com", "Football", "Trial", str(today + timedelta(days=10))),
    ("Ananya Roy", "ananya@gmail.com", "Badminton", "Premium", str(today + timedelta(days=200))),
    ("Rohit Das", "rohit@gmail.com", "Cricket", "Gold", str(today + timedelta(days=150))),
    ("Sneha Jain", "sneha@gmail.com", "Tennis", "Trial", str(today + timedelta(days=20)))
]

cursor.executemany("""
INSERT INTO users(name,email,sport,membership,trial_end)
VALUES(?,?,?,?,?)
""", users)

payments = [

    # Today
    ("Rahul Sharma", 500, str(today)),
    ("Priya Singh", 700, str(today)),
    ("Aman Verma", 400, str(today)),
    ("Riya Gupta", 600, str(today)),
    ("Arjun Kumar", 350, str(today)),

    # Yesterday
    ("Neha Sharma", 800, str(yesterday)),
    ("Karan Patel", 450, str(yesterday)),
    ("Ananya Roy", 700, str(yesterday)),

    # Two days ago
    ("Rohit Das", 550, str(two_days)),
    ("Sneha Jain", 300, str(two_days)),

    # Three days ago
    ("Rahul Sharma", 900, str(three_days)),
    ("Riya Gupta", 650, str(three_days)),
]

cursor.executemany("""
INSERT INTO revenue(customer_name,amount,date)
VALUES(?,?,?)
""", payments)

conn.commit()
conn.close()

print("✅ Database seeded successfully!")