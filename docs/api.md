# HotelHub PMS API Documentation

## Authentication

### Register User
```http
POST /api/auth/register
```

Request body:
```json
{
    "email": "user@example.com",
    "password": "securepassword",
    "first_name": "John",
    "last_name": "Doe"
}
```

Response:
```json
{
    "id": 1,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "user"
}
```

### Login
```http
POST /api/auth/login
```

Request body:
```json
{
    "email": "user@example.com",
    "password": "securepassword"
}
```

Response:
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "token_type": "bearer"
}
```

## Rooms

### List Rooms
```http
GET /api/rooms
```

Query parameters:
- `status`: Filter by room status (available, occupied, maintenance)
- `type`: Filter by room type
- `min_price`: Minimum price per night
- `max_price`: Maximum price per night

Response:
```json
{
    "rooms": [
        {
            "id": 1,
            "room_number": "101",
            "room_type": "Standard",
            "capacity": 2,
            "price_per_night": 100.00,
            "status": "available",
            "amenities": ["WiFi", "TV", "Air Conditioning"]
        }
    ]
}
```

### Create Room
```http
POST /api/rooms
```

Request body:
```json
{
    "room_number": "101",
    "room_type": "Standard",
    "capacity": 2,
    "price_per_night": 100.00,
    "description": "A comfortable standard room",
    "amenities": ["WiFi", "TV", "Air Conditioning"],
    "floor": 1
}
```

## Bookings

### Create Booking
```http
POST /api/bookings
```

Request body:
```json
{
    "room_id": 1,
    "check_in_date": "2024-03-15",
    "check_out_date": "2024-03-17",
    "number_of_guests": 2,
    "special_requests": "Late check-in"
}
```

### Get Booking
```http
GET /api/bookings/{booking_id}
```

Response:
```json
{
    "id": 1,
    "room": {
        "id": 1,
        "room_number": "101",
        "room_type": "Standard"
    },
    "check_in_date": "2024-03-15",
    "check_out_date": "2024-03-17",
    "status": "confirmed",
    "total_price": 200.00,
    "number_of_guests": 2
}
```

## Payments

### Process Payment
```http
POST /api/payments
```

Request body:
```json
{
    "booking_id": 1,
    "amount": 200.00,
    "payment_method": "credit_card",
    "card_token": "tok_visa"
}
```

### Get Payment Status
```http
GET /api/payments/{payment_id}
```

Response:
```json
{
    "id": 1,
    "booking_id": 1,
    "amount": 200.00,
    "status": "succeeded",
    "transaction_id": "ch_1234567890"
}
```

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
    "error": "validation_error",
    "message": "Invalid input data",
    "details": {
        "field": ["error message"]
    }
}
```

### 401 Unauthorized
```json
{
    "error": "unauthorized",
    "message": "Invalid or expired token"
}
```

### 404 Not Found
```json
{
    "error": "not_found",
    "message": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
    "error": "internal_server_error",
    "message": "An unexpected error occurred"
}
```

## Rate Limiting

The API implements rate limiting to prevent abuse:
- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated users

Rate limit headers are included in all responses:
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1583850000
```
