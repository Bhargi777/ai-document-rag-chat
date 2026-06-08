from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analytics_events_endpoint():
    response = client.get('/api/v1/analytics/events')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
