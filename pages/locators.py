from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    PASSWORD_REPEAT = (By.NAME, "registration-password2")
    SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET = (By. CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
    ADDBASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE_FOR_PRODUCT = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    SUCCESS_MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    VIEW_BASKET = (By.XPATH, "//a[text()='View basket']")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty.')]")

