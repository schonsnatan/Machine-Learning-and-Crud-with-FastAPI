import requests
from datetime import datetime

def fetch_url(url):
    response = requests.get(url)
    return response.text

def main():
    ini = datetime.now()
    urls = ["https://example.com"]*10
    responses = [fetch_url(url) for url in urls]
    for response in responses:
        print(response[:100])
    fim = datetime.now() - ini
    print(fim)

main()