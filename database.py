import sqlite3

DATABASE = "support.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Create orders table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_number TEXT PRIMARY KEY,
        customer_name TEXT,
        status TEXT,
        amount REAL,
        payment_status TEXT
    )
""")

# Create tickets table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_email TEXT,
        category TEXT,
        priority TEXT,
        order_number TEXT,
        action TEXT,
        decision TEXT,
        issue TEXT,
        review_status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Sample orders
orders = [
    ("4821", "Lina", "Completed", 99.99, "Paid"),
    ("4822", "Sarah", "Shipped", 49.99, "Paid"),
    ("4823", "John", "Processing", 79.99, "Paid")
]

cursor.executemany("""
    INSERT OR IGNORE INTO orders
    (order_number, customer_name, status, amount, payment_status)
    VALUES (?, ?, ?, ?, ?)
""", orders)

connection.commit()
connection.close()

print("Database created successfully!")


