from playwright.sync_api import Page, expect

from api.user_api import create_user, delete_user
from data.user_payloads import new_user_payload
from pages.login_page import LoginPage


def test_api_created_user_can_login_via_ui(page: Page):
    payload = new_user_payload()
    email = payload["email"]
    password = payload["password"]

    # create user
    response = create_user(payload)
    assert response.status_code == 200
    data = response.json()
    assert data["responseCode"] == 201
    assert data["message"] == "User created!"

    try:
        # UI login
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(email, password)
        expect(page).to_have_url("https://automationexercise.com/")
        expect(login_page.logout_link()).to_be_visible()

        login_page.logout_link().click()
        assert "/login" in page.url

    finally:
        delete_user(email, password)
