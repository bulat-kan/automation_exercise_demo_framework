from pathlib import Path

from playwright.sync_api import Page, expect

UPLOAD_FILE = Path(__file__).parents[2] / "data" / "upload.txt"


def test_contact_us_form_success(page: Page):
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Contact us").click()
    expect(page).to_have_url("https://automationexercise.com/contact_us")
    expect(page.get_by_role("heading", name="Get In Touch")).to_be_visible()

    page.get_by_placeholder("Name").fill("JKVD")
    page.get_by_role("textbox", name="Email", exact=True).fill("jkvd@jkvd.com")
    page.get_by_placeholder("Subject").fill("Application experience feedback")
    page.get_by_placeholder("Your Message Here").fill(
        "Great application! too many ads though, but was able to block them")

    upload_field = page.locator("input[type='file']")
    upload_field.set_input_files(str(UPLOAD_FILE))
    assert "upload.txt" in upload_field.input_value()

    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Submit").click()

    success_message = page.locator(".status.alert-success")
    expect(success_message).to_be_visible()
    expect(success_message).to_contain_text(
        "Success! Your details have been submitted successfully."
    )

    page.locator("a.btn.btn-success").click()
    expect(page).to_have_url("https://automationexercise.com/")
