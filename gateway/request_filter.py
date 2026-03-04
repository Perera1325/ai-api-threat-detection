import logging

from ai_engine.anomaly_detector import detect_anomaly
from gateway.rate_limiter import check_rate_limit
from gateway.ip_reputation import check_ip
from gateway.metrics import record

logging.basicConfig(filename="logs/gateway.log", level=logging.INFO)


def analyze_request(data):

    ip = data.get("ip", "unknown")
    rpm = data.get("requests_per_minute", 10)

    logging.info(f"Incoming request from {ip} RPM:{rpm}")

    # Blacklist check
    if check_ip(ip) == "blocked":
        logging.warning(f"Blacklisted IP blocked: {ip}")
        record("blocked")
        return "block"

    # Rate limit check
    if check_rate_limit(ip) == "limit_exceeded":
        logging.warning(f"Rate limit exceeded by {ip}")
        record("blocked")
        return "block"

    # AI anomaly detection
    result = detect_anomaly(rpm)

    if result == "anomaly":
        logging.warning(f"AI detected anomaly from {ip}")
        record("blocked")
        return "block"

    record("allowed")
    return "allow"