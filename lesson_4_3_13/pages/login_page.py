from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_address_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_REG)
        email_address_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REG)
        password_input.send_keys(password)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_REG)
        password_confirm_input.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.SUBMIT_REG_BUTTON)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login isn't in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form isn't presented"



