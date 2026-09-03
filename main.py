import os
import json
import sqlite3

from dotenv import load_dotenv
from google import genai
from sample_emails import sample_emails

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)

for customer_email in sample_emails:

    print("\n" + "=" * 50)
    print("Processing new customer email")
    print("=" * 50)

    prompt = f"""
Analyze this customer support email.

Return ONLY this format:

Category: Billing
Priority: High
Order Number: 4821
Action: Investigate duplicate payment

Do not add any explanation.

Customer email:
{customer_email}
"""

    try:
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=prompt
        )
    except Exception as e:
        print(f"\nGemini API error: {e}")
        print("Skipping this email and continuing...")
        continue

    raw_output = interaction.output_text.strip()

    result = {}

    for line in raw_output.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()

    print("\n--- AI Triage Result ---")
    print(json.dumps(result, indent=2))

    category = result.get("Category")
    priority = result.get("Priority")

    if category == "Billing" and priority == "High":
        decision = "Human Review Required"
    elif priority == "High":
        decision = "Human Review Required"
    elif category == "Shipping" and priority == "Low":
        decision = "Auto Reply"
    else:
        decision = "Standard Support Queue"

    print("\n--- Business Decision ---")
    print(decision)

    order_number = result.get("Order Number")

    connection = sqlite3.connect("support.db")
    cursor = connection.cursor()

    order = None

    if order_number and order_number != "N/A":
        cursor.execute("""
            SELECT order_number, customer_name, status, amount, payment_status
            FROM orders
            WHERE order_number = ?
        """, (order_number,))

        order = cursor.fetchone()

    print("\n--- Order Lookup ---")

    if order:
        print(f"Order Number: {order[0]}")
        print(f"Customer: {order[1]}")
        print(f"Status: {order[2]}")
        print(f"Amount: ${order[3]}")
        print(f"Payment Status: {order[4]}")
    else:
        print("Order not found.")

    if category == "Billing" and priority == "High":
        issue = "Possible duplicate payment"
        recommended_action = "Human investigation required"

    elif category == "Shipping" and order and order[2] != "Delivered":
        issue = "Order delivery issue"
        recommended_action = "Check shipping status"

    elif category in ["Technical Support", "Account Access"]:
        issue = "Account or technical access problem"
        recommended_action = "Assist with account recovery or technical troubleshooting"

    else:
        issue = "No critical issue detected"
        recommended_action = "Continue standard support process"

    print("\n--- Issue Detection ---")
    print(f"Issue: {issue}")
    print(f"Recommended Action: {recommended_action}")

    if decision == "Human Review Required":
        review_status = "Pending Review"
    else:
        review_status = "Auto Processed"

    cursor.execute("""
        INSERT INTO tickets (
            customer_email,
            category,
            priority,
            order_number,
            action,
            decision,
            issue,
            review_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        customer_email.strip(),
        category,
        priority,
        order_number,
        result.get("Action"),
        decision,
        issue,
        review_status
    ))

    connection.commit()
    connection.close()

    print("\n--- Ticket Saved ---")
    print("Triage result saved successfully.")
    print(f"Review Status: {review_status}")


print("\n" + "=" * 50)
print("All sample emails processed successfully!")
print("=" * 50)
