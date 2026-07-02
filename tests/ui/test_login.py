# UI test suite for login flow
# Uses Page Object Model via LoginPage

import pytest
from pages.login_page import LoginPage

BASE_URL = "https://the-internet.herokuapp.com"
VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open_login_page(BASE_URL)
    return page


@pytest.mark.ui
@pytest.mark.smoke
class TestLogin:

    def test_valid_login_succeeds(self, login_page):
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        assert login_page.is_login_successful()
        assert "secure" in login_page.get_current_url()

    def test_valid_login_flash_message(self, login_page):
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        message = login_page.get_flash_message()
        assert "You logged into a secure area" in message

    @pytest.mark.regression
    def test_invalid_username(self, login_page):
        login_page.login("wronguser", VALID_PASSWORD)
        message = login_page.get_flash_message()
        assert "Your username is invalid" in message
        assert not login_page.is_login_successful()

    @pytest.mark.regression
    def test_invalid_password(self, login_page):
        login_page.login(VALID_USERNAME, "wrongpassword")
        message = login_page.get_flash_message()
        assert "Your password is invalid" in message

    @pytest.mark.regression
    def test_empty_credentials(self, login_page):
        login_page.login("", "")
        assert not login_page.is_login_successful()

    @pytest.mark.regression
    def test_logout_returns_to_login(self, login_page):
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        assert login_page.is_login_successful()
        login_page.logout()
        assert login_page.is_on_login_page()

    def test_page_title_correct(self, login_page):
        assert "The Internet" in login_page.get_title()

    @pytest.mark.parametrize("username, password", [
        ("", VALID_PASSWORD),
        (VALID_USERNAME, ""),
        ("", ""),
        ("admin", "admin"),
    ])
    def test_various_invalid_combinations(self, login_page, username, password):
        login_page.login(username, password)
        assert not login_page.is_login_successful()
