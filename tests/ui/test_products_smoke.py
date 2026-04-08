from playwright.sync_api import expect, Page
from pages.products_page import ProductsPage


def test_products_page_loads(page: Page):
    prod_page = ProductsPage(page)
    prod_page.open()
    expect(page).to_have_title("Automation Exercise - All Products")
    expect(prod_page.all_products_heading()).to_be_visible()
    expect(prod_page.brands_heading()).to_be_visible()
    expect(prod_page.products_search_input()).to_be_visible()


def test_products_list_visible(page: Page):
    prod_page = ProductsPage(page)
    prod_page.open()
    products = prod_page.products_list()
    assert products.count() > 0


def test_products_search_works(page: Page):
    prod_page = ProductsPage(page)
    prod_page.open()
    prod_page.search_for_product("Peacock Blue Cotton")

    results = prod_page.products_list()
    expect(results.nth(0)).to_contain_text("Peacock Blue Cotton")


def test_products_search_finds_no_results_with_invalid_data(page: Page):
    prod_page = ProductsPage(page)
    prod_page.open()
    prod_page.search_for_product("asdasda")

    results = prod_page.products_list()
    assert results.count() == 0


def test_view_products_displays_product_details(page):
    prod_page = ProductsPage(page)
    prod_page.open()
    product_name = "Fancy Green Top"
    prod_page.search_for_product(product_name)
    search_results = prod_page.products_list()

    expect(search_results.nth(0)).to_contain_text(product_name)
    search_results.nth(0).page.get_by_role("link", name="View Product").click()

    assert "product_details" in page.url
