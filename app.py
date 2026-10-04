
from flask import Flask, jsonify, request
from openfoodfacts import find_product, search_product

app = Flask(__name__)

# Simulated inventory database
inventory = [
    {
        "id": 1,
        "name": "Organic Almond Milk",
        "brand": "Silk",
        "price": 450,
        "stock": 20,
        "barcode": "123456789",
        "ingredients": "Water, almonds"
    },
    {
        "id": 2,
        "name": "Fresh Milk",
        "brand": "Brookside",
        "price": 250,
        "stock": 30,
        "barcode": "987654321",
        "ingredients": "Milk"
    }
]


# GET all inventory
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


# GET one product
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next(
        (item for item in inventory if item["id"] == item_id),
        None
    )

    if item is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(item), 200


# POST new product
@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    required_fields = ["name", "price", "stock"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    try:
        price = float(data["price"])
        stock = int(data["stock"])

        if price < 0 or stock < 0:
            return jsonify({"error": "Price and stock cannot be negative"}), 400

    except (ValueError, TypeError):
        return jsonify({"error": "Invalid price or stock"}), 400

    new_item = {
        "id": max((item["id"] for item in inventory), default=0) + 1,
        "name": data["name"],
        "brand": data.get("brand", "Unknown"),
        "price": price,
        "stock": stock,
        "barcode": data.get("barcode", ""),
        "ingredients": data.get("ingredients", "")
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


# PATCH update product
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    item = next(
        (item for item in inventory if item["id"] == item_id),
        None
    )

    if item is None:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()

    if not isinstance(data, dict) or not data:
        return jsonify({"error": "Valid JSON data is required"}), 400

    for field in ["price", "stock"]:
        if field in data:
            try:
                value = float(data[field]) if field == "price" else int(data[field])

                if value < 0:
                    return jsonify({"error": f"{field} cannot be negative"}), 400

                item[field] = value

            except (ValueError, TypeError):
                return jsonify({"error": f"Invalid {field}"}), 400

    for field in ["name", "brand", "barcode", "ingredients"]:
        if field in data:
            item[field] = data[field]

    return jsonify(item), 200


# DELETE product
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = next(
        (item for item in inventory if item["id"] == item_id),
        None
    )

    if item is None:
        return jsonify({"error": "Product not found"}), 404

    inventory.remove(item)

    return jsonify({"message": "Product deleted successfully"}), 200


# Search OpenFoodFacts by barcode
@app.route("/external/barcode/<barcode>", methods=["GET"])
def external_barcode(barcode):
    product = find_product(barcode)

    if product is None:
        return jsonify({"error": "Product not found or API unavailable"}), 404

    return jsonify(product), 200


# Search OpenFoodFacts by name
@app.route("/external/search", methods=["GET"])
def external_search():
    name = request.args.get("name")

    if not name:
        return jsonify({"error": "Product name is required"}), 400

    products = search_product(name)

    return jsonify(products), 200


# Import external product into inventory
@app.route("/external/import/<barcode>", methods=["POST"])
def import_product(barcode):
    product = find_product(barcode)

    if product is None:
        return jsonify({"error": "External product not found"}), 404

    existing = next(
        (item for item in inventory if item["barcode"] == barcode),
        None
    )

    if existing:
        return jsonify({"error": "Product already exists"}), 409

    new_item = {
        "id": max((item["id"] for item in inventory), default=0) + 1,
        "name": product["product_name"],
        "brand": product["brands"],
        "price": 0,
        "stock": 0,
        "barcode": product["barcode"],
        "ingredients": product["ingredients_text"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


if __name__ == "__main__":
    app.run(debug=True, port=5555)