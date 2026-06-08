# System Overview

AI Document RAG Chat uses a monorepo architecture with separated frontend and backend applications.

- `apps/web` — Next.js frontend UI.
- `apps/api` — FastAPI backend with LangChain and vector search.
- `packages/ui` — shared React components.
- `packages/shared` — shared TypeScript utilities.

The backend uses OpenAI embeddings and Pinecone/FAISS for semantic search, plus PostgreSQL for user and metadata storage.
