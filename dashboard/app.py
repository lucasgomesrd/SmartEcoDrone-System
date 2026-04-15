import streamlit as st
import requests

st.set_page_config(page_title="Drone Dashboard", layout="wide")

st.title("🚁 Smart Eco Drone Dashboard")

API_URL = "http://127.0.0.1:5000/telemetry"

try:
    response = requests.get(API_URL)
    dados = response.json()

    if dados:
        ultimo = dados[-1]

        st.subheader("📍 Latest Telemetry")

        col1, col2, col3 = st.columns(3)

        col1.metric("🔋 Battery", f"{ultimo['battery_pct']}%")
        col2.metric("🚀 Speed", f"{ultimo.get('speed_mps', 0)} m/s")
        col3.metric("📡 Signal", f"{ultimo.get('signal_dbm', 0)} dBm")

        col4, col5 = st.columns(2)
        col4.metric("📍 Latitude", round(ultimo["latitude"], 5))
        col5.metric("📍 Longitude", round(ultimo["longitude"], 5))

        # STATUS INTELIGENTE
        st.subheader("🧠 System Status")

        alerts = []

        if ultimo["battery_pct"] < 20:
            alerts.append("🔴 Low Battery")

        if ultimo.get("signal_dbm", -80) < -100:
            alerts.append("📡 Weak Signal")

        if ultimo.get("speed_mps", 0) > 20:
            alerts.append("🚀 High Speed")

        if alerts:
            for alert in alerts:
                st.error(alert)
        else:
            st.success("🟢 All systems normal")

        # HISTÓRICO
        st.subheader("📊 Telemetry History")

        baterias = [d["battery_pct"] for d in dados]
        st.line_chart(baterias)

    else:
        st.warning("No data received yet.")

except Exception as e:
    st.error(f"Error: {e}")
