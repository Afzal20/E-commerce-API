import requests

url = "http://localhost:8000/dj-rest-auth/registration/" 
headers = {
    "Content-Type": "application/json"
}

data = {
    "email": "new_user@example.com", 
    "password1": "!@#$%^&*",  
    "password2": "!@#$%^&*"  
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Registration successful!")
    print("Response:", response.json())
else:
    print(f"Error: {response.status_code}")
    print("Response:", response.text)
