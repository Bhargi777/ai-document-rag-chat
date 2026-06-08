# Deployment

This project supports Docker-based backend deployment and Vercel frontend deployment.

- `infrastructure/docker`: backend container configuration
- `apps/web`: Next.js frontend deployable to Vercel
- `vercel.json`: deployment settings for the frontend

## Vercel

Set `NEXT_PUBLIC_API_URL` to your FastAPI backend URL in Vercel environment variables.

## Docker

Use `docker-compose` in `infrastructure/docker/docker-compose.yml` to run the backend locally.
