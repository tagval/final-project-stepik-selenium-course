from .pages.main_page import MainPage
import time
#def test_guest_can_go_to_login_page(browser):
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
   # page.go_to_login_page()
    page.should_be_login_link()
    time.sleep(10)


    # pytest -v --tb=line --language=en lesson_4_2/test_main_page.py