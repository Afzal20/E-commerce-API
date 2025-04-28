import requests

# URL for fetching user profile
url = "http://localhost:8000/api/users/"

# Assuming you already have an access token from login
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjo0ODkzODAwMzIzLCJpYXQiOjE3NDAyMDAzMjMsImp0aSI6ImI1ZjRjYTE3NWI5MjRkYTI5NTY2MTgyZTA4NmNmYWFmIiwidXNlcl9pZCI6M30.ZxXjD7FnUHAtNIDnixsW7LpUvRx34NC1Pl89l90Lx-8"

# Headers for the request including the access token
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# Making the GET request
response = requests.get(url, headers=headers)

# Checking the response
if response.status_code == 200:
    print("Profile fetch successful!")
    print("User Profile:", response.json())
else:
    print(f"Error: {response.status_code}")
    print("Response:", response.text)