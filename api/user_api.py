import requests
from requests import Response
from config.settings import API_BASE_URL


def delete_user(email: str, password: str) -> Response:
    return requests.delete(f"{API_BASE_URL}/deleteAccount", data={"email": email, "password": password})


def create_user(payload: dict) -> Response:
    return requests.post(f"{API_BASE_URL}/createAccount", data=payload)


def verify_login(email: str, password: str) -> Response:
    return requests.post(f"{API_BASE_URL}/verifyLogin", data={"email": email, "password": password})


def get_user_details_by_email(email: str) -> Response:
    return requests.get(f"{API_BASE_URL}/getUserDetailByEmail", params={"email": email})
