from playwright.sync_api import Page, expect


def dismiss_google_vignette_if_present(page: Page):
    try:
        if "#google_vignette" in page.url:
            close_button = page.locator("#dismiss-button-element")
            close_button.wait_for(state="visible", timeout=2000)
            close_button.click()
            page.wait_for_load_state("domcontentloaded")
            return

        close_button = page.get_by_text("Close", exact=True)
        if close_button.is_visible(timeout=2000):
            close_button.click()
            page.wait_for_timeout(500)

    except TimeoutError:
        pass
