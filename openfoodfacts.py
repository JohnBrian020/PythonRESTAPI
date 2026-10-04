import requests

BASE_URL = "https://world.openfoodfacts.org"


def find_product(barcode):
    """Find a product using its barcode."""

    url = f"{BASE_URL}/api/v2/product/{barcode}.json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("status") != 1:
            return None

        product = data.get("product", {})

        return {
            "barcode": barcode,
            "product_name": product.get("product_name", "Unknown"),
            "brands": product.get("brands", "Unknown"),
            "ingredients_text": product.get("ingredients_text", ""),
            "quantity": product.get("quantity", ""),
            "image_url": product.get("image_url", "")
        }

    except requests.RequestException:
        return None


def search_product(name):
    """Search for a product using its name."""

    url = f"{BASE_URL}/cgi/search.pl"

    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": 5
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        products = []

        for product in data.get("products", []):
            products.append({
                "barcode": product.get("code", ""),
                "product_name": product.get("product_name", "Unknown"),
                "brands": product.get("brands", "Unknown"),
                "ingredients_text": product.get("ingredients_text", ""),
                "quantity": product.get("quantity", ""),
                "image_url": product.get("image_url", "")
            })

        return products

    except requests.RequestException:
        return []