# Architecture Diagrams

The core system architecture consists of:

- Frontend: Next.js dashboard and chat UI.
- Backend: FastAPI service with LangChain, OpenAI, and vector search.
- Data stores: PostgreSQL for metadata, Pinecone/FAISS for embeddings.
- Deployments: Vercel frontend, Dockerized backend.

Diagram placeholders:

- `docs/architecture/diagrams/system.png`
- `docs/architecture/diagrams/flow.png`
