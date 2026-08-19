# Checkboxes Page Object
# Targets the-internet.herokuapp.com/checkboxes

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    """Page object for the Checkboxes example page."""

    CHECKBOXES    = (By.CSS_SELECTOR, "input[type='checkbox']")
    PAGE_HEADER   = (By.CSS_SELECTOR, "div.example h3")
    CHECKBOX_PATH = "/checkboxes"

    def open_checkboxes_page(self, base_url: str):
        self.open(f"{base_url}{self.CHECKBOX_PATH}")
        return self

    def get_all_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def get_checkbox(self, index: int):
        return self.get_all_checkboxes()[index]

    def is_checked(self, index: int) -> bool:
        return self.get_checkbox(index).is_selected()

    def check(self, index: int):
        cb = self.get_checkbox(index)
        if not cb.is_selected():
            cb.click()
        return self

    def uncheck(self, index: int):
        cb = self.get_checkbox(index)
        if cb.is_selected():
            cb.click()
        return self

    def toggle(self, index: int):
        self.get_checkbox(index).click()
        return self

    def check_all(self):
        for cb in self.get_all_checkboxes():
            if not cb.is_selected():
                cb.click()
        return self

    def uncheck_all(self):
        for cb in self.get_all_checkboxes():
            if cb.is_selected():
                cb.click()
        return self

    def count_checked(self) -> int:
        return sum(1 for cb in self.get_all_checkboxes() if cb.is_selected())

    def count_total(self) -> int:
        return len(self.get_all_checkboxes())

    def get_header_text(self) -> str:
        return self.get_text(self.PAGE_HEADER)
