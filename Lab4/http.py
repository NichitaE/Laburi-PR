import requests
from requests.exceptions import SSLError

class OnlineStoreClient:
    def init(self, base_url):
        self.base_url = base_url

    def list_categories(self):
        url = f"{self.base_url}/api/Category/categories"
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
            return response.json()
        except SSLError as e:
            print("SSL Error:", e)
            return None
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            return None

    def create_category(self, title):
        url = f"{self.base_url}/api/Category/categories"
        data = {"title": title}
        try:
            response = requests.post(url, json=data, verify=False)
            response.raise_for_status()
            return response.json()
        except SSLError as e:
            print("SSL Error:", e)
            return None
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            return None

    def get_category_details(self, category_id):
        url = f"{self.base_url}/api/Category/categories/{category_id}"
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
            return response.json()
        except SSLError as e:
            print("SSL Error:", e)
            return None
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            return None

    def delete_category(self, category_id):
        url = f"{self.base_url}/api/Category/categories/{category_id}"
        try:
            response = requests.delete(url, verify=False)
            response.raise_for_status()
            return response.status_code == 204
        except SSLError as e:
            print("SSL Error:", e)
            return False
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            return False

    def list_products_in_category(self, category_id):
        url = f"{self.base_url}/api/Category/categories/{category_id}/products"
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
            return response.json()
        except SSLError as e:
            print("SSL Error:", e)
            return None
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            return None

    def create_product_in_category(self, category_id, product_name):
        url = f"{self.base_url}/api/Category/categories/{category_id}/products"
        data = {"title": product_name}
        try:
            response = requests.post(url, json=data, verify=False)
            response.raise_for_status()
            return response.json()
        except SSLError as e:
            print("SSL Error:", e)
            return None
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            return None

    def search_categories(self, category_name):
        url = f"{self.base_url}/api/Category/categories/search"
        params = {"categoryName": category_name}
        try:
            response = requests.get(url, params=params, verify=False)
            response.raise_for_status()
            return response.json()
        except SSLError as e:
            print("SSL Error:", e)
            return None
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            return None
          def update_category(self, category_id, new_title):
        url = f"{self.base_url}/api/Category/{category_id}"
        data = {"title": new_title}
        try:
            response = requests.put(url, json=data, verify=False)
            response.raise_for_status()
            return response.status_code == 204
        except SSLError as e:
            print("SSL Error:", e)
            return False
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            return False

def print_menu():
    print("1. List Categories")
    print("2. Create Category")
    print("3. Get Category Details")
    print("4. Delete Category")
    print("5. List Products in Category")
    print("6. Create Product in Category")
    print("7. Search Categories")
    print("8. Update Category")
    print("q. Quit")

def handle_list_categories(client):
    categories = client.list_categories()
    if categories is not None:
        print("Categories:", categories)

def handle_create_category(client):
    title = input("Enter category title: ")
    new_category = client.create_category(title)
    if new_category is not None:
        print("New category created:", new_category)

def handle_get_category_details(client):
    category_id = input("Enter category ID: ")
    category_details = client.get_category_details(category_id)
    if category_details is not None:
        print(f"Category details for ID {category_id}:", category_details)

def handle_delete_category(client):
    category_id = input("Enter category ID to delete: ")
    if client.delete_category(category_id):
        print(f"Category with ID {category_id} deleted successfully")
    else:
        print(f"Failed to delete category with ID {category_id}")

def handle_list_products_in_category(client):
    category_id = input("Enter category ID: ")
    products = client.list_products_in_category(category_id)
    if products is not None:
        print(f"Products in category {category_id}:", products)

def handle_create_product_in_category(client):
    category_id = input("Enter category ID: ")
    product_name = str(input("Enter product name: "))
    new_product = client.create_product_in_category(category_id, product_name)
    if new_product is not None:
        print("New product created:", new_product)

def handle_search_categories(client, category_name):
    categories = client.search_categories(category_name)
    if categories is not None:
        print("Searched categories:", categories)

def handle_update_category(client):
    category_id = input("Enter category ID to update: ")
    new_title = input("Enter new title: ")
    if client.update_category(category_id, new_title):
        print(f"Category with ID {category_id} updated successfully")
    else:
        print(f"Failed to update category with ID {category_id}")


menu_actions = {
    '1': handle_list_categories,
    '2': handle_create_category,
    '3': handle_get_category_details,
    '4': handle_delete_category,
    '5': handle_list_products_in_category,
    '6': handle_create_product_in_category,
    '7': lambda client: handle_search_categories(client, input("Enter category name to search: ")),
    '8': handle_update_category,
}

if name == "main":
    base_url = "https://localhost:44370" 
    client = OnlineStoreClient(base_url)

    while True:
        print("\nOnline Store API Menu")
        print_menu()
        choice = input("Enter your choice: ")

        if choice.lower() == 'q':
            print("Exiting program...")
            break

        action = menu_actions.get(choice)
        if action:
            action(client)
        else:
            print("Invalid choice. Please try again.")
