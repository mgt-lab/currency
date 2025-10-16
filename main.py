import requests

result = requests.get("https://httpbin.org/get")
print(result.text)