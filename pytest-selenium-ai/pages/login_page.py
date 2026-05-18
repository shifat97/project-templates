from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = '/login'
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-btn')
    ERROR_MSG = (By.CLASS_NAME, 'error-message')
    FORGOT_LINK = (By.LINK_TEXT, 'Forgot Password?')

    def open(self):
        return self.visit(self.PATH)

    def login(self, email, password):
        self.type_text(self.EMAIL, email)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        return self

    def get_error(self):
        return self.get_text(self.ERROR_MSG)

    def click_forgot_password(self):
        self.click(self.FORGOT_LINK)
        return self
