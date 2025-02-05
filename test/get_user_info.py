import requests

# URL for fetching user profile
url = "http://localhost:8000/api/users/"

# Assuming you already have an access token from login
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjo0ODkyMzU3Mjc1LCJpYXQiOjE3Mzg3NTcyNzUsImp0aSI6Ijg2M2VjZTc2ZjdmZDQ1MTQ5NTIxMWJlMTVhMmU1Y2E3IiwidXNlcl9pZCI6Mn0.Hgsk1SxouieCnOo9fG1EJsQUGM7qqjuTdfu_bAWhScw"

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