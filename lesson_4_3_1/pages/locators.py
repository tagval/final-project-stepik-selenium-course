from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #теперь каждый селектор — это пара: как искать и что искать.

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, ".row h1")
    PRODUCT_NAME_ALERTINNER = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_PRICE_PAGE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_ALERTINNER = (By.CSS_SELECTOR, ".alert-info p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


