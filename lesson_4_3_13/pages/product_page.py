from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page_and_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def go_to_product_page_and_add_to_basket_and_solve_quiz(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        BasePage.solve_quiz_and_get_code(self)

    def product_name_in_message_is_the_same(self):
        name_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE).text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERTINNER).text
        assert name_text == name_in_message, "Wrong product NAME in alertinner"

    def product_price_in_message_is_the_same(self):
        price_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_PAGE).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERTINNER).text
        assert price_text == price_in_message, "Wrong product PRICE in alertinner"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"
