from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Products is in the basket, but should not be"

    def should_be_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), "'...basket is empty' is not in message, but should be"