
# Home page UI test suite

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

BASE_URL = "https://the-internet.herokuapp.com"


@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.open_home_page(BASE_URL)
    return page


@pytest.mark.ui
@pytest.mark.smoke
class TestHomePage:

    def test_home_page_loads(self, home_page):
        assert "The Internet" in home_page.get_title()

    def test_heading_present(self, home_page):
        assert "Welcome to the-internet" in home_page.get_heading_text()

    def test_links_present(self, home_page):
        assert home_page.count_available_links() > 10

    def test_navigate_to_login(self, home_page, driver):
        home_page.navigate_to_login()
        assert "login" in driver.current_url

    @pytest.mark.regression
    def test_all_links_have_text(self, home_page):
        links = home_page.get_all_link_texts()
        assert all(link.strip() for link in links), "Found link with no text"

    @pytest.mark.regression
    def test_url_correct(self, home_page):
        assert home_page.get_current_url() == f"{BASE_URL}/"
