from playwright.sync_api import Page, Locator


class ProductDetailsPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, page_num: str) -> None:
        self.page.goto(
            f"https://automationexercise.com/product_details/{page_num}")

    def product_image(self) -> Locator:
        return self.page.locator("div.view-product img")

    def product_name_header(self) -> Locator:
        return self.page.locator(
            ".product-information h2")

    def product_price(self) -> Locator:
        return self.page.locator(
            ".product-information span span")

    def name_review_input(self) -> Locator:
        return self.page.get_by_placeholder("Your Name")

    def email_review_input(self) -> Locator:
        return self.page.get_by_placeholder("Email Address")

    def review_input(self) -> Locator:
        return self.page.get_by_placeholder("Add Review Here!")

    def add_to_cart_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Add to cart")

    def submit_review_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Submit")

#   Confirmation Modal Header
    def modal_added_header(self) -> Locator:
        return self.page.locator("div.modal-header h4")

    def modal_added_body_message(self) -> Locator:
        return self.page.locator("div.modal-content p.text-center").nth(0)

    def modal_added_body_view_cart_link(self) -> Locator:
        return self.page.locator("div.modal-body").get_by_role("link",
                                                               name="View Cart")

    def modal_added_continue_shopping_btn(self) -> Locator:
        return self.page.locator(".modal-footer button")

    def submit_review(self, name: str, email: str, review: str) -> None:
        self.email_review_input().fill(email)
        self.name_review_input().fill(name)
        self.review_input().fill(review)
        self.submit_review_btn().click()
