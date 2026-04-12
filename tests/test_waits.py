from playwright.sync_api import Page, expect


def test_dynamic_loading(page: Page):
    """This page has a 'Start' button that triggers a 5-second loading bar.
    The element appears AFTER 5 seconds. Watch how Playwright handles it."""
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    page.click("#start button")

    # The #finish element doesn't exist yet — it appears 5 seconds later
    # Playwright auto-waits for it. No sleep, no manual wait.
    expect(page.locator("#finish h4")).to_have_text("Hello World!")


def test_dynamic_loading_with_render(page: Page):
    """This page is even harder — the element doesn't even EXIST in the DOM
    until after the loading completes. Same code still works."""
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    page.click("#start button")

    expect(page.locator("#finish h4")).to_have_text("Hello World!")