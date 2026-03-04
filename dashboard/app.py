import streamlit as st
import requests

st.title("AI API Security Monitoring Dashboard")

metrics_url = "http://127.0.0.1:8000/metrics"

data = requests.get(metrics_url).json()

st.metric("Allowed Requests", data["allowed"])
st.metric("Blocked Requests", data["blocked"])

st.write("Real-time API threat monitoring system")

threat_url = "http://127.0.0.1:8000/threat-level"

threat = requests.get(threat_url).json()

st.subheader("System Threat Level")

st.metric("Threat Level", threat["threat_level"])

level = threat["threat_level"]

if level == "LOW":
    st.success("System Secure")

elif level == "MEDIUM":
    st.warning("Suspicious Activity Detected")

elif level == "HIGH":
    st.error("High Attack Traffic")

else:
    st.error("CRITICAL SECURITY ALERT")