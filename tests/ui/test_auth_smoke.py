from playwright.sync_api import expect, Page
from pages.login_page import LoginPage


def test_login_page_sections_visible(page: Page):

    login_page = LoginPage(page)
    login_page.open()

    expect(login_page.login_email_input()).to_be_visible()
    expect(login_page.login_password_input()).to_be_visible()
    expect(login_page.login_button()).to_be_visible()


def test_signup_section_visible(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    expect(login_page.email_signup_input()).to_be_visible()
    expect(login_page.name_signup_input()).to_be_visible()
    expect(login_page.signup_button()).to_be_visible()


def test_login_fails_with_invalid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    invalid_email = "wrong@wrong.com"
    invalid_password = "Password1"

    login_page.login(invalid_email, invalid_password)
    expect(login_page.login_error_alert()).to_be_visible()


def test_login_successful(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    valid_email = "thewitcher@mail.com"
    valid_password = "Password@1"
    login_page.login(valid_email, valid_password)

    expect(login_page.logout_link()).to_be_visible()
    expect(login_page.logged_in_as_text()).to_be_visible()


def test_logout_successful(page: Page):
    login_page = LoginPage(page)
    valid_email = "thewitcher@mail.com"
    valid_password = "Password@1"
    login_page.open()
    login_page.login(valid_email, valid_password)
    login_page.logout_link().click()

    expect(page).to_have_url(login_page.URL)
