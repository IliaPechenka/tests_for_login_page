from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, wait=15):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)

    def wait_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator), message=f"Element {locator} not found!")

    def send_keys(self, locator, value):
        find_field = self.wait_element(locator)
        find_field.send_keys(value)

    def click(self, locator):
        find_field = self.wait_element(locator)
        find_field.click()

    def find_element(self, locator):
        return self.wait_element(locator)

    def clear(self, locator):
        self.wait_element(locator).clear()
