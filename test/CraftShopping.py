import time
import unittest
from selenium.webdriver.common.by import By

from Src.pages.LandingPage import LandingPage
from Src.pages.LoginPage import LoginPage
from Src.pages.OrderPage import OrderPage
from Src.pages.RegPage import RegPage
from Src.pages.CartPage import CartPage
from Src.pages.ProductPage import ProductPage

class TestLoin(unittest.testcase):
    def setup(self):
        self.driver = getBrowser()
        self.driver.get("https://shop.icraft.net:8095/")
        self.landing_page = landingPage(self.driver)
        self.landing_page = LoginPage(self.driver)
        self.landing_page = OrderPage(self.driver)
        self.landing_page = RegPage(self.driver)
        self.landing_page = cartPage(self.driver)
        self.landing_page = ProductPage(self.driver)

        def tearDown(self):
            self.driver.quit()

        def test_Regstration(self):
            self.LandingPage.click_login()
