import logging

from ai_engine.anomaly_detector import detect_anomaly
from gateway.rate_limiter import check_rate_limit
from gateway.ip_reputation import check_ip

logging.basicConfig(filename="logs/gateway.log", level=logging.INFO)

def analyze_request(data):

    ip = data.get("ip","unknown")
    rpm = data.get("requests_per_minute",10)

    logging.info(f"Incoming request from {ip} RPM:{rpm}")

    # blacklist check
    if check_ip(ip) == "blocked":
        logging.warning(f"Blacklisted IP blocked: {ip}")
        return "block"

    # rate limit check
    if check_rate_limit(ip) == "limit_exceeded":
        logging.warning(f"Rate limit exceeded by {ip}")
        return "block"

    # AI anomaly detection
    result = detect_anomaly(rpm)

    if result == "anomaly":
        logging.warning(f"AI detected anomaly from {ip}")
        return "block"

    return "allow"