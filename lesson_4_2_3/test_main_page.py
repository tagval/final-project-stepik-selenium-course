from .pages.main_page import MainPage
import time
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    time.sleep(10)


    # pytest -v --tb=line --language=en lesson_4_2_3/test_main_page.py