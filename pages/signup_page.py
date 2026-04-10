from playwright.sync_api import Page, Locator


class SignupPage:

    URL = "https://automationexercise.com/signup"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        self.page.goto("https://automationexercise.com/signup")

    # def name_signup_input(self) -> Locator:
    #     return self.page.get_by_test_id("signup-name")

    # def email_signup_input(self) -> Locator:
    #     return self.page.get_by_test_id("signup-email")

    # def signup_button(self) -> Locator:
    #     return self.page.get_by_role("button", name="Signup")

    # sign up form locators

    def title_mr(self) -> Locator:
        return self.page.get_by_label("Mr.")

    def title_mrs(self) -> Locator:
        return self.page.get_by_label("Mrs.")

    def form_header(self) -> Locator:
        return self.page.get_by_role("heading", name="Enter Account Information")

    def password_input(self) -> Locator:
        return self.page.get_by_test_id("password")

    def day_dropdown(self) -> Locator:
        return self.page.locator("select#days")

    def month_dropdown(self) -> Locator:
        return self.page.locator("select#months")

    def year_dropdown(self) -> Locator:
        return self.page.locator("select#years")

    def first_name(self) -> Locator:
        return self.page.get_by_role("textbox", name="First name")

    def last_name(self) -> Locator:
        return self.page.get_by_role("textbox", name="Last name")

    def address_1(self) -> Locator:
        return self.page.get_by_test_id("address")

    def country_dropdown(self) -> Locator:
        return self.page.locator("select#country")

    def state(self) -> Locator:
        return self.page.get_by_role("textbox", name="State")

    def city(self) -> Locator:
        return self.page.get_by_test_id("city")

    def zipcode(self) -> Locator:
        return self.page.get_by_test_id("zipcode")

    def mobile_number(self) -> Locator:
        return self.page.get_by_role("textbox", name="Mobile Number")

    def create_account_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Create Account")

    def fill_in_dob(self, day: str, month: str, year: str) -> None:
        self.day_dropdown().select_option(label=day)
        self.month_dropdown().select_option(label=month)
        self.year_dropdown().select_option(label=year)

    def fill_in_first_and_last_name(self, f_name: str, l_name: str) -> None:
        self.first_name().fill(f_name)
        self.last_name().fill(l_name)

    def fill_out_address(self, street: str, country: str, state: str, city: str, zipcode: str, mobile: str) -> None:
        self.address_1().fill(street)
        self.country_dropdown().select_option(label=country)
        self.state().fill(state)
        self.city().fill(city)
        self.zipcode().fill(zipcode)
        self.mobile_number().fill(mobile)
