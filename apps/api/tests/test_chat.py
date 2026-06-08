from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_query_requires_text():
    response = client.post('/api/v1/chat/query', json={'session_id': '1', 'query': ''})
    assert response.status_code == 400
