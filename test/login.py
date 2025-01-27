import requests

url = "http://localhost:8000/dj-rest-auth/login/" 
headers = {
    "Content-Type": "application/json"
}

data = {
    "username": "",  
    "email": "new_user@example.com", 
    "password": "!@#$%^&*"  
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Login successful!")
    print("Response:", response.json())
else:
    print(f"Error: {response.status_code}")
    print("Response:", response.text)
