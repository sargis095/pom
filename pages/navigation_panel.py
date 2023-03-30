from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from wait.wait import Wait



class NavigationPanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ROOT_ELEMENT = (By.CSS_SELECTOR, 'nav[aria-label="Sidepanel"]')
    NAVIGATION_ITEMS = (By.CSS_SELECTOR, 'ul[class=oxd-main-menu] > li')
    # PAGE_IS_VISIBLE = (By.CSS_SELECTOR, 'a.oxd-main-menu-item active')
    NEW_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates'

    def get_navigation_items(self):
        self.get_wait().wait_for_page()
        navigation_elements = self.get_wait().wait_for_list_size_change(self.NAVIGATION_ITEMS, size=11)
        navigation_item_names = ['Admin', 'PIM', 'LEAVE', 'TIME', 'Recruitment', 'My_Info', 'Performance', 'Dashboard',
                                 'Directory', 'Maintenance', 'Buzz']
        return dict(zip(navigation_item_names, navigation_elements))

    def go_to(self, page):
        element = self.get_navigation_items().get(page)
        self.get_wait().wait_for_element_to_be_clickable(element)
        self.click(element)


    def wait_until_url_to_be(self):
        return self.get_current_url() == self.NEW_URL