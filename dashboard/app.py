import streamlit as st
import requests

st.title("AI API Security Monitoring Dashboard")

metrics_url = "http://127.0.0.1:8000/metrics"

data = requests.get(metrics_url).json()

st.metric("Allowed Requests", data["allowed"])
st.metric("Blocked Requests", data["blocked"])

st.write("Real-time API threat monitoring system")