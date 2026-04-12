
from playwright.sync_api import expect

class CheckboxesPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/checkboxes"
        self.checkbox1 = page.locator("#checkboxes input[type='checkbox']").nth(0)
        self.checkbox2 = page.locator("#checkboxes input[type='checkbox']").nth(1)

    def navigate(self):
        self.page.goto(self.url)

    def check_first(self):
       self.checkbox1.check()

    def uncheck_second(self):
        self.checkbox2.uncheck()

    def should_first_be_checked(self):
        expect(self.checkbox1).to_be_checked()

    def should_first_not_be_checked(self):
        expect(self.checkbox1).not_to_be_checked()

    def should_second_be_checked(self):
        expect(self.checkbox2).to_be_checked()

    def should_second_not_be_checked(self):
        expect(self.checkbox2).not_to_be_checked()