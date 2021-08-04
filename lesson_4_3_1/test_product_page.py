from .pages.product_page import ProductPage
import time
import pytest

# @pytest.mark.parametrize('promo_number', [0, 1, 2, 3, 4, 5, 6,
#                                   pytest.param(7, marks=pytest.mark.xfail),
#                                   8, 9])

# def test_guest_can_add_product_to_basket(browser,promo_number):
#     #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offerN"
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_product_page_and_add_to_basket_and_solve_quiz()
#     page.product_name_in_message_is_the_same()
#     page.product_price_in_message_is_the_same()
#     time.sleep(2)

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page_and_add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page_and_add_to_basket()
    page.success_message_disappeared()

    # pytest -s -v --tb=line --language=en lesson_4_3_1/test_product_page.py