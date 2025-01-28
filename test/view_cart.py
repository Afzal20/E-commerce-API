import requests

# Base URL of your API
BASE_URL = "http://localhost:8000/api"

# Authentication token (access token)
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjo0ODkxNTgzMDI0LCJpYXQiOjE3Mzc5ODMwMjQsImp0aSI6ImIzMzU4MjczZDFjZjQ4YzY4OTc3N2ZhMWJjMDg3OTgwIiwidXNlcl9pZCI6Mn0.RN4ONI5MELM_tiHfLj3EiGMjfbqPu2v4TFZXdqoIPow"

# Headers for authenticated requests
HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

# Test item details
PRODUCT_ID = "CKSS"
QUANTITY = 2


def get_item_details(product_id):
    """Fetch item details using product_id."""
    url = f"{BASE_URL}/items/?product_id={product_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print("Item Details:")
        item_details = response.json()
        print(item_details)
        return item_details[0]  # Assuming the first item is the one we need
    else:
        print(f"Failed to fetch item details: {response.status_code} - {response.text}")
        return None

def view_cart():
    """Fetch the cart details."""
    url = f"{BASE_URL}/cart/"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        cart_details = response.json()
        print("Cart Details:")
        print(cart_details)
        print(f"Total number of carts: {len(cart_details)}")  # Count the number of carts
    else:
        print(f"Failed to fetch cart details: {response.status_code} - {response.text}")


if __name__ == "__main__":
    print("Testing Add to Cart API...")

    item_details = get_item_details(PRODUCT_ID)
    view_cart()
