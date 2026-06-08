# Authentication API

## Register

`POST /api/v1/auth/register`

Request body:

```json
{
  "email": "user@example.com",
  "password": "secure-password"
}
```

Response includes a JWT bearer token.

## Login

`POST /api/v1/auth/login`

Use form encoded credentials with `username` and `password`.

Response returns access token and token type.
