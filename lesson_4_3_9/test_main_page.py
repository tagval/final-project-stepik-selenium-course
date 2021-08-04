from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    time.sleep(10)

def test_guest_can_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_guest_can_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_guest_can_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    #login_page = page.go_to_login_page() # 1й способ перехода когда в main_page.py инициализируется новый объект Page и возвращают его, а потом в теле теста просто используют ту переменную, куда произошло сохранение
    page.go_to_login_page() # 2й способ перехода когда LoginPage инициализируется в теле теста
    login_page = LoginPage(browser, browser.current_url) # 2й способ
    login_page.should_be_login_page()

    # pytest -v --tb=line --language=en lesson_4_2_login_page/test_main_page.py
