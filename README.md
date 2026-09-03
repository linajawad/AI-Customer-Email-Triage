# AI Customer Email Triage

An AI-powered customer support email triage system built with Python, Gemini, and SQLite.

The system analyzes incoming customer emails, classifies the issue, determines priority, checks order information, applies business rules, and saves the resulting support ticket to a database.

It also includes a human-in-the-loop review workflow for tickets that require manual approval.

## Project Overview

Customer support teams often receive large numbers of emails that need to be categorized, prioritized, and routed.

This project demonstrates how AI can assist with that process while keeping important decisions under human control.

The workflow is:

Customer Email
→ Gemini AI
→ Email Classification
→ Business Rules
→ Order Database Lookup
→ Issue Detection
→ Ticket Storage
→ Human Review

## Features

- AI-powered email classification using Google Gemini
- Automatic category and priority detection
- Order number extraction
- SQLite database for orders and support tickets
- Business-rule-based ticket decisions
- Issue detection and recommended actions
- Human-in-the-loop review workflow
- Approve, Reject, or Skip review actions
- Review status tracking
- Error handling for Gemini API failures
- Environment variable support for API credentials

## Example Workflow

### Example 1 — Billing Issue

Customer email:

> I was charged twice for my order #4821. Can you help me fix this?

AI classification:

- Category: Billing
- Priority: High
- Order Number: 4821
- Action: Investigate duplicate payment

Business decision:

**Human Review Required**

The system also checks order #4821 in the SQLite database and identifies the issue as a possible duplicate payment.

The ticket is then saved with:

**Review Status: Pending Review**

A human can later approve or reject the ticket.

### Example 2 — Shipping Issue

Customer email:

> Where is my order #4822? I haven't received it yet.

The system identifies the email as a shipping issue, looks up the order, and checks its current status.

## Technology Stack

- Python
- Google Gemini API
- SQLite
- python-dotenv
- Git / GitHub

## Project Structure

```text
AI-Customer-Email-Triage/
│
├── main.py
├── database.py
├── sample_emails.py
├── view_tickets.py
├── review_tickets.py
├── support.db
├── .gitignore
├── .env
└── README.md
