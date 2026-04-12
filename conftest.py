import pytest

from pages.checkboxes_page import CheckboxesPage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from playwright.sync_api import Page, expect


@pytest.fixture(autouse=True)
def configure_timeouts(page: Page):
    page.set_default_timeout(10000)
    expect.set_options(timeout=10000)

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.navigate()
    return lp

@pytest.fixture
def checkbox_page(page):
    cp = CheckboxesPage(page)
    cp.navigate()
    return cp


