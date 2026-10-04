
import pytest
from app import app, inventory


@pytest.fixture
def client():
    original_inventory = [item.copy() for item in inventory]

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

    inventory.clear()
    inventory.extend(original_inventory)


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_single_item(client):
    response = client.get("/inventory/1")

    assert response.status_code == 200
    assert response.json["name"] == "Organic Almond Milk"


def test_add_item(client):
    response = client.post("/inventory", json={
        "name": "Yoghurt",
        "price": 150,
        "stock": 10
    })

    assert response.status_code == 201
    assert response.json["name"] == "Yoghurt"


def test_update_item(client):
    response = client.patch("/inventory/1", json={
        "price": 500,
        "stock": 15
    })

    assert response.status_code == 200
    assert response.json["price"] == 500
    assert response.json["stock"] == 15


def test_delete_item(client):
    response = client.delete("/inventory/1")

    assert response.status_code == 200


def test_item_not_found(client):
    response = client.get("/inventory/999")

    assert response.status_code == 404


def test_missing_required_fields(client):
    response = client.post("/inventory", json={
        "name": "Bread"
    })

    assert response.status_code == 400