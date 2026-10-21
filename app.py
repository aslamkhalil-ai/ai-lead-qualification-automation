
import os
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)





def get_connection(database=None):
    config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password":""
    }

    if database:
        config["database"] = database

    return mysql.connector.connect(**config)


def setup_database():
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS ai_lead_automation"
        )
        cursor.close()
    finally:
        connection.close()

    connection = get_connection("ai_lead_automation")

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(255) NOT NULL,
                message TEXT NOT NULL,
                lead_score INT NOT NULL DEFAULT 0,
                priority VARCHAR(20) NOT NULL DEFAULT 'Cold',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()
        cursor.close()
    finally:
        connection.close()


def qualify_lead(message):
    message = message.lower()

    score = 0

    high_intent_words = [
        "buy", "purchase", "hire", "urgent",
        "pricing", "quote", "ready", "need"
    ]

    medium_intent_words = [
        "interested", "automation", "service",
        "business", "cost", "information"
    ]

    for word in high_intent_words:
        if word in message:
            score += 20

    for word in medium_intent_words:
        if word in message:
            score += 10

    score = min(score, 100)

    if score >= 60:
        priority = "Hot"
    elif score >= 30:
        priority = "Warm"
    else:
        priority = "Cold"

    return score, priority


@app.route("/")
def home():
    return jsonify({
        "message": "AI Lead Automation API is running!",
        "status": "success"
    })


@app.route("/leads", methods=["POST"])
def receive_lead():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    required_fields = ["name", "email", "message"]

    missing_fields = [
        field for field in required_fields
        if not isinstance(data.get(field), str)
        or not data[field].strip()
    ]

    if missing_fields:
        return jsonify({
            "error": "Missing or invalid required fields",
            "fields": missing_fields
        }), 400

    name = data["name"].strip()
    email = data["email"].strip()
    message = data["message"].strip()

    score, priority = qualify_lead(message)

    connection = None

    try:
        connection = get_connection("ai_lead_automation")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO leads
                (name, email, message, lead_score, priority)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, email, message, score, priority))

        connection.commit()
        lead_id = cursor.lastrowid
        cursor.close()

        return jsonify({
            "status": "success",
            "message": "Lead saved and qualified successfully",
            "lead": {
                "id": lead_id,
                "name": name,
                "email": email,
                "message": message,
                "lead_score": score,
                "priority": priority
            }
        }), 201

    except mysql.connector.Error:
        app.logger.exception("MySQL operation failed")
        return jsonify({
            "error": "Database operation failed. Check server logs."
        }), 500

    finally:
        if connection and connection.is_connected():
            connection.close()


@app.route("/leads", methods=["GET"])
def get_leads():
    connection = None

    try:
        connection = get_connection("ai_lead_automation")
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, name, email, message,
                   lead_score, priority, created_at
            FROM leads
            ORDER BY id DESC
        """)

        leads = cursor.fetchall()
        cursor.close()

        for lead in leads:
            if lead["created_at"]:
                lead["created_at"] = lead["created_at"].isoformat()

        return jsonify({
            "status": "success",
            "count": len(leads),
            "leads": leads
        })

    except mysql.connector.Error:
        app.logger.exception("Could not retrieve leads")
        return jsonify({"error": "Database query failed"}), 500

    finally:
        if connection and connection.is_connected():
            connection.close()




if __name__ == "__main__":
    setup_database()
    print("MySQL database and table are ready.")
    app.run(debug=True, port=5000)
