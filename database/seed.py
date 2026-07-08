import sqlite3

conn = sqlite3.connect("database/hobbyfi.db")
cursor = conn.cursor()




users = [
    ("Rahul Sharma", "rahul@gmail.com", "Badminton", "Trial", "2026-07-15"),
    ("Priya Singh", "priya@gmail.com", "Football", "Premium", "2026-12-31"),
    ("Aman Verma", "aman@gmail.com", "Cricket", "Gold", "2026-11-20"),
    ("Riya Gupta", "riya@gmail.com", "Badminton", "Premium", "2026-10-10"),
    ("Arjun Kumar", "arjun@gmail.com", "Tennis", "Trial", "2026-07-20"),
    ("Neha Sharma", "neha@gmail.com", "Swimming", "Gold", "2026-09-15"),
    ("Karan Patel", "karan@gmail.com", "Football", "Trial", "2026-07-18"),
    ("Ananya Roy", "ananya@gmail.com", "Badminton", "Premium", "2027-01-01"),
    ("Rohit Das", "rohit@gmail.com", "Cricket", "Gold", "2026-12-05"),
    ("Sneha Jain", "sneha@gmail.com", "Tennis", "Trial", "2026-07-22")
]

cursor.executemany("""
INSERT INTO users(name,email,sport,membership,trial_end)
VALUES(?,?,?,?,?)
""", users)

# Revenue
payments = [
    ("Rahul Sharma", 500, "2026-07-08"),
    ("Priya Singh", 700, "2026-07-08"),
    ("Aman Verma", 400, "2026-07-08"),
    ("Riya Gupta", 600, "2026-07-08"),
    ("Arjun Kumar", 350, "2026-07-08"),
    ("Rahul Sharma", 500, "2026-07-09"),
    ("Neha Sharma", 800, "2026-07-09"),
    ("Karan Patel", 450, "2026-07-09"),
    ("Ananya Roy", 700, "2026-07-09"),
    ("Rohit Das", 550, "2026-07-09"),
    ("Sneha Jain", 300, "2026-07-09")
]

cursor.executemany("""
INSERT INTO revenue(customer_name,amount,date)
VALUES(?,?,?)
""", payments)

conn.commit()
conn.close()

print(" Database seeded successfully!")