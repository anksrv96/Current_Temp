import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.Basepage import Basepage


class SunscreenPage(Basepage):
    CART_BUTTON = (By.CSS_SELECTOR, "thin-text nav-link")
    SUNSCREEN_PAGE_HEADER = (By.TAG_NAME, "h2")
    PRODUCT_LIST = [(By.CSS_SELECTOR, "font-weight-bold top-space-10")]
    PRICES = [(By.CLASS_NAME, "font-weight-bold top-space-10")]
    INSTRUCTIONS = (By.CSS_SELECTOR, "octicon octicon-info")
    ADD_BUTTONS = [(By.CLASS_NAME, "btn btn-primary")]

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_sunscreen_page_title(self, title):
        return self.get_title(title)

    def get_visibility_of_sunscreen_page_header(self):
        return self.is_visible(self.SUNSCREEN_PAGE_HEADER)

    def get_visibility_of_instructions_button(self):
        return self.is_visible(self.INSTRUCTIONS)

    def select_products(self):
        prod_list = []
        price_list = []

        final_prod_list =[]
        for product in self.PRODUCT_LIST:
            prod_list.append(product.text)

        for price in price_list:
            price_list.append(price[:-3])

        product_map = dict(zip(prod_list, price_list))

        for key in product_map:
            if product_map.get(key).contains("SPF-50"):
                self.do_click(By.XPATH, "/html/body/div[1]/div[2]/div[1]/button")
                self.do_click(By.XPATH, "/html/body/div[1]/div[3]/div[1]/button")

    def get_visibility_of_cart_button(self):
        return self.is_visible(self.CART_BUTTON)

    def get_visibility_of_add_buttons(self):
        flag = True
        for button in self.ADD_BUTTONS:
            if self.is_visible(button):
                continue
            else:
                flag = False
        return flag





