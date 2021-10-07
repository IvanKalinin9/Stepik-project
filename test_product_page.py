from pages.product_page import ProductPage



def test_can_quest_add_product_to_busket(browser):
    link = 'ttp://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.solve_quiz_and_get_code()


