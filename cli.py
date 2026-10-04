
import requests

BASE_URL = "http://127.0.0.1:5555"


def show_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    print(response.json())


def view_item():
    item_id = input("Enter product ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")
    print(response.json())


def add_item():
    data = {
        "name": input("Product name: "),
        "brand": input("Brand: "),
        "price": float(input("Price: ")),
        "stock": int(input("Stock: "))
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=data
    )

    print(response.status_code, response.json())


def update_item():
    item_id = input("Enter product ID: ")

    data = {
        "price": float(input("New price: ")),
        "stock": int(input("New stock: "))
    }

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=data
    )

    print(response.status_code, response.json())


def delete_item():
    item_id = input("Enter product ID: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    print(response.status_code, response.json())


def search_external():
    name = input("Enter product name: ")

    response = requests.get(
        f"{BASE_URL}/external/search",
        params={"name": name}
    )

    print(response.json())


def import_external():
    barcode = input("Enter product barcode: ")

    response = requests.post(
        f"{BASE_URL}/external/import/{barcode}"
    )

    print(response.status_code, response.json())


def main():
    while True:
        print("\n===== INVENTORY MANAGEMENT =====")
        print("1. View all products")
        print("2. View one product")
        print("3. Add product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Search OpenFoodFacts")
        print("7. Import external product")
        print("0. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                show_inventory()
            elif choice == "2":
                view_item()
            elif choice == "3":
                add_item()
            elif choice == "4":
                update_item()
            elif choice == "5":
                delete_item()
            elif choice == "6":
                search_external()
            elif choice == "7":
                import_external()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

        except (requests.RequestException, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()