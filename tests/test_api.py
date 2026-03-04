import requests
import time

url = "http://127.0.0.1:8000/api"

normal = {
    "ip":"192.168.1.10",
    "requests_per_minute":10
}

attack = {
    "ip":"192.168.1.50",
    "requests_per_minute":500
}

print("Normal request")
print(requests.post(url,json=normal).json())

print("AI attack test")
print(requests.post(url,json=attack).json())

print("Rate limit attack")

for i in range(25):

    r = requests.post(url,json=normal)

    print(i,r.json())

    time.sleep(0.1)