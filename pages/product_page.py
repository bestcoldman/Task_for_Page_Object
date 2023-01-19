from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_can_add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()

    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text


    def should_be_add_to_basket(self):
        self.should_be_message()
        self.should_be_right_price()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def verify_message_added_product_name_to_basket(self):
        message_pname = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_FOR_PRODUCT)
        assert self.get_product_name() == message_pname.text, "Book wasn't added to cart"

    def verify_message_product_price_to_basket(self):
        message_pprice = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_WITH_PRICE)
        assert self.get_product_price() == message_pprice.text, "Incorrect product price in cart"

    def should_be_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADDBASKET_BUTTON).click()

    def should_be_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        print(product_name, message)
        assert message == product_name, f"{product_name} is not {message}"

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(product_price, basket_price)
        assert product_price == basket_price, f"{product_price} not equal {basket_price}"

    def message_should_be_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Message isn't dissapeared after adding product to basket"





