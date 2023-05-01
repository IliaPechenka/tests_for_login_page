import pytest
import os
from selenium import webdriver

DRIVERS = os.path.expanduser("~/Downloads/drivers")
CHROMEDRIVER = f"{DRIVERS}/chromedriver"


@pytest.fixture(scope="function")
def browser():
    chrome_driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    chrome_driver.get("https://passport.yandex.ru/")
    chrome_driver.maximize_window()
    chrome_driver.set_page_load_timeout(15)
    yield chrome_driver
    chrome_driver.quit()
