# AI Document RAG Chat

A production-ready AI Document Search and PDF Chat SaaS built with Next.js, FastAPI, LangChain, Pinecone, and PostgreSQL.

## Overview

This repository contains a modern monorepo structure for a document retrieval and chat application.

- `apps/web` — Next.js frontend with TypeScript, TailwindCSS, and shadcn/ui.
- `apps/api` — FastAPI backend with LangChain, PostgreSQL, and vector search support.
- `packages/ui` — Shared UI components.
- `packages/shared` — Shared TypeScript utilities.
- `infrastructure` — Docker and deployment configuration.
- `docs` — Architecture, API, and deployment guides.

## Quick Start

1. Install dependencies for the frontend monorepo.
2. Configure environment variables for backend and vector stores.
3. Start the backend and frontend locally.

## Project Structure

- `apps/web` — Next.js frontend application.
- `apps/api` — FastAPI backend and service layer.
- `packages/ui` — Shared design system components.
- `packages/shared` — Utility modules and shared helpers.
- `infrastructure` — Docker and deployment orchestration.
- `docs` — Architecture, API, and deployment documentation.

## Contribution

Contributions are welcome via issues and pull requests. Please follow the templates in `.github/`.

## License

MIT License.
