from playwright.sync_api import Page, expect


def test_dynamic_loading(page: Page):

    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    page.click("#start button")

    # The #finish element doesn't exist yet — it appears 5 seconds later

    expect(page.locator("#finish h4")).to_have_text("Hello World!")


def test_dynamic_loading_with_render(page: Page):

    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    page.click("#start button")

    expect(page.locator("#finish h4")).to_have_text("Hello World!")