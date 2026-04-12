from playwright.sync_api import expect

class DropdownPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/dropdown"
        self.dropdown = page.locator("#dropdown")

    def navigate(self):
        self.page.goto(self.url)

    def select_option_by_value(self, value):
        self.dropdown.select_option(value)

    def should_have_value(self, expected):
        expect(self.dropdown).to_have_value(expected)