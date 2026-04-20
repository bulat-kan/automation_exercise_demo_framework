import requests
from requests import Response


BASE_URL = "https://automationexercise.com/api"


def delete_user(email: str, password: str) -> Response:
    return requests.delete(f"{BASE_URL}/deleteAccount", data={"email": email, "password": password})


def create_user(payload) -> Response:
    return requests.post(f"{BASE_URL}/createAccount", data=payload)


def verify_login(email: str, password: str) -> Response:
    return requests.post(f"{BASE_URL}/verifyLogin", data={"email": email, "password": password})


def get_user_details_by_email(email: str) -> Response:
    return requests.get(f"{BASE_URL}/getUserDetailByEmail", params={"email": email})
