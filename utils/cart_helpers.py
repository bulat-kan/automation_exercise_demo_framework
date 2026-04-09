from playwright.sync_api import expect
from pages.products_page import ProductsPage


def add_searched_product_and_open_cart(product_name: str, product_page: ProductsPage) -> None:
    page = product_page.page
    product_page.search_for_product(product_name)
    search_results = product_page.products_list()
    search_results.nth(0).hover()
    search_results.nth(0).locator(".overlay-content a.add-to-cart").click()
    expect(page.locator("div.modal-content")).to_be_visible()
    expect(page.locator(".modal-content").get_by_role("heading",
           name="Added!")).to_be_visible()
    expect(page.locator(".modal-content").get_by_role("link",
           name="View Cart")).to_be_visible()
    page.locator(".modal-content").get_by_role("link",
                                               name="View Cart").click()
    expect(page.locator("td h4 a")).to_contain_text(product_name)
