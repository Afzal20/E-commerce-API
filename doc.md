# Saving the content to a .md file as requested by the user

content = """
# E-commerce API Documentation

## Overview
This API provides access to the e-commerce platform, allowing you to manage products, orders, carts, users, and more. It supports common operations such as listing, retrieving, creating, updating, and deleting resources.

### Base URL:  
`https://http://localhost:8000/api/`

---

## Endpoints

### 1. **Districts**
- **URL**: `/api/districts/`
- **Methods**: `GET`, `POST`
- **Description**: Manage districts for product delivery.

### 2. **Categories**
- **URL**: `/api/categories/`
- **Methods**: `GET`, `POST`
- **Description**: Manage product categories.

### 3. **Item Types**
- **URL**: `/api/item-types/`
- **Methods**: `GET`, `POST`
- **Description**: Manage different types of items.

### 4. **Sizes**
- **URL**: `/api/sizes/`
- **Methods**: `GET`, `POST`
- **Description**: Manage sizes for items.

### 5. **Ratings**
- **URL**: `/api/ratings/`
- **Methods**: `GET`, `POST`
- **Description**: Manage item ratings.

### 6. **Colors**
- **URL**: `/api/colors/`
- **Methods**: `GET`, `POST`
- **Description**: Manage item colors.

### 7. **Items**
- **URL**: `/api/items/`
- **Methods**: `GET`, `POST`
- **Description**: Manage items in the store.

### 8. **Item Images**
- **URL**: `/api/item-images/`
- **Methods**: `GET`, `POST`
- **Description**: Manage images for items.

### 9. **Item Sizes**
- **URL**: `/api/item-sizes/`
- **Methods**: `GET`, `POST`
- **Description**: Manage available sizes for items.

### 10. **Item Colors**
- **URL**: `/api/item-colors/`
- **Methods**: `GET`, `POST`
- **Description**: Manage available colors for items.

### 11. **Carts**
- **URL**: `/api/carts/`
- **Methods**: `GET`, `POST`
- **Description**: Manage shopping carts.

### 12. **Order Items**
- **URL**: `/api/order-items/`
- **Methods**: `GET`, `POST`
- **Description**: Manage individual items in an order.

### 13. **Orders**
- **URL**: `/api/orders/`
- **Methods**: `GET`, `POST`
- **Description**: Manage orders.

### 14. **Sliders**
- **URL**: `/api/sliders/`
- **Methods**: `GET`, `POST`
- **Description**: Manage sliders on the homepage.

### 15. **Billing Addresses**
- **URL**: `/api/billing-addresses/`
- **Methods**: `GET`, `POST`
- **Description**: Manage billing addresses.

### 16. **Payments**
- **URL**: `/api/payments/`
- **Methods**: `GET`, `POST`
- **Description**: Manage payments for orders.

### 17. **Coupons**
- **URL**: `/api/coupons/`
- **Methods**: `GET`, `POST`
- **Description**: Manage discount coupons.

### 18. **Refunds**
- **URL**: `/api/refunds/`
- **Methods**: `GET`, `POST`
- **Description**: Manage order refunds.

### 19. **Get Item by Product ID**
- **URL**: `/api/items/<str:product_id>/`
- **Methods**: `GET`
- **Description**: Retrieve item details using its `product_id`.

---

## User Authentication Endpoints

### 1. **Register User**
- **URL**: `/api/users/register/`
- **Methods**: `POST`
- **Description**: Register a new user account.
- **Body Parameters**: 
  - `username`: string, required
  - `email`: string, required
  - `password`: string, required

### 2. **Login User**
- **URL**: `/api/users/login/`
- **Methods**: `POST`
- **Description**: Log in an existing user.
- **Body Parameters**: 
  - `username`: string, required
  - `password`: string, required

### 3. **Logout User**
- **URL**: `/api/users/logout/`
- **Methods**: `POST`
- **Description**: Log out the current user.

### 4. **Get User Info**
- **URL**: `/api/users/user/`
- **Methods**: `GET`
- **Description**: Retrieve information about the currently authenticated user.

---

## Authentication
- All endpoints (except user registration and login) require authentication.
- Use JWT tokens for authentication in requests.

---

## React.js Developer User Guide

### 1. **Setting up Axios in React**

First, install Axios in your React project:
```cmd
npm install axios
````

```` js
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
});

// Optionally, set the JWT token in headers for authenticated requests
API.interceptors.request.use((req) => {
  if (localStorage.getItem('token')) {
    req.headers.Authorization = `Bearer ${localStorage.getItem('token')}`;
  }
  return req;
});

export default API;
````

### 2. **user registation**

```` js

import API from './api';

const registerUser = async (userData) => {
  try {
    const response = await API.post('users/register/', userData);
    console.log('User registered:', response.data);
  } catch (error) {
    console.error('Error registering user:', error);
  }
};

// Example usage
registerUser({
  username: 'newuser',
  email: 'newuser@example.com',
  password: 'password123',
});
````

### 3. **user login**

```` js
import API from './api';

const loginUser = async (credentials) => {
  try {
    const response = await API.post('users/login/', credentials);
    // Store JWT token in localStorage
    localStorage.setItem('token', response.data.token);
    console.log('Logged in successfully:', response.data);
  } catch (error) {
    console.error('Error logging in:', error);
  }
};

// Example usage
loginUser({
  username: 'existinguser',
  password: 'password123',
});
````
