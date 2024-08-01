# tests/test_classification.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_classify_endpoint():
    response = client.post("/classification/", json={"text": "Sample text to classify"})
    assert response.status_code == 200
    assert "prediction" in response.json()
