from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.cart_helpers import add_searched_product_and_open_cart, clean_cart_if_not_empty


def test_logged_in_user_can_add_product_to_cart(page: Page):
    login_page = LoginPage(page)
    email = "thewitcher@mail.com"
    password = "Password@1"
    login_page.open()
    login_page.login(email, password)
    expect(page).to_have_url("https://automationexercise.com/")
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    clean_cart_if_not_empty(page)

    product_page = ProductsPage(page)
    product_page.open()
    expect(page).to_have_url("https://automationexercise.com/products")

    product_name = "Blue Top"
    add_searched_product_and_open_cart(product_name, product_page)
    expect(page.locator(".cart_quantity")).to_contain_text("1")
