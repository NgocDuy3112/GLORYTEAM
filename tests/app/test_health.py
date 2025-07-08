from fastapi.testclient import TestClient
from app.beta import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json().get("status") == "ok"