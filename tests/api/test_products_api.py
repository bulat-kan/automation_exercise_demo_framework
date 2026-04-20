import requests
from faker import Faker
from uuid import uuid4

BASE_URL = "https://automationexercise.com"


# Expected response shape:
# {
#   "responseCode": 200,
#   "products": [...]
# }

def test_get_all_products():
    response = requests.get(f"{BASE_URL}/api/productsList")

    assert response.status_code == 200
    data = response.json()
    assert 'products' in data

    assert len(data["products"]) > 0


def test_post_to_all_products_list():
    payload = {"cellphone": "iphone 21"}
    response = requests.post(f"{BASE_URL}/api/productsList", payload)

    assert response.status_code == 200
    data = response.json()

    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."


def test_get_all_brands_list():
    response = requests.get(f"{BASE_URL}/api/brandsList")
    assert response.status_code == 200
    data = response.json()

    assert "brands" in data

    assert len(data["brands"]) > 0


def test_put_to_all_brands():
    payload = {"brand": "samsung"}
    response = requests.put(f"{BASE_URL}/api/brandsList", data=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["responseCode"] == 405
    assert data["message"] == 'This request method is not supported.'


def test_product_search():
    product_to_search_for = "Beautiful Peacock Blue Cotton Linen Saree"
    payload = {"search_product": product_to_search_for}
    response = requests.post(f"{BASE_URL}/api/searchProduct", data=payload)
    assert response.status_code == 200
    data = response.json()

    assert "products" in data
    assert len(data["products"]) > 0
    assert any(product_to_search_for in product["name"]
               for product in data["products"])


def test_product_search_without_product():
    payload = {}
    response = requests.post(f"{BASE_URL}/api/searchProduct", payload)
    data = response.json()

    assert response.status_code == 200

    assert data["responseCode"] == 400
    assert data["message"] == "Bad request, search_product parameter is missing in POST request."


def test_product_search_non_existing_product():
    payload = {"search_product": "iphone 25"}
    response = requests.post(f"{BASE_URL}/api/searchProduct", data=payload)
    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert len(data["products"]) == 0
