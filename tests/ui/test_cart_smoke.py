from playwright.sync_api import expect, Page
from pages.products_page import ProductsPage
from utils.cart_helpers import add_searched_product_and_open_cart


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
