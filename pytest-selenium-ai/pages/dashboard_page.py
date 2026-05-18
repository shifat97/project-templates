from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    PATH = '/dashboard'
    WELCOME_MSG = (By.ID, 'welcome-banner')
    LOGOUT_BTN = (By.ID, 'logout-btn')
    NAV_MENU = (By.CSS_SELECTOR, 'nav.sidebar')

    def is_loaded(self):
        return self.is_visible(self.WELCOME_MSG)

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MSG)

    def logout(self):
        self.click(self.LOGOUT_BTN)
        return self
