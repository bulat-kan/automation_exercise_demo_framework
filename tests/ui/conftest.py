from pathlib import Path

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


def safe_artifact_name(nodeid: str) -> str:
    return (
        nodeid.replace("/", "_")
        .replace("::", "__")
        .replace("[", "_")
        .replace("]", "_")
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"report_{report.when}", report)


@pytest.fixture
def page(request):
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
        try:
            yield page
            if request.node.report_call.failed:
                screenshot_dir = Path("test-results/screenshots")
                screenshot_dir.mkdir(parents=True, exist_ok=True)
                screenshot_path = screenshot_dir / \
                    f"{safe_artifact_name(request.node.nodeid)}.png"
                page.screenshot(path=str(screenshot_path), full_page=True)
        finally:
            browser.close()
