from playwright.sync_api import expect, Page


def test_products_page_loads(page: Page):
    page.goto("https://automationexercise.com/products")
    expect(page).to_have_title("Automation Exercise - All Products")
    expect(page.locator("#sale_image")).to_be_visible()
    expect(page.get_by_placeholder("Search Product")).to_be_visible()


def test_products_list_visible(page: Page):
    page.goto("https://automationexercise.com/products")
    expect(page).to_have_title("Automation Exercise - All Products")
    products_list = page.locator(".features_items .col-sm-4")
    assert products_list.count() > 0


def test_products_search_works(page: Page):
    page.goto("https://automationexercise.com/products")
    product_search_input = page.get_by_placeholder("Search Product")
    expect(product_search_input).to_be_visible()
    product_search_input.type("Peacock Blue Cotton")
    page.locator("#submit_search").click()

    results = page.locator(".features_items .col-sm-4")
    assert results.count() == 1
    expect(results.nth(0)).to_contain_text(
        "Beautiful Peacock Blue Cotton Linen Saree")


def test_products_search_finds_no_results_with_invalid_data(page: Page):
    page.goto("https://automationexercise.com/products")
    product_search_input = page.get_by_placeholder("Search Product")
    expect(product_search_input).to_be_visible()
    product_search_input.fill("asdasda")
    page.locator("#submit_search").click()

    results = page.locator(".features_items .col-sm-4")
    assert results.count() == 0
