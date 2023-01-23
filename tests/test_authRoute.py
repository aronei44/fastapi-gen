from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/api/auth/register",
        json={"email": "test@example.com", "password": "iniPasswordd12334", "name":"testing coy"},
    )
    assert response.status_code == 201
    data = response.json()
    assert "token" in data


    response = client.post(
        "/api/auth/login",
        json={"email": "test@example.com", "password": "iniPasswordd12334"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

    response = client.get(
        "/api/auth/me",
        headers={"Authorization":f"Bearer {data['token']}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data['email'] == "test@example.com"
