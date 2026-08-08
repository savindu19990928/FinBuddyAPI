# FinBuddy API Documentation

Welcome to the API Documentation for the Personal Finance Management System (FinBuddy). This document outlines the available RESTful endpoints for the application.

## Authentication

The API uses JSON Web Tokens (JWT) for authentication. For protected endpoints, you must include the token in the `Authorization` header:
`Authorization: Bearer <your_access_token>`

### 1. Register User
- **Endpoint**: `POST /api/auth/register/`
- **Description**: Registers a new user and automatically creates their associated profile.
- **Payload**:
  ```json
  {
      "username": "johndoe",
      "email": "john@example.com",
      "password": "strongpassword123",
      "first_name": "John",
      "last_name": "Doe",
      "profile": {
          "phone_number": "+123456789",
          "preferred_currency": "USD",
          "time_zone": "America/New_York"
      }
  }
  ```

### 2. Login (Obtain Token)
- **Endpoint**: `POST /api/auth/login/`
- **Description**: Authenticates a user and returns an access and refresh token.
- **Payload**:
  ```json
  {
      "username": "johndoe",
      "password": "strongpassword123"
  }
  ```
- **Response**:
  ```json
  {
      "refresh": "eyJhbGciOi...",
      "access": "eyJhbGciOi..."
  }
  ```

### 3. Refresh Token
- **Endpoint**: `POST /api/auth/login/refresh/`
- **Description**: Refreshes an expired access token using the refresh token.
- **Payload**:
  ```json
  {
      "refresh": "eyJhbGciOi..."
  }
  ```
- **Response**:
  ```json
  {
      "access": "eyJhbGciOi..."
  }
  ```

### 4. User Profile
- **Endpoint**: `GET, PUT, PATCH /api/auth/profile/`
- **Description**: Retrieves or updates the currently authenticated user's profile information.
- **Headers**: `Authorization: Bearer <token>`
- **Response (GET)**:
  ```json
  {
      "id": 1,
      "username": "johndoe",
      "email": "john@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "profile": {
          "phone_number": "+123456789",
          "profile_picture": null,
          "preferred_currency": "USD",
          "time_zone": "America/New_York",
          "notification_preferences": {}
      }
  }
  ```

---

## Finances

All endpoints under the `/api/finances/` prefix require JWT authentication. 

### 1. Accounts
Represents the financial accounts (e.g., Cash, Bank, Digital Wallets) for the user.

- **List Accounts**: `GET /api/finances/accounts/`
  - *Returns all accounts belonging to the authenticated user.*
- **Create Account**: `POST /api/finances/accounts/`
  - *Payload*:
    ```json
    {
        "name": "Main Bank Account",
        "account_type": "Bank",
        "balance": "5000.00"
    }
    ```
- **Retrieve Account**: `GET /api/finances/accounts/{id}/`
- **Update Account**: `PUT, PATCH /api/finances/accounts/{id}/`
- **Delete Account**: `DELETE /api/finances/accounts/{id}/`

### 2. Categories
Represents system default categories and custom user-created categories for income and expenses.

- **List Categories**: `GET /api/finances/categories/`
  - *Returns all system-default categories and the authenticated user's custom categories.*
- **Create Custom Category**: `POST /api/finances/categories/`
  - *Payload*:
    ```json
    {
        "name": "Freelance Design",
        "category_type": "INCOME"
    }
    ```
- **Retrieve Category**: `GET /api/finances/categories/{id}/`
- **Update Category**: `PUT, PATCH /api/finances/categories/{id}/`
- **Delete Category**: `DELETE /api/finances/categories/{id}/`

### 3. Transactions
Represents the income, expenses, and money transfers for a user.

- **List Transactions**: `GET /api/finances/transactions/`
  - *Returns all transactions belonging to the authenticated user.*
- **Create Transaction**: `POST /api/finances/transactions/`
  - *Payload*:
    ```json
    {
        "account": 1,
        "category": 2,
        "transaction_type": "EXPENSE",
        "amount": "150.00",
        "date": "2026-08-08T12:00:00Z",
        "description": "Grocery shopping",
        "merchant": "Supermarket"
    }
    ```
- **Retrieve Transaction**: `GET /api/finances/transactions/{id}/`
- **Update Transaction**: `PUT, PATCH /api/finances/transactions/{id}/`
- **Delete Transaction**: `DELETE /api/finances/transactions/{id}/`

---

*Note: Budgeting, Subscriptions, and Support API endpoints will be added to this document as they are fully implemented in the ViewSets.*
