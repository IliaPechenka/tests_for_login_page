import time
from pages.page_login import LoginPage
from pages.page_personal_area import PersonalAreaPage

email = 'someemail321@rambler.ru'
password = 'optZ80vG'


class TestsLogin:

    def test_authorization_with_email(self, browser):
        LoginPage(browser).input_login_or_email(email)
        LoginPage(browser).click_btn_login()
        LoginPage(browser).input_password(password)
        LoginPage(browser).click_btn_login()
        PersonalAreaPage(browser).wait_page_load()
        assert browser.current_url == 'https://id.yandex.ru/'

    def test_incorrect_password(self, browser):
        assert LoginPage(browser).check_status_press_btn_post()
        LoginPage(browser).input_login_or_email(email)
        LoginPage(browser).click_btn_login()
        LoginPage(browser).input_password('blablabla')
        LoginPage(browser).click_btn_login()
        assert LoginPage(browser).search_contains_text_on_a_page('Неверный пароль')

    def test_check_btn_create_id(self, browser):
        LoginPage(browser).click_btn_create_id()
        time.sleep(3)  #Плохая практика, но обрабатывать загрузку страницы из-за 1 теста выглядит нерационально
        assert browser.title == 'Регистрация'

    def test_check_press_btn_phone(self, browser):
        LoginPage(browser).click_press_btn_phone()
        assert LoginPage(browser).check_status_press_btn_phone(), \
            "Нажатие на кнопку 'Телефон' не вывело форму для ввода телефона"

    def test_do_not_remember(self, browser):
        LoginPage(browser).click_not_remember()
        LoginPage(browser).input_phone('926 456 40 79')
        LoginPage(browser).click_btn_submit()
        assert LoginPage(browser).search_contains_text_on_a_page('Введите код из смс')

    def test_login_from_vk(self, browser):
        LoginPage(browser).click_icon_vk()
        windows = browser.window_handles
        browser.switch_to.window(windows[1])
        assert LoginPage(browser).check_redirect_vk(), 'Переход на экран авторизации с помощью VK не осуществлён'

    def test_validation_correct_email(self, browser):
        list_incorrect_email = ['', 'email@111.222.333.text.', 'email.domain.com', '@domain.com', '#@%^%#$@#$@#.com',
                                'Joe Smith <email@domain.com>', 'email@domain@domain.com', '.email@domain.com']
        for i in range(len(list_incorrect_email)):
            LoginPage(browser).input_login_or_email(list_incorrect_email[i])
            LoginPage(browser).click_btn_login()
            assert LoginPage(browser).check_text_error_login(), \
                f'Не выводится текст ошибки о некорректном email {list_incorrect_email[i]}'
            LoginPage(browser).clear_form_login()
