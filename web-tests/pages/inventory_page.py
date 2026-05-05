from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def is_loaded(self):
        return self.wait.until(EC.url_contains("inventory"))

    def add_first_product_to_cart(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory"))).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()