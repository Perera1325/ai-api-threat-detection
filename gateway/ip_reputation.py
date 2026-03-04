blacklist = [
    "192.168.1.200",
    "10.0.0.99"
]

def check_ip(ip):

    if ip in blacklist:
        return "blocked"

    return "safe"