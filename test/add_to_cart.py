import requests

# Base URL of your API
BASE_URL = "http://localhost:8000/api"

# Authentication token (replace with a valid token)
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3OTc4MTE0LCJpYXQiOjE3Mzc5NzYzMTQsImp0aSI6IjU3Zjk0OWQ4YTJhNDRiZWU5MmQyZjdjYTdjYmQzYzE1IiwidXNlcl9pZCI6M30.NLdIzlW9lLqxw15RiZAThHLcdfOvcm4NE0bSLR9Z7Xs"

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
        return item_details[0]  
    else:
        print(f"Failed to fetch item details: {response.status_code} - {response.text}")
        return None


def add_to_cart(item_details):
    """Test adding an item to the cart."""
    if not item_details:
        print("No item details available to add to cart.")
        return

    url = f"{BASE_URL}/cart/add/"
    payload = {
        "item": item_details['id'],  
        "item_color_code": item_details['item_color'][0]['color']['code'],  # First color code
        "item_size": item_details['item_size'][0]['size']['name'],  # First size name
        "quantity": QUANTITY,
        "applied_coupon": None
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 201:
        print("Item successfully added to cart!")
        print(response.json())
    else:
        print(f"Failed to add to cart: {response.status_code} - {response.text}")


def view_cart():
    """Fetch the cart details."""
    url = f"{BASE_URL}/cart/"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print("Cart Details:")
        print(response.json())
    else:
        print(f"Failed to fetch cart details: {response.status_code} - {response.text}")


if __name__ == "__main__":
    print("Testing Add to Cart API...")

    item_details = get_item_details(PRODUCT_ID)
    add_to_cart(item_details)
    view_cart()
