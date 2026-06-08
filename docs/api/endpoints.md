# API Endpoints

## Authentication

- `POST /api/v1/auth/register` — register a new user
- `POST /api/v1/auth/login` — login and receive a Bearer token

## User

- `GET /api/v1/users/me` — retrieve the authenticated user's profile

## Documents

- `POST /api/v1/documents/upload` — upload a PDF document

## Chat

- `POST /api/v1/chat/query` — execute a semantic query against uploaded documents

## History

- `GET /api/v1/history/sessions/{session_id}/history` — retrieve chat message history for a session
