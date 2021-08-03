from .pages.product_page import ProductPage

import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page_and_add_to_basket()
    page.product_name_in_message_is_the_same()
    page.product_price_in_message_is_the_same()
    time.sleep(10)


    # pytest -s --tb=line --language=en lesson_4_3_1/test_product_page.py