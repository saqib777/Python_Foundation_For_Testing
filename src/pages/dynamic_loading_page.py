from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    FINISH_TEXT = (By.ID, "finish")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def click_start(self):
        self.wait.until(EC.element_to_be_clickable(self.START_BUTTON)).click()

    def get_finish_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.FINISH_TEXT))
        return element.text
