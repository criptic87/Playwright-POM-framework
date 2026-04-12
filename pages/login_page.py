from  playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"

        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"
        self.flash_message = "#flash"

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    @property
    def error_message(self):
        return self.page.locator(self.flash_message).inner_text()

    @property
    def success_message(self):
        return self.page.locator(self.flash_message).inner_text()

    def should_show_success_message(self, text):
        expect(self.page.locator(self.flash_message)).to_contain_text(text)

    def should_show_error_message(self, text):
        expect(self.page.locator(self.flash_message)).to_contain_text(text)