import logging
from ai_engine.anomaly_detector import detect_anomaly

logging.basicConfig(filename="logs/gateway.log", level=logging.INFO)

def analyze_request(data):

    ip = data.get("ip","unknown")
    rpm = data.get("requests_per_minute",10)

    logging.info(f"Request from {ip} RPM:{rpm}")

    result = detect_anomaly(rpm)

    if result == "anomaly":
        logging.warning(f"Blocked suspicious traffic from {ip}")
        return "block"

    return "allow"