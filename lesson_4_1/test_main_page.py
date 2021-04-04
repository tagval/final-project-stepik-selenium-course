import time
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    time.sleep(10)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

    # pytest -v --tb=line --language=en lesson_4_1/test_main_page.py