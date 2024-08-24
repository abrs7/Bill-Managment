# Bill and Payment Management System

This project is a simple Bill and Payment Management System built using Django and Django REST Framework. It allows users to manage their bills and payments through a RESTful API.

## Features

- **User Registration and Authentication**: Users can register, log in, and obtain an authentication token to access the API.
- **Bill Management**: Users can create, view, update, and delete bills.
- **Payment Management**: Users can create, view, update, and delete payments.
- **Token-Based Authentication**: Secure the API endpoints using token authentication.

## API Endpoints

### User Authentication
- **Register**: `POST /register/`  
  Allows a new user to register.
  
- **Login**: `POST /api/token/`  
  Returns an authentication token for a registered user.

### Bills
- **List Bills**: `GET /api/v1/bills/`  
  View all bills (requires authentication).
  
- **Create Bill**: `POST /api/v1/bills/`  
  Create a new bill (requires authentication).

### Payments
- **List Payments**: `GET /api/v1/payments/`  
  View all payments (requires authentication).
  
- **Create Payment**: `POST /api/v1/payments/`  
  Create a new payment (requires authentication).

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
