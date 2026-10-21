
import requests

url = "https://muhammadaslam2.app.n8n.cloud/webhook/new-lead"

leads = [
    {
        "name": "Ali Khan",
        "email": "ali@example.com",
        "message": "I urgently need AI automation for my business and pricing",
        "expected": "Hot"
    },
    {
        "name": "Ahmed Raza",
        "email": "ahmed@example.com",
        "message": "I am interested in your services and would like to know more",
        "expected": "Warm"
    },
    {
        "name": "Usman Ali",
        "email": "usman@example.com",
        "message": "Just browsing, not interested right now",
        "expected": "Cold"
    }
]

for lead in leads:
    data = {
        "name": lead["name"],
        "email": lead["email"],
        "message": lead["message"]
    }

    print("\n" + "=" * 40)
    print("Testing:", lead["expected"], "Lead")
    print("Name:", lead["name"])

    try:
        response = requests.post(url, json=data, timeout=30)

        print("Status Code:", response.status_code)
        print("Response:", response.text)

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)
        break
