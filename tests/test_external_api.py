
from unittest.mock import patch
from app import app


def test_external_barcode(client=None):
    with app.test_client() as client:
        with patch("app.find_product") as mock_product:

            mock_product.return_value = {
                "barcode": "12345",
                "product_name": "Almond Milk",
                "brands": "Silk",
                "ingredients_text": "Water, almonds"
            }

            response = client.get("/external/barcode/12345")

            assert response.status_code == 200
            assert response.json["product_name"] == "Almond Milk"


def test_external_product_not_found():
    with app.test_client() as client:
        with patch("app.find_product", return_value=None):

            response = client.get("/external/barcode/99999")

            assert response.status_code == 404