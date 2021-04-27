from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link") #теперь каждый селектор — это пара: как искать и что искать.
