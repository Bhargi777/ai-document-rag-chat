from fastapi.testclient import TestClient
from app.main import app
from io import BytesIO
from pypdf import PdfWriter

client = TestClient(app)

def _minimal_pdf_bytes() -> bytes:
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    buffer = BytesIO()
    writer.write(buffer)
    return buffer.getvalue()

def test_upload_pdf_rejects_non_pdf():
    response = client.post('/api/v1/documents/upload', files={'file': ('test.txt', b'hello', 'text/plain')})
    assert response.status_code == 400

def test_upload_pdf_accepts_pdf():
    response = client.post('/api/v1/documents/upload', files={'file': ('test.pdf', _minimal_pdf_bytes(), 'application/pdf')})
    assert response.status_code == 200
    assert response.json()['title'] == 'test.pdf'
