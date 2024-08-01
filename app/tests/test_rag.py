# tests/test_rag.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rag_endpoint():
    response = client.post("/rag/", json={"prompt": "I feel stressed and anxious."})
    assert response.status_code == 200
    assert "response" in response.json()
