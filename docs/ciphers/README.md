# Ciphers App Architecture

Summary of the architecture and reasoning behind the `ciphers` app.

## Main Idea

Use one Django app with separate modules per cipher method:
- Separate model
- Separate serializer
- Separate viewset

This keeps everything isolated and easy to extend.

## Why This Structure

- Different ciphers need different fields.
  - Caesar: `key`
  - Affine: `a`, `b`
  - Columnar: `key`
  - OTP: `key`
- Different ciphers need different validation and microservice calls.
- Dedicated endpoints are safer than dynamic switching from a frontend string.

## Shared Base Components

- `BaseCipher` (abstract model): common logging fields (`created_at`, `created_by`, `input_text`, `output_text`, `operation`).
- `BaseCipherSerializer`: shared create behavior (sets `created_by` from request user).
- `BaseViewSet`: shared request flow (validate -> process -> save -> respond).