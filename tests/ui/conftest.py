import pytest
from playwright.sync_api import sync_playwright


AD_KEYWORDS = [
    "google_vignette",
    "doubleclick",
    "googlesyndication",
    "googleads",
    "adservice",
]


def should_block(url: str) -> bool:
    return any(keyword in url for keyword in AD_KEYWORDS)


@pytest.fixture
def page():
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-qa")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})

        def handle_route(route):
            url = route.request.url
            if should_block(url):
                route.abort()
            else:
                route.continue_()

        context.route("**/*", handle_route)

        page = context.new_page()
        yield page
        browser.close()
