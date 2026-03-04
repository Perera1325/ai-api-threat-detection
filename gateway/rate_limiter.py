request_counter = {}

def check_rate_limit(ip):

    if ip not in request_counter:
        request_counter[ip] = 1
    else:
        request_counter[ip] += 1

    if request_counter[ip] > 20:
        return "limit_exceeded"

    return "ok"