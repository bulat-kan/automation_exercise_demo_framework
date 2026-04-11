from playwright.sync_api import expect, Page
from pages.products_page import ProductsPage
from utils.helpers import dismiss_google_vignette_if_present


def test_view_product_takes_to_product_details(page: Page):
    products_page = ProductsPage(page)
    products_page.open()

    first_product = products_page.products_list().nth(1)
    product_name = first_product.locator("p").first.inner_text().strip()
    product_price = first_product.locator("h2").first.inner_text().strip()
    page.pause()
    first_product.get_by_role("link", name="View Product").click()
    dismiss_google_vignette_if_present(page)

    assert "product_details/" in page.url

    product_name_on_product_details = page.locator(
        ".product-information h2").inner_text().strip()
    assert product_name == product_name_on_product_details

    product_price_on_product_details = page.locator(
        ".product-information span span").inner_text().strip()
    assert product_price == product_price_on_product_details


def test_product_details_page_components(page: Page):
    ...
