from playwright.sync_api import expect, Page
from pages.products_page import ProductsPage


def add_searched_product_and_open_cart(product_name: str, product_page: ProductsPage) -> None:
    page = product_page.page
    product_page.search_for_product(product_name)

    first_result = product_page.products_list().nth(0)
    first_result.hover()
    first_result.locator(".overlay-content a.add-to-cart").click()

    modal = page.locator(".modal-content")
    expect(modal).to_be_visible()
    expect(modal.get_by_role("heading", name="Added!")).to_be_visible()
    expect(modal.get_by_role("link", name="View Cart")).to_be_visible()
    modal.get_by_role("link", name="View Cart").click()

    expect(page.locator("td h4 a")).to_contain_text(product_name)


def clean_cart_if_not_empty(page: Page) -> None:
    page.goto("https://automationexercise.com/view_cart")

    empty_message = page.get_by_text(
        "Cart is empty! Click here to buy products.")
    delete_buttons = page.locator(".cart_quantity_delete")

    while delete_buttons.count() > 0:
        current_count = delete_buttons.count()
        delete_buttons.first.click()
        expect(delete_buttons).to_have_count(current_count - 1)
        delete_buttons = page.locator(".cart_quantity_delete")

    expect(empty_message).to_be_visible()
