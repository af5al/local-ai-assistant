from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    """Verify health endpoint returns 200 and healthy status"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_list_models(monkeypatch):
    """Verify /models returns a list (isolated with mocking)"""
    monkeypatch.setattr("src.main.provider.get_models", lambda: ["mock-model-1", "mock-model-2"])
    
    response = client.get("/models")
    assert response.status_code == 200
    assert response.json()["models"] == ["mock-model-1", "mock-model-2"]

def test_chat_validation_error():
    """Verify Pydantic rejects invalid requests with HTTP 422"""
    # Sending empty body with missing required fields
    response = client.post("/chat", json={})
    assert response.status_code == 422
