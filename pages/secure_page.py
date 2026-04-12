from playwright.sync_api import expect

class SecurePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/secure"
        self.page_heading = page.locator("h2")
        self.logout_button = page.get_by_role("link", name="Logout")

    @property
    def heading_text(self):
        return self.page_heading.inner_text()

    def logout(self):
        self.logout_button.click()

    def should_be_on_secure_page(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/secure")
        expect(self.page_heading).to_have_text("Secure Area")

