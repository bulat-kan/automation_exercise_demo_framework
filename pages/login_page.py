from playwright.sync_api import Page, Locator


class LoginPage:

    URL = "https://automationexercise.com/login"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def login_email_input(self) -> Locator:
        return self.page.get_by_test_id("login-email")

    def login_password_input(self) -> Locator:
        return self.page.get_by_test_id("login-password")

    def login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Login")

    def name_signup_input(self) -> Locator:
        return self.page.get_by_placeholder("Name")

    def email_signup_input(self) -> Locator:
        return self.page.get_by_test_id("signup-email")

    def signup_button(self) -> Locator:
        return self.page.get_by_role("button", name="Signup")

    def login_error_alert(self) -> Locator:
        return self.page.get_by_text("Your email or password is incorrect!")

    def logout_link(self) -> Locator:
        return self.page.get_by_role("link", name="Logout")

    def logged_in_as_text(self) -> Locator:
        return self.page.get_by_text("Logged in as")

    def login(self, email: str, password: str) -> None:
        self.login_email_input().fill(email)
        self.login_password_input().fill(password)
        self.login_button().click()
