from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_HEADER = (By.TAG_NAME, "span a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p > a")
    BASKET_ITEMS = (By.CSS_SELECTOR,"basket-items")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REG = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM_REG = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_REG_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, ".row h1")
    PRODUCT_NAME_ALERTINNER = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_PRICE_PAGE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_ALERTINNER = (By.CSS_SELECTOR, ".alert-info p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


