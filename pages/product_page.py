from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time




class ProductPage(BasePage):
    def add_to_busket(self):
        add_link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_LINK)
        add_link.click()


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NOTIFICATION_TITLE), \
            "Success message is presented, but should not be"


    def succes_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.NOTIFICATION_TITLE), \
            "Succes message should be disappeared"


    def assert_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        notification_text = self.browser.find_element(*ProductPageLocators.NOTIFICATION_PRICE).text
        my_notification = 'Your basket total is now ' + price
        assert notification_text == my_notification('Busket price should be the same as book price')


    def assert_title(self):
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        notification_text = self.browser.find_element(*ProductPageLocators.NOTIFICATION_TITLE).text
        my_notification = title + ' has been added to your basket.'
        assert notification_text == my_notification('Book title in the busket should be the same as added book title')




