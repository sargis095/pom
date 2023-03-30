import pytest
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver import Keys


@pytest.mark.usefixtures('log_in')
class PersonalDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    NAME = (By.CSS_SELECTOR, "input[name='firstName']")
    MIDDLE_NAME = (By.CSS_SELECTOR, "input[name='middleName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name = 'lastName']")
    MY_NAME = 'Clark'
    MY_MIDDLE_NAME = 'Junior'
    MY_LAST_NAME = "Bush"
    INPUT_FIELDS = (By.CSS_SELECTOR, 'input[class= "oxd-input oxd-input--active"]')
    NATIONALITY_FIELD = (By.CSS_SELECTOR, ".oxd-select-text")
    NATIONALITIES_LIST = (By.CSS_SELECTOR, "div[class='oxd-select-option']")
    MARTIAL_STATUS_OPTION = (By.XPATH, '//span[text()="Married"]')
    MARTIAL_STATUS_OPTION_UNSELECT = (By.XPATH, '//div[text()="-- Select --"]')
    GENERAL = (By.CSS_SELECTOR, 'div[class="oxd-select-text oxd-select-text--active"]')
    GENDER = (By.XPATH, '(//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"])[1]')
    SUBMIT = (By.CSS_SELECTOR, "button[type = 'submit']")

    def clear_input(self, clear_field):
        element = self.get_wait().wait_for_element(clear_field)
        self.element_send_keys(element, Keys.CONTROL + 'a')
        self.element_send_keys(element, Keys.BACK_SPACE)

    def clear_multiple_inputs(self):
        self.element_send_keys_without_selector(Keys.CONTROL + 'a')
        self.element_send_keys_without_selector(Keys.BACK_SPACE)

    def fill_name(self, filled_name, fill_field):
        element = self.get_wait().wait_for_element_to_be_clickable(filled_name)
        self.element_send_keys(element, fill_field)

    def find_input_fields(self):
        # input_field.fill_name(input_field, self.INPUT_FIELDS_NAME[i])
        # input_fields[i].send_keys(Keys.CONTROL + 'a')
        # input_fields[i].send_keys(Keys.BACK_SPACE)
        # nput_fields[i].send_keys(self.INPUT_FIELDS_NAME[j])
        input_fields = self.get_wait().wait_for_list_size_change(self.INPUT_FIELDS, 10)
        fields_inputs = {
            input_fields[0]: 'Nickname',
            input_fields[1]: '1001',
            input_fields[2]: '1002',
            input_fields[3]: '1003',
            input_fields[4]: '1004',
            input_fields[5]: '2023-03-16',
            input_fields[6]: '1006',
            input_fields[7]: '1007',
            input_fields[8]: '2023-03-16',
            input_fields[9]: '1009'
        }
        for key, value in fields_inputs.items():
            key.send_keys(Keys.CONTROL + 'a')
            key.send_keys(Keys.BACK_SPACE)
            key.send_keys(value)

    def nationality_checker(self):
        nationality_fild = self.get_wait().wait_for_element_to_be_clickable(self.NATIONALITY_FIELD)
        nationality_fild.click()
        nationalities_list = self.get_wait().wait_for_list_size_change(self.NATIONALITIES_LIST, 193)
        nationalities_list[70].click()

    # It's have a Timeout Exception Error. I don't know why.
    def martial_status(self):
        martial_status_field = self.get_wait().wait_for_element_to_be_clickable(self.selection(2))
        martial_status_field.click()
        martial_status_option = self.get_wait().wait_for_element(self.MARTIAL_STATUS_OPTION)
        martial_status_option.click()

    def selection(self, index):
        selection_field = self.get_wait().wait_for_list_size_change(self.GENERAL, 3)
        return selection_field[index]

    def radio_button_selection(self):
        gender_field = self.get_wait().wait_for_element(self.GENDER)
        gender_field.click()

    def submit(self):
        submit_field = self.get_wait().wait_for_element(self.SUBMIT)
        submit_field.click()

    def assertion(self):
        firstname = self.get_wait().wait_for_element(self.NAME)
        return firstname.get_attribute('value') == self.MY_NAME