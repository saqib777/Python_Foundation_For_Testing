# Base Page Object — shared actions for all page classes
# Part of the Page Object Model architecture

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """
    Base class that every page object inherits from.
    Wraps common Selenium actions with explicit waits built in,
    so individual page classes never need to write wait logic themselves.
    """

    def __init__(self, driver, timeout: int = 10):
        self.driver  = driver
        self.wait    = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)
        return self

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def type_text(self, locator, text: str, clear_first: bool = True):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear_first:
            element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_attribute(self, locator, attribute: str) -> str:
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    def is_displayed(self, locator) -> bool:
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def is_enabled(self, locator) -> bool:
        try:
            return self.driver.find_element(*locator).is_enabled()
        except NoSuchElementException:
            return False

    def wait_for_url_contains(self, partial_url: str, timeout: int = None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        wait.until(EC.url_contains(partial_url))
        return self

    def wait_for_element_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
        return self

    def select_dropdown_by_text(self, locator, visible_text: str):
        from selenium.webdriver.support.ui import Select
        element = self.wait.until(EC.presence_of_element_located(locator))
        Select(element).select_by_visible_text(visible_text)
        return self

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self

    def take_screenshot(self, filename: str):
        self.driver.save_screenshot(filename)
        return self

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_title(self) -> str:
        return self.driver.title

    def refresh(self):
        self.driver.refresh()
        return self
