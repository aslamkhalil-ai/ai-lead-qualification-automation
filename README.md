# AI Lead Qualification & Automation System

An intelligent lead management system built with **Python, Flask, MySQL, and n8n** that automatically receives, qualifies, stores, and routes business leads based on their priority.

## Overview

Businesses often lose potential customers because leads are not processed quickly or followed up consistently.

This project automates the lead qualification process through a Flask REST API and an n8n workflow. It evaluates incoming leads, assigns a priority, stores lead information in MySQL, and enables automated email notifications.

## Key Features

- **Automated Lead Intake:** Receive lead data through webhooks.
- **Lead Qualification:** Categorize leads as Hot, Warm, or Cold.
- **REST API:** Process lead data using Flask.
- **MySQL Integration:** Store qualified leads in a database.
- **Workflow Automation:** Connect the API with n8n.
- **Email Notifications:** Route leads based on priority using Gmail integration.
- **API Testing:** Test webhook requests with Python and Requests.
- **Environment-Based Configuration:** Keep sensitive credentials out of source control.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend logic and API integration |
| Flask | REST API development |
| MySQL | Lead data storage |
| n8n | Workflow automation |
| Gmail | Automated email notifications |
| Requests | HTTP requests and webhook testing |
| Git & GitHub | Version control and project hosting |

## How It Works

1. A new lead enters the n8n workflow through a webhook.
2. n8n sends the lead information to the Flask API.
3. Flask evaluates the lead and assigns a priority.
4. The qualified lead is stored in MySQL.
5. The API returns the lead details and qualification result.
6. n8n checks the lead priority and routes the appropriate email notification.
7. A Python test script helps verify the webhook integration.
## Workflow Architecture

The following diagram shows how the lead qualification system connects n8n, the Flask REST API, MySQL, and automated email notifications.


(lead-automation-workflow.png)

**Workflow overview:**
1. Receive lead data through an n8n webhook.
2. Send the lead to the Flask API for qualification.
3. Save lead information in MySQL.
4. Route the lead according to its priority.
5. Send the appropriate email notification.

## Project Structure

```text
ai-lead-qualification-automation/
├── app.py
├── test_webhook.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── workflows/
    └── lead-automation.json
```

*Note: Keep this structure aligned with the actual files committed to the repository. The `workflows/lead-automation.json` and `.env.example` files are optional unless you have created them.*

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aslamkhalil-ai/ai-lead-qualification-automation.git
cd ai-lead-qualification-automation
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Configure the Flask application and MySQL connection using environment variables.

Example configuration:

```env
FLASK_DEBUG=False
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
```

Use the exact variable names expected by `app.py`. Do not commit real passwords, API keys, or other secrets to GitHub.

### 5. Start the Flask API

```bash
python app.py
```

The API should start on the host and port configured in your application.

### 6. Test the Webhook

Ensure the Flask API and n8n workflow are configured correctly, then run:

```bash
python test_webhook.py
```

Check the terminal output and API response to verify that lead qualification and database storage work as expected.

## Example API Response

The following is an illustrative example of a successful response:

```json
{
  "status": "success",
  "message": "Lead saved and qualified successfully",
  "lead": {
    "id": 1,
    "name": "Ali Khan",
    "email": "ali@example.com",
    "lead_score": 80,
    "priority": "Hot"
  }
}
```

The actual response fields and scoring rules depend on your implementation.

## Security Practices

- Store credentials in environment variables.
- Keep `.env` and `.venv/` out of version control.
- Never publish database passwords or private API credentials.
- Use placeholder values in example configuration files.
- Disable Flask debug mode in production.

## Future Improvements

- Lead analytics dashboard.
- Configurable lead-scoring rules.
- Automatic retry and error handling.
- CRM integration.
- Cloud deployment and production monitoring.

## Author

**Aslam Khalil**

GitHub: [@aslamkhalil-ai](https://github.com/aslamkhalil-ai)

---

*Built to demonstrate practical skills in backend development, database integration, API testing, and AI-powered business workflow automation.*
