import os
from flask import Flask, request, jsonify

app = Flask(__name__)

API_TOKEN = os.getenv("API_TOKEN", "change-me")

@app.route("/telemetry", methods=["POST"])
def receive_telemetry():
    token = request.headers.get("Authorization")

    if token != API_TOKEN:
        return {"error": "Unauthorized"}, 403

    data = request.json

    required = ["drone_id", "latitude", "longitude", "battery_pct"]
    missing = [f for f in required if f not in data]

    if missing:
        return {"error": "Invalid payload", "missing": missing}, 400

    return {"status": "accepted"}

if __name__ == "__main__":
    app.run(debug=True)
