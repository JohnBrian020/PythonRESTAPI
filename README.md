# PythonRESTAPI
# Python REST API with Flask — Inventory Management System

## Project Description

The Inventory Management System is a Python-based REST API built with Flask. It allows employees to manage products in an e-commerce inventory through CRUD operations.

The application also integrates with the OpenFoodFacts API to retrieve product information using barcodes or product names.

A command-line interface (CLI) allows users to interact with the API directly from the terminal.

The project uses a Python list as a simulated database to store inventory items.

## Features

* View all inventory products.
* Retrieve a single product by ID.
* Add new products to inventory.
* Update product prices and stock levels.
* Delete products from inventory.
* Search products using the OpenFoodFacts API.
* Find products using barcodes.
* Import external product information into the inventory.
* CLI-based inventory management.
* Error handling for invalid inputs and missing products.
* Automated testing using pytest and unittest.mock.

## Technologies Used

* Python
* Flask
* Requests
* OpenFoodFacts API
* Pytest
* unittest.mock
* Git and GitHub
* Postman

## Project Structure

```text
inventory-management-system/
│
├── app.py
├── cli.py
├── openfoodfacts.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    ├── __init__.py
    ├── test_api.py
    ├── test_external_api.py
    └── test_cli.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/JohnBrian020/inventory-management-system.git
```

### 2. Navigate into the project directory

```bash
cd inventory-management-system
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

For Linux / Ubuntu / WSL:

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Flask Application

Start the Flask development server:

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5555
```

The application can be tested using a browser, Postman, or the CLI.

## Using the CLI

Open a second terminal, activate the virtual environment, and run:

```bash
python cli.py
```

The CLI provides the following menu:

```text
===== INVENTORY MANAGEMENT =====

1. View all products
2. View one product
3. Add product
4. Update product
5. Delete product
6. Search OpenFoodFacts
7. Import external product
0. Exit
```

Select an option and follow the prompts to manage inventory.

## API Endpoint Documentation

Base URL:

```text
http://127.0.0.1:5555
```

### Inventory Routes

| Method | Endpoint          | Description            | Status |
| ------ | ----------------- | ---------------------- | ------ |
| GET    | `/inventory`      | Retrieve all products  | 200    |
| GET    | `/inventory/<id>` | Retrieve one product   | 200    |
| POST   | `/inventory`      | Add a new product      | 201    |
| PATCH  | `/inventory/<id>` | Update product details | 200    |
| DELETE | `/inventory/<id>` | Delete a product       | 200    |

### External API Routes

| Method | Endpoint                      | Description                            |
| ------ | ----------------------------- | -------------------------------------- |
| GET    | `/external/barcode/<barcode>` | Find product by barcode                |
| GET    | `/external/search?name=milk`  | Search products by name                |
| POST   | `/external/import/<barcode>`  | Import external product into inventory |

### Example POST Request

Endpoint:

```text
POST /inventory
```

JSON body:

```json
{
  "name": "Organic Almond Milk",
  "brand": "Silk",
  "price": 450,
  "stock": 20
}
```

Successful response:

```json
{
  "id": 3,
  "name": "Organic Almond Milk",
  "brand": "Silk",
  "price": 450,
  "stock": 20,
  "barcode": "",
  "ingredients": ""
}
```

## OpenFoodFacts API Integration

The project uses the OpenFoodFacts API to retrieve real-world product information.

API Documentation:

https://openfoodfacts.github.io/openfoodfacts-server/api/

Product information may include:

* Product name
* Brand
* Barcode
* Ingredients
* Quantity
* Product image

The retrieved information can be imported into the local inventory using the external import endpoint.

Products imported from OpenFoodFacts receive a default price and stock of zero, which can be updated through the PATCH endpoint.

## Running Tests

The project uses pytest to validate API endpoints, CLI functionality, and external API interactions.

Run all tests:

```bash
pytest -v
```

The test suite covers:

* GET requests
* POST requests
* PATCH requests
* DELETE requests
* Invalid product IDs
* Missing required fields
* External API responses using mocks
* CLI HTTP interactions

Mocking is used to avoid depending on a live external API during automated tests.

## Data Storage and Limitations

This project uses an in-memory Python list to simulate a database.

### Advantages

* Simple to implement.
* No database installation required.
* Suitable for learning Flask CRUD operations.
* Easy to test.

### Limitations

* Inventory data is lost when the Flask server restarts.
* Data is not permanently stored.
* Not suitable for multiple users or production environments.
* Does not provide database-level concurrency or persistence.

A future version could use SQLite or PostgreSQL for permanent data storage.

## Future Improvements

* Integrate a permanent database.
* Add user authentication and administrator roles.
* Build a React-based frontend.
* Add product categories and low-stock alerts.
* Implement pagination and advanced search.
* Deploy the API to a cloud hosting platform.

## Author

John Brian Waweru

---