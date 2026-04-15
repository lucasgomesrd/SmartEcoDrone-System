import os
from flask import Flask, request, jsonify

app = Flask(__name__)

API_TOKEN = os.getenv("API_TOKEN", "change-me")

dados_recebidos = []

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

    dados_recebidos.append(data)

    return {"status": "accepted"}


@app.route("/telemetry", methods=["GET"])
def get_telemetry():
    return jsonify(dados_recebidos)


if __name__ == "__main__":
    app.run(debug=True)
