from playwright.sync_api import Page, Locator


class ProductsPage:
    URL = "https://automationexercise.com/products"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        self.page.goto(self.URL)

    def category_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Category")

    def brands_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Brands")

    def all_products_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="All Products")

    def products_list(self) -> Locator:
        return self.page.locator(".features_items .col-sm-4")

    def products_search_input(self) -> Locator:
        return self.page.get_by_placeholder("Search Product")

    def search_button(self) -> Locator:
        return self.page.locator("#submit_search")

    def search_for_product(self, product_name: str):
        self.products_search_input().fill(product_name)
        self.search_button().click()
