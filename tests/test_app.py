
import pytest
from app.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"AWS EC2" in response.data


def test_info_endpoint(client):
    response = client.get("/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "Docker Web Application"
    assert data["platform"] == "AWS EC2"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
