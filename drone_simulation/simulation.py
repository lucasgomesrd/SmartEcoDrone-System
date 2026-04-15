import random
import requests
import time
from datetime import datetime, timezone

API_URL = "http://127.0.0.1:5000/telemetry"
TOKEN = "change-me"

def collect_telemetry():
    return {
        "drone_id": "DRONE-01",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "latitude": random.uniform(-15.95, -15.70),
        "longitude": random.uniform(-48.05, -47.80),
        "altitude_m": round(random.uniform(60, 140), 1),
        "speed_mps": round(random.uniform(3, 14), 1),
        "heading_deg": random.randint(0, 359),
        "battery_pct": random.randint(15, 100),
        "signal_dbm": random.randint(-110, -60)
    }

def send(data):
    headers = {"Authorization": TOKEN}
    try:
        r = requests.post(API_URL, json=data, headers=headers)
        print(r.status_code, data)
    except:
        print("Error sending data")

while True:
    telemetry = collect_telemetry()
    send(telemetry)
    time.sleep(5)
