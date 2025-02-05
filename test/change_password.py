import requests
import json

# Base URL for your API
BASE_URL = 'http://localhost:8000/dj-rest-auth/'

# JWT tokens for authentication
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjo0ODkyMzU3Mjc1LCJpYXQiOjE3Mzg3NTcyNzUsImp0aSI6Ijg2M2VjZTc2ZjdmZDQ1MTQ5NTIxMWJlMTVhMmU1Y2E3IiwidXNlcl9pZCI6Mn0.Hgsk1SxouieCnOo9fG1EJsQUGM7qqjuTdfu_bAWhScw"

# Headers for authentication
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

def test_change_password():
    url = f"{BASE_URL}password/change/"
    data = {
        "new_password1": "NewPassword123!",  # New password
        "new_password2": "NewPassword123!"   # Confirmation of new password
    }

    response = requests.post(url, headers=headers, json=data)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # If 200, the password was successfully changed
    print("Password change successful:", response.json())

def run_tests():
    test_cases = [
        test_change_password
    ]
    
    for test in test_cases:
        try:
            test()
            print(f"{test.__name__} passed")
        except AssertionError as e:
            print(f"{test.__name__} failed: {str(e)}")

if __name__ == "__main__":
    run_tests()