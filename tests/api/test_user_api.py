import requests
from uuid import uuid4
from faker import Faker
from api.user_api import create_user, delete_user, verify_login, get_user_details_by_email

BASE_URL = "https://automationexercise.com/api"


def test_create_user():
    payload = new_user_payload()

    response = create_user(payload)
    assert response.status_code == 200
    data = response.json()
    assert data["responseCode"] == 201
    assert data["message"] == "User created!"


def test_verify_login_with_created_user():
    payload = new_user_payload()
    email = payload["email"]
    password = payload["password"]
    response = create_user(payload)
    data = response.json()
    assert data["message"] == "User created!"

    verify_user_response = verify_login(email, password)
    assert verify_user_response.status_code == 200
    verify_response_data = verify_user_response.json()

    assert verify_response_data["responseCode"] == 200
    assert verify_response_data["message"] == "User exists!"


def test_get_user_detail_by_email():
    payload = new_user_payload()
    email = payload["email"]
    create_response = create_user(payload)
    create_data = create_response.json()
    assert create_response.status_code == 200
    assert create_data["responseCode"] == 201
    assert create_data["message"] == "User created!"

    # get user details by email
    response = get_user_details_by_email(email)
    data = response.json()
    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["user"]["email"] == email


def test_delete_user():
    payload = new_user_payload()
    email = payload["email"]
    password = payload["password"]

    # create user
    create_response = create_user(payload)
    created_data = create_response.json()
    assert created_data["responseCode"] == 201
    assert created_data["message"] == "User created!"

    # delete user
    delete_response = delete_user(email, password)
    data = delete_response.json()
    assert delete_response.status_code == 200
    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"


def test_deleted_user_cannot_login():
    payload = new_user_payload()
    email = payload["email"]
    password = payload["password"]

    # create user
    create_response = create_user(payload)
    created_data = create_response.json()
    assert created_data["responseCode"] == 201
    assert created_data["message"] == "User created!"

    # delete user
    delete_payload = {
        "email": email,
        "password": password
    }
    delete_response = delete_user(email, password)
    assert delete_response.status_code == 200
    data = delete_response.json()
    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"

    # attemp to login
    login_response = verify_login(email, password)
    login_response_data = login_response.json()
    assert login_response.status_code == 200
    assert login_response_data["responseCode"] == 404
    assert login_response_data["message"] == "User not found!"


def test_verify_login_without_email_parameter():
    payload = {
        "password": "Pass123"
    }
    response = requests.post(f"{BASE_URL}/verifyLogin", data=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["responseCode"] == 400
    assert data["message"] == "Bad request, email or password parameter is missing in POST request."


def test_verify_login_with_invalid_credentials():
    email = "123test@mail.com"
    password = "Password123"
    response = verify_login(email, password)
    assert response.status_code == 200
    data = response.json()
    assert data["responseCode"] == 404
    assert data["message"] == "User not found!"


def new_user_payload() -> dict:
    fake = Faker()
    f_name = fake.first_name()
    l_name = fake.last_name()
    name = f"{f_name} {l_name}"
    email = f"test_{uuid4().hex[:8]}@mail.com"
    password = "Password@1"
    title = "Mr"
    payload = {
        "name": name,
        "email": email,
        "password": password,
        "title": title,
        "birth_date": 1,
        "birth_month": 1,
        "birth_year": 2001,
        "firstname": f_name,
        "lastname": l_name,
        "company": "",
        "address1": "123 Main st",
        "address2": "",
        "country": "United States",
        "zipcode": 31321,
        "state": "Florida",
        "city": "Miami",
        "mobile_number": "1234567890"
    }
    return payload
