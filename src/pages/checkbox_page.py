from selenium.webdriver.common.by import By


class CheckboxPage:
    def __init__(self, driver):
        self.driver = driver

    CHECKBOX_1 = (By.XPATH, "//input[@type='checkbox'][1]")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")

    def select_checkbox(self):
        checkbox = self.driver.find_element(*self.CHECKBOX_1)
        if not checkbox.is_selected():
            checkbox.click()

    def is_checkbox_selected(self):
        return self.driver.find_element(*self.CHECKBOX_1).is_selected()
