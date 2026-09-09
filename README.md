# AI Customer Email Triage 📧

An AI-powered customer support email triage system built with **Python, Google Gemini, and SQLite**.

The system analyzes incoming customer emails, classifies the issue, determines priority, extracts order information, applies business rules, and creates a support ticket for further action.

It also includes a **human-in-the-loop review workflow**, allowing people to review AI-generated decisions before they are finalized.

---

## 🎯 Project Overview

Customer support teams often receive large numbers of emails that need to be categorized, prioritized, and routed.

This project demonstrates how AI can automate the initial triage process while keeping important decisions under human control.

### Workflow

```text
Customer Email
      ↓
Gemini AI
      ↓
Email Classification
      ↓
Business Rules
      ↓
Order Database Lookup
      ↓
Issue Detection
      ↓
Ticket Creation
      ↓
Human Review
      ↓
Approve / Reject / Skip
```

---

## ✨ Features

* 🤖 AI-powered email classification using Google Gemini
* 🏷️ Automatic category and priority detection
* 🔢 Order number extraction
* 🗄️ SQLite database for orders and support tickets
* ⚙️ Business-rule-based ticket decisions
* 🔍 Issue detection and recommended actions
* 👤 Human-in-the-loop review workflow
* ✅ Approve, Reject, or Skip review actions
* 📊 Review status tracking
* ⚠️ Gemini API error handling
* 🔐 Environment-based API credential management

---

## 🔄 Example Workflow

### Example 1 — Billing Issue

**Customer Email**

> I was charged twice for my order #4821. Can you help me fix this?

**AI Classification**

* **Category:** Billing
* **Priority:** High
* **Order Number:** 4821
* **Recommended Action:** Investigate duplicate payment

**Business Decision**

**Human Review Required**

The system checks order #4821 in the SQLite database and identifies a possible duplicate payment.

The ticket is then saved with:

**Review Status:** Pending Review

A human reviewer can then approve or reject the AI-generated decision.

---

### Example 2 — Shipping Issue

**Customer Email**

> Where is my order #4822? I haven't received it yet.

The system:

1. Identifies the email as a shipping issue.
2. Extracts order #4822.
3. Looks up the order in SQLite.
4. Checks the current order status.
5. Creates a support ticket based on the available information.

---

## 🧠 Human-in-the-Loop Review

One of the main goals of this project is to demonstrate that AI automation does not always need to make the final decision by itself.

Tickets can be reviewed by a human using:

```text
Approve
Reject
Skip
```

This approach provides an additional control layer for cases where the AI identifies a potentially important or ambiguous issue.

---

## 🛠️ Technology Stack

| Technology        | Purpose                           |
| ----------------- | --------------------------------- |
| Python            | Application logic and automation  |
| Google Gemini API | Email analysis and classification |
| SQLite            | Order and support ticket storage  |
| python-dotenv     | Environment variable management   |
| Git / GitHub      | Version control                   |

---

## 📁 Project Structure

```text
AI-Customer-Email-Triage/
│
├── main.py
├── database.py
├── sample_emails.py
├── view_tickets.py
├── review_tickets.py
├── support.db
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

> `.env` is used locally for API credentials and should not be committed to GitHub.

---

## ⚙️ Setup

### Requirements

* Python 3.10+
* Google Gemini API key
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/linajawad/AI-Customer-Email-Triage.git
cd AI-Customer-Email-Triage
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your real API key to GitHub.

---

## ▶️ Running the Project

Run the main application:

```bash
python main.py
```

Additional scripts are available for working with stored tickets:

```bash
python view_tickets.py
```

```bash
python review_tickets.py
```

The workflow allows AI-generated support tickets to be inspected and reviewed after processing.

---

## 📊 Example Results

The project was tested with sample customer support emails.

Example ticket:

```text
Order: #4821
Category: Billing
Priority: High
Issue: Possible duplicate payment
Review Status: Pending Review
```

Another example:

```text
Order: #4822
Category: Shipping
Priority: Medium
Action: Standard Support Queue
```

These examples demonstrate how the system combines AI classification with database information and business rules before creating a support ticket.

---

## 🔐 Security

* API credentials are stored in `.env`.
* `.env` is excluded from Git using `.gitignore`.
* `.env.example` contains placeholder values only.
* No real API credentials should be committed to the repository.

---

## 🎯 What This Project Demonstrates

This project demonstrates practical experience with:

* AI-powered workflow automation
* LLM-based text classification
* Business rule implementation
* Human-in-the-loop AI systems
* REST API integration
* SQLite database operations
* Automated support-ticket creation
* AI decision review
* Error handling
* Python application development
* Environment configuration
* Git and GitHub

---

## 💡 Why I Built This

I wanted to build a practical AI automation project that solves a real business problem instead of simply sending prompts to an AI model.

This project helped me understand how AI can be combined with **business rules, databases, automation, and human review** to create a more reliable workflow.

The human-review component was especially important because it demonstrates that AI can assist with decisions while still keeping people involved when additional judgment is needed.

---

## 👩‍💻 Author

**Lina Jawad**

AI Automation • AI Agent Testing • QA Automation • Python • API Integration • Cybersecurity

GitHub: [@linajawad](https://github.com/linajawad)
