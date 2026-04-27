from playwright.sync_api import expect, Page
from config.settings import BASE_URL


def test_homepage_loads(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Automation Exercise")


def test_homepage_main_navigation_visible(page: Page):
    page.goto(BASE_URL)
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="Products")).to_be_visible()
    expect(page.get_by_role("link", name="Cart")).to_be_visible()
    expect(page.get_by_role("link", name="Signup / Login")).to_be_visible()


def test_signup_login_page_opens(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("link", name="Signup / Login").click()

    expect(page).to_have_title("Automation Exercise - Signup / Login")
    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
