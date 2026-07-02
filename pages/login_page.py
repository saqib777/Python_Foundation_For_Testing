# Login Page Object
# Targets the-internet.herokuapp.com/login (public test site)

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login screen."""

    USERNAME_INPUT  = (By.ID, "username")
    PASSWORD_INPUT  = (By.ID, "password")
    LOGIN_BUTTON    = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE   = (By.ID, "flash")
    LOGOUT_BUTTON   = (By.CSS_SELECTOR, "a.button.secondary")
    SECURE_HEADING  = (By.CSS_SELECTOR, "div.example h2")

    LOGIN_PATH = "/login"

    def open_login_page(self, base_url: str):
        self.open(f"{base_url}{self.LOGIN_PATH}")
        return self

    def enter_username(self, username: str):
        self.type_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        self.type_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, username: str, password: str):
        return (self.enter_username(username)
                    .enter_password(password)
                    .click_login())

    def get_flash_message(self) -> str:
        return self.get_text(self.FLASH_MESSAGE)

    def is_login_successful(self) -> bool:
        return self.is_displayed(self.SECURE_HEADING)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
        return self

    def is_on_login_page(self) -> bool:
        return self.get_current_url().endswith(self.LOGIN_PATH)
