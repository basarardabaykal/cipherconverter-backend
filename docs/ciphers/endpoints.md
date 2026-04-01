# Ciphers API Endpoints

**Base URL:** `http://localhost:8805/api/ciphers/`

---

### Caesar Cipher

**POST** `caesar/`

Header: `Authorization: Bearer <access_token>`

Request body:
```json
{
  "input_text": "hello world",
  "key": 3,
  "operation": "encrypt"
}
```

Success response (`200 OK`):
```json
{
  "status_message": "Success",
  "message": "Successfully processed cipher.",
  "content": {
    "input_text": "hello world",
    "key": 3,
    "operation": "encrypt",
    "output_text": "khoor zruog",
    "created_at": "2026-04-01T10:00:00Z",
    "created_by": 1
  }
}
```

Validation error example (`400 Bad Request`) - invalid key:
```json
{
  "key": [
    "Ensure this value is less than or equal to 26."
  ]
}
```

Validation error example (`400 Bad Request`) - invalid operation:
```json
{
  "operation": [
    "\"rotate\" is not a valid choice."
  ]
}
```

Unauthorized (`401 Unauthorized`):
```json
{
  "detail": "Authentication credentials were not provided."
}
```

Microservice unavailable (`503 Service Unavailable`):
```json
{
  "detail": "Cipher microservice unavailable (UNAVAILABLE)"
}
```
