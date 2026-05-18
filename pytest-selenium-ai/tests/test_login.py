import pytest

from config.config import Config
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


class TestLogin:
    @pytest.mark.smoke
    @pytest.mark.auth
    def test_valid_login_redirects_to_dashboard(self, driver):
        """Valid credentials → dashboard URL and welcome banner."""
        LoginPage(driver).open().login(
            Config.VALID_EMAIL, Config.VALID_PASSWORD
        )
        dash = DashboardPage(driver)
        dash.wait_for_url('/dashboard')
        assert dash.is_loaded(), 'Dashboard welcome banner not visible'

    @pytest.mark.auth
    def test_invalid_password_shows_error(self, driver):
        """Wrong password → inline error message displayed."""
        page = LoginPage(driver).open()
        page.login(Config.VALID_EMAIL, 'WrongPass!')
        assert 'Invalid credentials' in page.get_error()

    @pytest.mark.auth
    def test_empty_email_shows_validation(self, driver):
        """Empty email → field-level validation error."""
        page = LoginPage(driver).open()
        page.login('', 'SomePass1!')
        assert page.is_visible(LoginPage.ERROR_MSG)

    @pytest.mark.auth
    def test_forgot_password_navigates_correctly(self, driver):
        """Forgot Password link leads to reset page."""
        LoginPage(driver).open().click_forgot_password()
        assert '/forgot-password' in driver.current_url

    def test_login_page_title(self, driver):
        """Page title matches expected value."""
        LoginPage(driver).open()
        assert 'Login' in driver.title
