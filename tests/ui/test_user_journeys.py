from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.cart_helpers import add_searched_product_and_open_cart, clean_cart_if_not_empty
from faker import Faker
from pages.signup_page import SignupPage
from pages.product_details_page import ProductDetailsPage
from uuid import uuid4


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


def test_user_can_signup_login_logout(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    fake = Faker()
    f_name = fake.first_name()
    l_name = fake.last_name()
    full_name = f"{f_name} {l_name}"
    email = f"test_{uuid4().hex[:8]}@mail.com"
    password = "Password@1"
    signup_page: SignupPage = login_page.initial_signup(full_name, email)
    signup_page.title_mr().check()
    signup_page.fill_in_first_and_last_name(f_name, l_name)
    signup_page.password_input().fill(password)

    signup_page.fill_in_dob("1", "January", "2001")

    street = fake.street_address()
    signup_page.fill_out_address(
        street, "United States", "Florida", "Miami", "31443", "2345678901")
    signup_page.create_account_btn().click()
    expect(page.get_by_role("heading", name="Account Created!")).to_be_visible()

    page.get_by_role("link", name="Continue").click()
    expect(page).to_have_url("https://automationexercise.com/")
    expect(page.get_by_text(f"Logged in as {f_name} {l_name}")).to_be_visible()

    page.get_by_role("link", name="Logout").click()
    assert "login" in page.url
    expect(login_page.signup_form_heading()).to_be_visible()


# login -> product details -> add to cart -> cart verification
def test_user_is_able_to_login_add_product_from_product_details(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    valid_email = "thewitcher@mail.com"
    valid_password = "Password@1"
    login_page.login(valid_email, valid_password)

    expect(login_page.logout_link()).to_be_visible()
    clean_cart_if_not_empty(page)
    prod_details_page = ProductDetailsPage(page)
    prod_details_page.open(2)
    product_name = prod_details_page.product_name_header().inner_text().strip().lower()
    expect(prod_details_page.product_name_header()).to_be_visible()
    prod_details_page.add_to_cart_btn().click()
    expect(prod_details_page.modal_added_header()).to_be_visible()
    prod_details_page.modal_added_body_view_cart_link().click()
    expect(page).to_have_url("https://automationexercise.com/view_cart")
    product_name_in_cart = page.locator(
        ".cart_description a").inner_text().strip().lower()
    assert product_name == product_name_in_cart
