
# AI Lead Qualification & Automation System

An automated lead management system built with Python, Flask, MySQL, and n8n to receive, qualify, store, and route business leads.

## Overview

This project connects a Flask REST API with an n8n automation workflow to process incoming leads and send email notifications based on their priority.

## Features

- Webhook-based lead intake using n8n
- REST API integration with Flask
- Lead storage using MySQL
- Hot, Warm, and Cold lead qualification
- Automated Gmail notifications for lead priorities
- Python script for webhook testing
- API response and workflow execution monitoring

## Tech Stack

- Python
- Flask
- REST API
- MySQL
- n8n
- Gmail integration
- Requests

## Workflow Architecture

1. A new lead is submitted to the n8n webhook.
2. n8n sends the lead data to the Flask API.
3. The API qualifies the lead and saves it to MySQL.
4. n8n checks the returned lead priority.
5. The workflow routes the lead to the relevant email notification.
6. The Python test script sends requests to the webhook for testing.

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

*Adjust the file structure to match the actual files in your repository.*

## Setup

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the required packages:

   `pip install -r requirements.txt`

4. Configure the required environment variables for Flask and MySQL.
5. Start the Flask API.
6. Import the n8n workflow and configure your webhook, API endpoint, and Gmail credentials.
7. Run `python test_webhook.py` to test the webhook.

## Security

- Keep API keys, passwords, and OAuth credentials out of source control.
- Store secrets in environment variables.
- Use placeholder values in example configuration files.

## Future Improvements

- Add a lead analytics dashboard.
- Introduce configurable lead-scoring rules.
- Add retry handling and workflow error notifications.
- Deploy the API to a production hosting platform.

## Author

**Aslam Khalil**

GitHub: [@aslamkhalil-ai](https://github.com/aslamkhalil-ai)
