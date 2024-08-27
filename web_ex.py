import requests

response = requests.get(url="https://www.google.com")

print(response.text)