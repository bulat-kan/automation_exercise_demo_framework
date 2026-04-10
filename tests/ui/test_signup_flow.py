from playwright.sync_api import expect, Page
from uuid import uuid4
from faker import Faker
from pages.signup_page import SignupPage
from pages.login_page import LoginPage


def test_new_user_can_signup(page: Page):

    login_page = LoginPage(page)
    login_page.open()

    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()

    fake = Faker()
    email = f"test_{uuid4().hex[:8]}@mail.com"
    first_name = fake.first_name()

    last_name = fake.last_name()
    name = f"{first_name} {last_name}"
    password = "Password@1"

    signup_page = login_page.initial_signup(name, email)

    expect(signup_page.form_header()).to_be_visible()

    signup_page.title_mr().check()
    signup_page.password_input().fill(password)

    # DOB
    signup_page.fill_in_dob("1", "April", "2002")
    signup_page.fill_in_first_and_last_name(first_name, last_name)

    # address data
    address = fake.street_address()
    mobile = fake.numerify("##########")

    signup_page.fill_out_address(street=address, country="United States",
                                 state="Florida", city="Miami", zipcode="31234", mobile=mobile)

    signup_page.create_account_btn().click()

    expect(page).to_have_url("https://automationexercise.com/account_created")
    expect(page.get_by_role("heading", name="Account Created!")).to_be_visible()

    page.get_by_role("link", name="Continue").click()
    expect(page).to_have_url("https://automationexercise.com/")
    expect(page.get_by_role("link", name="Logout")).to_be_visible()


def test_existing_user_cannot_signup(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()

    existing_user = "The Witcher"
    existing_email = "thewitcher@mail.com"
    login_page.initial_signup(existing_user, existing_email)

    expect(page.get_by_text("Email Address already exist!")).to_be_visible()
    expect(page).to_have_url("https://automationexercise.com/signup")


def test_new_user_cant_signup_without_filling_out_required_fields(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()

    fake = Faker()
    email = f"test_{uuid4().hex[:8]}@mail.com"
    first_name = fake.first_name()

    last_name = fake.last_name()
    name = f"{first_name} {last_name}"
    signup_page = login_page.initial_signup(name, email)

    expect(page).to_have_url("https://automationexercise.com/signup")
    expect(page.get_by_role(
        "heading", name="Enter Account Information")).to_be_visible()

    signup_page.title_mr().check()
    expect(page.get_by_label("Mr.")).to_be_checked()

    signup_page.fill_in_first_and_last_name(first_name, last_name)

    field = page.get_by_test_id("password")
    page.get_by_role("button", name="Create Account").click()

    assert "signup" in page.url
    assert field.evaluate("el => !el.checkValidity()")
    assert "fill out this field" in field.evaluate(
        "el => el.validationMessage").lower()
