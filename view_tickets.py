import sqlite3

connection = sqlite3.connect("support.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT
        id,
        customer_email,
        category,
        priority,
        order_number,
        action,
        decision,
        issue,
        review_status,
        created_at
    FROM tickets
""")

tickets = cursor.fetchall()

connection.close()

print("\n--- Saved Support Tickets ---\n")

for ticket in tickets:
    print(f"Ticket ID: {ticket[0]}")
    print(f"Email: {ticket[1]}")
    print(f"Category: {ticket[2]}")
    print(f"Priority: {ticket[3]}")
    print(f"Order Number: {ticket[4]}")
    print(f"Action: {ticket[5]}")
    print(f"Decision: {ticket[6]}")
    print(f"Issue: {ticket[7]}")
    print(f"Review Status: {ticket[8]}")
    print(f"Created At: {ticket[9]}")
    print("-" * 40)
    
    