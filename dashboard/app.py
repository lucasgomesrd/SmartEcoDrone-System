import streamlit as st
import requests

st.title("🚁 Smart Eco Drone Dashboard")

API_URL = "http://127.0.0.1:5000/telemetry"

try:
    response = requests.get(API_URL)
    dados = response.json()

    if dados:
        ultimo = dados[-1]

        st.subheader("📍 Latest Telemetry")

        st.write(f"Latitude: {ultimo['latitude']}")
        st.write(f"Longitude: {ultimo['longitude']}")
        st.write(f"Battery: {ultimo['battery_pct']}%")

        # STATUS
        if ultimo["battery_pct"] < 20:
            st.error("🔴 LOW BATTERY")
        else:
            st.success("🟢 NORMAL")

    else:
        st.warning("No data received yet.")

except:
    st.error("Error connecting to API")
