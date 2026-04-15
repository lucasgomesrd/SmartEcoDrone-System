def analyze(data):
    alerts = []

    if data["battery_pct"] < 20:
        alerts.append("Low battery")

    if data.get("signal_dbm", -80) < -100:
        alerts.append("Weak signal")

    if data.get("speed_mps", 0) > 20:
        alerts.append("High speed")

    if alerts:
        return {"status": "WARNING", "alerts": alerts}

    return {"status": "NORMAL", "alerts": []}
