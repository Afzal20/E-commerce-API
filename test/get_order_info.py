import requests

url = "http://localhost:8000/api/orders/"
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjo0ODkyMzU3Mjc1LCJpYXQiOjE3Mzg3NTcyNzUsImp0aSI6Ijg2M2VjZTc2ZjdmZDQ1MTQ5NTIxMWJlMTVhMmU1Y2E3IiwidXNlcl9pZCI6Mn0.Hgsk1SxouieCnOo9fG1EJsQUGM7qqjuTdfu_bAWhScw"

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)

orders = response.json()
print(len(orders))
print("\n")

if response.status_code == 200:
    print("Orders retrieved successfully!")
    print("Orders:", orders)
else:
    print(f"Error: {response.status_code}")
    print("Response:", response.text)

