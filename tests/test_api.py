from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    """Verify health endpoint returns 200 and healthy status"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_list_models():
    """Verify /models returns a list"""
    response = client.get("/models")
    assert response.status_code == 200
    assert "models" in response.json()
    assert isinstance(response.json()["models"], list)

def test_chat_validation_error():
    """Verify Pydantic rejects invalid requests with HTTP 422"""
    # Sending empty body with missing required fields
    response = client.post("/chat", json={})
    assert response.status_code == 422
