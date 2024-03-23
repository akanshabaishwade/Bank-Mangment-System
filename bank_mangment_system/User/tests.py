import requests

url = 'http://127.0.0.1:8000/login/'
data = {
    "email": "test@example.com",
    "password": "testpassword"
}
response = requests.post(url, data=data)

if response.status_code == 200:
    print("Login successful")
else:
    print("Login failed:", response.json())