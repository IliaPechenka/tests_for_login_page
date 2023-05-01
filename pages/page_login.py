from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORM_LOGIN_OR_EMAIL = (By.ID, 'passp-field-login')
    FORM_PHONE = (By.ID, 'passp-field-phone')
    FORM_PASS = (By.ID, 'passp-field-passwd')
    BTN_LOGIN = (By.ID, 'passp:sign-in')
    CREATE_ID = (By.ID, 'passp:exp-register')
    PRESS_BTN_POST = (By.XPATH, "//button[@data-type='login']")
    PRESS_BTN_PHONE = (By.XPATH, "//button[@data-type='phone']")
    NOT_REMEMBER = (By.LINK_TEXT, 'Не помню')
    VK_ICON = (By.XPATH, "//span[@data-t='icon:vk']")
    BTN_SUBMIT = (By.XPATH, "//button[@type='submit']")
    ABOUT_VK = (By.XPATH,
                "//div[@class='vkc__ContentHeader__header vkc__ContentHeader__transitionalFixup']")  # Плохая практика, но лучше решения не нашлось
    TEXT_ERROR_LOGIN = (By.ID, "field:input-login:hint")


class LoginPage(BasePage):
    def check_text_error_login(self):
        return self.find_element(LoginPageLocators.TEXT_ERROR_LOGIN)

    def clear_form_login(self):
        self.clear(LoginPageLocators.FORM_LOGIN_OR_EMAIL)

    def click_btn_submit(self):
        self.click(LoginPageLocators.BTN_SUBMIT)

    def check_redirect_vk(self):
        return self.find_element(LoginPageLocators.ABOUT_VK)

    def click_icon_vk(self):
        self.click(LoginPageLocators.VK_ICON)

    def input_password(self, text):
        self.send_keys(LoginPageLocators.FORM_PASS, f"{text}")

    def input_login_or_email(self, text):
        self.send_keys(LoginPageLocators.FORM_LOGIN_OR_EMAIL, f"{text}")

    def input_phone(self, text):
        self.send_keys(LoginPageLocators.FORM_PHONE, f"{text}")

    def search_contains_text_on_a_page(self, text):
        return self.find_element((By.XPATH, f"//*[contains(text(),'{text}')]"))

    def click_btn_login(self):
        self.click(LoginPageLocators.BTN_LOGIN)

    def click_btn_create_id(self):
        self.click(LoginPageLocators.CREATE_ID)

    def click_post_login(self):
        self.click(LoginPageLocators.PRESS_BTN_POST)

    def check_status_press_btn_post(self):
        return self.find_element(LoginPageLocators.PRESS_BTN_POST).get_attribute('aria-pressed')

    def check_status_press_btn_phone(self):
        return self.find_element(LoginPageLocators.PRESS_BTN_PHONE).get_attribute('aria-pressed')

    def click_press_btn_phone(self):
        self.click(LoginPageLocators.PRESS_BTN_PHONE)

    def click_not_remember(self):
        self.click(LoginPageLocators.NOT_REMEMBER)
