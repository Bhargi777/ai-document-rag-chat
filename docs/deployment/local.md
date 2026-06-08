# Local Development

1. Install Node dependencies:

```bash
npm install
```

2. Start the frontend from the root:

```bash
npm --workspace apps/web run dev
```

3. Start the backend with Docker or directly if Python is configured:

```bash
cd infrastructure/docker && docker compose up --build
```
```
