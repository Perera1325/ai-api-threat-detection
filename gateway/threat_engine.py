def calculate_threat_level(metrics):

    allowed = metrics["allowed"]
    blocked = metrics["blocked"]

    total = allowed + blocked

    if total == 0:
        return "LOW"

    ratio = blocked / total

    if ratio < 0.1:
        return "LOW"

    if ratio < 0.3:
        return "MEDIUM"

    if ratio < 0.6:
        return "HIGH"

    return "CRITICAL"