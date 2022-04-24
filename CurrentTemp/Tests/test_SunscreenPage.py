from Pages.SunscreenPage import SunscreenPage
from Tests import test_CartPage
from Tests.test_base import BaseTest
import pytest


class test_SunscreenPage(BaseTest):

    def __init__(self):
        self.sunscreen_page = SunscreenPage(self.driver)

    def test_sunscreen_page_displayed(self):
        assert self.sunscreen_page.get_visibility_of_sunscreen_page_header()

    def test_information_button_present(self):
        assert self.sunscreen_page.get_visibility_of_instructions_button()

    def test_cart_button_present(self):
        assert self.sunscreen_page.get_visibility_of_cart_button()

    def test_add_buttons_present(self):
        assert self.sunscreen_page.get_visibility_of_add_buttons()

    def test_add_products(self):
        self.sunscreen_page.select_products()
        next_page = test_CartPage
        public_methods = [method for method in dir(next_page) if callable(getattr(next_page, method))]
        for method in public_methods:
            getattr(next_page, method)
