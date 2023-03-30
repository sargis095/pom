import pytest
from pages.navigation_panel import NavigationPanel


@pytest.mark.usefixtures("log_in")
class TestNavigationPanel:

    def test_recruitment_page(self):
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("Recruitment")
        assert navigation_panel.wait_until_url_to_be()



