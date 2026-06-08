export async function fetchHealth() {
  const res = await fetch('/api/health');
  return res.json();
}

export async function uploadDocument(file: File) {
  const data = new FormData();
  data.append('file', file);
  const res = await fetch('/api/v1/documents/upload', { method: 'POST', body: data });
  return res.json();
}
