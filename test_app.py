from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "CI/CD Demo API V1 is running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_add():
    response = client.get("/add?a=2&b=3")

    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json()["version"] == "2.0"