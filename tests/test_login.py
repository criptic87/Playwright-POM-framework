import pytest

from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_login_success(login_page, test_users):
    user = test_users["valid_user"]
    login_page.login(user["username"], user["password"])
    assert "You logged into a secure area!" in login_page.success_message

def test_login_failure(login_page, test_users):
    user = test_users["invalid_user"]
    login_page.login(user["username"], user["password"])
    assert "Your username is invalid!" in login_page.error_message

def test_logging_and_logout(login_page, page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(page)
    assert "Secure Area" == secure_page.heading_text
    secure_page.logout()
    assert "You logged out of the secure area!" in login_page.success_message

@pytest.mark.parametrize("username, password, expected_error", [
    ("wrong_user", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "wrong_password", "Your password is invalid!"),
    ("", "", "Your username is invalid!"),
])
def test_login_invalid_credentials(login_page, username, password, expected_error):
    login_page.login(username, password)
    assert expected_error in login_page.error_message