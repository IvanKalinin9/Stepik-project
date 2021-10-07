from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math
import time




class ProductPage(BasePage):
    def add_to_busket(self):
        add_link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_LINK)
        add_link.click()



    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def assert_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        notification_text = self.browser.find_element(*ProductPageLocators.NOTIFICATION_PRICE).text
        my_notification = 'Your basket total is now ' + price
        assert notification_text == my_notification

    def assert_title(self):
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        notification_text = self.browser.find_element(*ProductPageLocators.NOTIFICATION_TITLE).text
        my_notification = title + ' has been added to your basket.'
        assert notification_text == my_notification




