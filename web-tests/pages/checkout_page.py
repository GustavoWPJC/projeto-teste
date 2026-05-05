from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        return self.wait.until(EC.url_contains("checkout-step-one"))

    def fill_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def finish(self):
        self.wait.until(EC.url_contains("checkout-step-two"))
        self.driver.find_element(By.ID, "finish").click()

    def is_complete(self):
        return self.wait.until(EC.url_contains("checkout-complete"))