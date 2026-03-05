import requests

BASE = "http://127.0.0.1:5000"

#1.
response = requests.get(f"{BASE}/")
print(f"[WELCOME] {response.status_code} -> {response.text}")

#2.
response = requests.get(f"{BASE}/about")
print(f"[ABOUT] {response.json()}")

#3.
response = requests.get(f"{BASE}/greet/Sarah")
print(f"[GREET] {response.text}")

#4.
response = requests.get(f"{BASE}/calculate?num1=10&num2=5&operation=add")
print(f"[Calc add] {response.json()}")
response = requests.get(f"{BASE}/calculate?num1=10&num2=5&operation=multiply")
print(f"[Calc multiply] {response.json()}")

#5.
# 5. Echo (POST)
response = requests.post(f"{BASE}/echo", json={"message": "Hello"})
print(f"Status: {response.status_code}")
print(f"Raw response: {response.text}")
print(f"[Echo] {response.json()}")

#6.
response = requests.get(f"{BASE}/status/404")
print(f"[Status 404] {response.status_code} -> {response.text}")
response = requests.get(f"{BASE}/status/200")
print(f"[Status 200] {response.status_code} -> {response.text}")

#7.
response = requests.get(f"{BASE}/")
print(f"[Custom Header] {response.headers.get('X-Custom-Header')}")

#8.
response = requests.get(f"{BASE}/calculate?num1=10&num2=0&operation=divide")
print(f"[Div by zero] {response.status_code} -> {response.text}")