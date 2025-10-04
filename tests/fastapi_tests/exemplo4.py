import requests

URL = "http://127.0.0.1:8000"

response = requests.get(URL)

print(response.json)