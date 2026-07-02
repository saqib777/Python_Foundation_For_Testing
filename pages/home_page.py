# Home Page Object
# Targets the-internet.herokuapp.com landing page

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page object for the site's home/landing page."""

    PAGE_HEADING       = (By.TAG_NAME, "h1")
    ALL_LINKS          = (By.CSS_SELECTOR, "ul li a")
    LOGIN_LINK         = (By.LINK_TEXT, "Form Authentication")
    DROPDOWN_LINK      = (By.LINK_TEXT, "Dropdown")
    CHECKBOXES_LINK    = (By.LINK_TEXT, "Checkboxes")
    DYNAMIC_LOAD_LINK  = (By.LINK_TEXT, "Dynamic Loading")

    def open_home_page(self, base_url: str):
        self.open(base_url)
        return self

    def get_heading_text(self) -> str:
        return self.get_text(self.PAGE_HEADING)

    def get_all_link_texts(self) -> list[str]:
        elements = self.driver.find_elements(*self.ALL_LINKS)
        return [el.text for el in elements]

    def navigate_to_login(self):
        self.click(self.LOGIN_LINK)
        return self

    def navigate_to_dropdown(self):
        self.click(self.DROPDOWN_LINK)
        return self

    def navigate_to_checkboxes(self):
        self.click(self.CHECKBOXES_LINK)
        return self

    def count_available_links(self) -> int:
        return len(self.driver.find_elements(*self.ALL_LINKS))
