from selenium.webdriver.common.by import By




class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//*[@id="login_form"]')
    REGISTRATION_FORM = (By.XPATH, '//*[@id="register_form"]')


class ProductPageLocators():
    ADD_PRODUCT_LINK = (By.ID, 'add_to_basket_form')
    NOTIFICATION_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]')
    BOOK_TITLE = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1')
    PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    NOTIFICATION_TITLE = (By.XPATH, '//*[@id="messages"]/div[1]/div')
