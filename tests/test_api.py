import requests

url = "http://127.0.0.1:8000/api"

headers = {
    "x-api-key":"123456"
}

data = {
    "ip":"192.168.1.10",
    "requests_per_minute":10
}

r = requests.post(url,json=data,headers=headers)

print(r.json())