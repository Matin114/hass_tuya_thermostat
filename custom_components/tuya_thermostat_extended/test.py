import requests
import time

url = "https://openapi.tuyaeu.com/v1.0/token?grant_type=1"
headers = {
    "client_id": "fqnf7sj7vpu5xm9eta45",
    "secret": "40684c26e34747b2bc9e25848929c8cc",
    "t": str(int(time.time() * 1000))
}

response = requests.get(url, headers=headers)
print(response.json())