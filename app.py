import streamlit as st
import requests

st.title("Drone Monitoring System")

API_URL = "http://127.0.0.1:5000/telemetry"

st.write("System running...")

try:
    r = requests.get(API_URL)
    st.write(r.json())
except:
    st.error("API not running")
