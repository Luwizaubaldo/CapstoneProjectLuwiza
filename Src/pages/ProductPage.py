from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class ProductPage:
    def __init__(self, driver):  # this method is called when object of the class is created
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # implicity define time sleep

    def search_box(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@type,'search')]"))
            )
            assert submit_button.is_displayed(), "search textbox is not displayed on the page."
            submit_button.send_keys("acer pc")

        except Exception as e:
            print(f"Assertion failed: {e}")

    def add_to_cart(self):
        try:
            add_cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[contains(@type,'submit')])[1]"))
            )
            assert add_cart.is_displayed(), "search textbox is not displayed on the page."
            add_cart.click()
        except Exception as e:
            print(f"Assertion failed: {e}")

