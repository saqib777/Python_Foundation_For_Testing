# Dropdown Page Object
# Targets the-internet.herokuapp.com/dropdown

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    """Page object for the Dropdown example page."""

    DROPDOWN    = (By.ID, "dropdown")
    PAGE_HEADER = (By.CSS_SELECTOR, "div.example h1")

    DROPDOWN_PATH = "/dropdown"

    def open_dropdown_page(self, base_url: str):
        self.open(f"{base_url}{self.DROPDOWN_PATH}")
        return self

    def get_select_element(self):
        return Select(self.driver.find_element(*self.DROPDOWN))

    def select_option_by_text(self, text: str):
        self.get_select_element().select_by_visible_text(text)
        return self

    def select_option_by_value(self, value: str):
        self.get_select_element().select_by_value(value)
        return self

    def select_option_by_index(self, index: int):
        self.get_select_element().select_by_index(index)
        return self

    def get_selected_option_text(self) -> str:
        return self.get_select_element().first_selected_option.text

    def get_all_options(self) -> list[str]:
        return [opt.text for opt in self.get_select_element().options]

    def get_header_text(self) -> str:
        return self.get_text(self.PAGE_HEADER)
