from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage (BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Item is in the basket"

    def text_basket_is_empty_should_be_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Message about empty basket isn't presented"