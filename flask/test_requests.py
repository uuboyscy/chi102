import requests

res = requests.get("http://127.0.0.1:5001/poker?player=5")

print(res.json())
print(type(res.json()))
