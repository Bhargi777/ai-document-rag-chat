from fastapi.testclient import TestClient
from app.main import app
from io import BytesIO

client = TestClient(app)

def test_upload_pdf_rejects_non_pdf():
    response = client.post('/api/v1/documents/upload', files={'file': ('test.txt', b'hello', 'text/plain')})
    assert response.status_code == 400

# The endpoint currently saves files locally and returns a file path. Use a PDF bytes stub for integration.
def test_upload_pdf_accepts_pdf():
    pdf_bytes = b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n'
    response = client.post('/api/v1/documents/upload', files={'file': ('test.pdf', pdf_bytes, 'application/pdf')})
    assert response.status_code == 200
    assert response.json()['title'] == 'test.pdf'
