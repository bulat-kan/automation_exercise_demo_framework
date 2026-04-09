from playwright.sync_api import expect, Page
from pages.login_page import LoginPage


def test_logged_in_user_can_add_product_to_cart(page: Page):
    login_page = LoginPage(page)
    email = "thewitcher@mail.com"
    password = "Password@1"
    login_page.open()
    login_page.login(email, password)
    expect(page).to_have_url("https://automationexercise.com/")
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_url("https://automationexercise.com/products")
