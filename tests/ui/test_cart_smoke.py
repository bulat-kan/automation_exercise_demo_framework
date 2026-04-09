from playwright.sync_api import expect, Page
from pages.products_page import ProductsPage


def test_cart_page_opens(page: Page):
    page.goto("https://automationexercise.com/view_cart")
    expect(page).to_have_title("Automation Exercise - Checkout")
    expect(page.locator("#cart_items li.active")).to_be_visible()
    expect(page.get_by_text(
        "Cart is empty! Click here to buy products.")).to_be_visible()


def test_added_product_in_cart(page: Page):
    product_page = ProductsPage(page)
    product_page.open()
    product_name = "Cotton Silk Hand Block Print Saree"
    add_searched_product_and_open_cart(product_name, product_page)

    expect(page.locator("#cart_items li.active")).to_be_visible()
    expect(page.locator("td h4 a")).to_contain_text(product_name)
    expect(page.locator(".cart_quantity")).to_contain_text("1")


def test_remove_product_in_cart(page: Page):
    product_name = "Cotton Silk Hand Block Print Saree"
    product_page = ProductsPage(page)
    product_page.open()

    add_searched_product_and_open_cart(product_name, product_page)
    expect(page.locator(".cart_quantity")).to_contain_text("1")

    page.locator("td a.cart_quantity_delete").click()
    expect(page.get_by_text(
        "Cart is empty! Click here to buy products.")).to_be_visible()


def add_searched_product_and_open_cart(product_name: str, product_page: ProductsPage):
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
