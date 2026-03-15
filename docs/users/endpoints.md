# Users API Endpoints

**Base URL:** `http://localhost:8805/api/auth/`

---

### Register

**POST** `register/`

Request body:
```json
{ 
  "email": "test@test.com",
  "password": "Testtest.1",
  "password2": "Testtest.1"
}
```

Success response (`201 Created`):
```json
{
  "id": 1,
  "email": "test@test.com",
  "date_joined": "2026-03-15T08:47:31.540511Z",
  "is_staff": false
}
```

Validation error examples (`400 Bad Request`):
```json
{
  "password": [
    "This password is too common."
  ]
}
```

```json
{
  "password": "Passwords do not match."
}
```

---

### Login

**POST** `login/`

Request body:
```json
{
  "email": "test@test.com",
  "password": "Testtest.1"
}
```

Success response (`200 OK`):
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

Invalid credentials (`401 Unauthorized`):
```json
{
  "detail": "No active account found with the given credentials"
}
```

---

### Refresh Token

**POST** `token/refresh/`

Request body:
```json
{
  "refresh": "<your_refresh_token>"
}
```

Success response (`200 OK`):
```json
{
  "access": "<new_access_token>"
}
```

Invalid/expired token (`401 Unauthorized`):
```json
{
  "detail": "Token is invalid or expired",
  "code": "token_not_valid"
}
```

---

### Logout

**POST** `logout/`

Header: `Authorization: Bearer <access_token>`

Request body:
```json
{
  "refresh": "<your_refresh_token>"
}
```

Success response (`200 OK`):
```json
{
  "detail": "Successfully logged out."
}
```

Missing/invalid access token (`401 Unauthorized`):
```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

### Get Current User

**GET** `me/`

Header: `Authorization: Bearer <access_token>`

Success response (`200 OK`):
```json
{
  "id": 1,
  "email": "test@test.com",
  "date_joined": "2026-03-15T12:00:00Z",
  "is_staff": false
}
```

Missing/invalid access token (`401 Unauthorized`):
```json
{
  "detail": "Authentication credentials were not provided."
}
```
