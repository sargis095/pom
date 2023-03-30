import pytest

from pages.login import LoginPage
from pages.navigation_panel import NavigationPanel


@pytest.mark.usefixtures("set_up")
class TestLogin:

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.wait_for_page_load()
        login_page.login("Admin", 'Kaqav')
        assert login_page.is_invalid_credential_alert_visible()

    # def test_valid_login(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.wait_for_page_load()
    #     login_page.login("Admin", "admin123")








