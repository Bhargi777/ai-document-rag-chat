const apiBaseUrl = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

export async function fetchHealth() {
  const res = await fetch(`${apiBaseUrl}/health`, { cache: 'no-store' });
  return res.json();
}

export async function uploadDocument(file: File) {
  const data = new FormData();
  data.append('file', file);
  const res = await fetch(`${apiBaseUrl}/api/v1/documents/upload`, { method: 'POST', body: data });
  return res.json();
}
