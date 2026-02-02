from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_login_successful(self):
        return "secure" in self.driver.current_url

    def login(self, username, password):
     self.enter_username(username)
     self.enter_password(password)
     self.click_login()

    ERROR_MESSAGE = (By.ID, "flash")
    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
    
    def is_login_successful(self):
      WebDriverWait(self.driver, 5).until(
         EC.url_contains("secure")
      )
      return "secure" in self.driver.current_url
