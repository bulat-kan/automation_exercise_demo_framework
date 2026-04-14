from playwright.sync_api import expect, Page
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage


def test_view_product_takes_to_product_details(page: Page):
    products_page = ProductsPage(page)
    products_page.open()

    first_product = products_page.products_list().nth(0)
    product_name = first_product.locator("p").first.inner_text().strip()
    product_price = first_product.locator("h2").first.inner_text().strip()

    first_product.get_by_role("link", name="View Product").click()
    assert "product_details/" in page.url

    product_details_page = ProductDetailsPage(page)
    assert product_name == product_details_page.product_name_header().inner_text().strip()

    assert product_price == product_details_page.product_price().inner_text().strip()


def test_product_details_page_components(page: Page):
    products_page = ProductsPage(page)
    products_page.open()
    product = products_page.products_list().nth(0)
    product.get_by_role("link", name="View Product").click()

    product_details_page = ProductDetailsPage(page)
    expect(product_details_page.product_image()).to_be_visible()

    details = product_details_page.product_detail_labels_texts()
    assert any("Category" in text for text in details)
    assert any("Availability" in text for text in details)
    assert any("Condition" in text for text in details)
    assert any("Brand" in text for text in details)

    expect(product_details_page.name_review_input()).to_be_visible()

    expect(product_details_page.email_review_input()).to_be_visible()
    expect(product_details_page.review_input()).to_be_visible()


def test_product_details_page_user_can_submit_review(page):
    prod_details_page = ProductDetailsPage(page)
    prod_details_page.open("1")

    prod_details_page.submit_review(
        "The Witcher", "thewitcher@mail.com", "good product!")
    expect(page.locator("div.alert-success.alert span")
           ).to_contain_text("Thank you for your review")


def test_user_can_add_product_from_product_details(page: Page):
    prod_details_page = ProductDetailsPage(page)
    prod_details_page.open("1")
    prod_details_page.add_to_cart_btn().click()
    expect(prod_details_page.modal_added_header()).to_have_text("Added!")
    expect(prod_details_page.modal_added_body_message()).to_have_text(
        "Your product has been added to cart.")

    expect(prod_details_page.modal_added_continue_shopping_btn()).to_be_visible()
    prod_details_page.modal_added_body_view_cart_link().click()

    assert "view_cart" in page.url

    expect(page.locator("a.check_out")).to_be_visible()
