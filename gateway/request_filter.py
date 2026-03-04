import logging

from ai_engine.anomaly_detector import detect_anomaly
from gateway.rate_limiter import check_rate_limit
from gateway.ip_reputation import check_ip
from gateway.metrics import record

logging.basicConfig(filename="logs/gateway.log", level=logging.INFO)

def analyze_request(data):

    ip = data.get("ip","unknown")
    rpm = data.get("requests_per_minute",10)

    logging.info(f"Incoming request from {ip} RPM:{rpm}")

    # blacklist check
    if check_ip(ip) == "blocked":
    record("blocked")
    return "block"

if check_rate_limit(ip) == "limit_exceeded":
    record("blocked")
    return "block"

if result == "anomaly":
    record("blocked")
    return "block"

record("allowed")
return "allow"