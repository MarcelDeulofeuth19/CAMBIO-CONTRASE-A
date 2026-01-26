import requests

API_URL = "http://98.91.0.246:3000/reports/journey-notification"
payload = {
    "variable1": "mdeulofeuth@alocredit.co",
    "variable2": "2"
}

try:
    response = requests.post(API_URL, json=payload, timeout=10)
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    try:
        print(f"Response JSON: {response.json()}")
    except Exception as e:
        print(f"No JSON response: {e}")
except Exception as e:
    print(f"Error: {e}")
