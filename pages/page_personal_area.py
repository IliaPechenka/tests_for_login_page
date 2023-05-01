from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PersonalAreaPageLocators:
    AVATAR_ICON = (By.CLASS_NAME, 'UserID-Avatar')


class PersonalAreaPage(BasePage):
    def wait_page_load(self):
        self.wait_element(PersonalAreaPageLocators.AVATAR_ICON)
