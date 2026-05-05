import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

USERNAME = os.getenv("LOGIN_USER")
PASSWORD = os.getenv("LOGIN_PASSWORD")


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    brave_path = "/usr/bin/brave-browser"
    if os.path.exists(brave_path):
        options.binary_location = brave_path

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


class TestCheckout:

    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(USERNAME, PASSWORD)

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_loaded()

    def test_add_product_to_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(USERNAME, PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_first_product_to_cart()
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        assert cart_page.is_loaded()
        assert cart_page.has_items()

    def test_complete_checkout(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(USERNAME, PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_first_product_to_cart()
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(driver)
        assert checkout_page.is_loaded()
        checkout_page.fill_info("Gustavo", "Silva", "12345")

        driver.save_screenshot("screenshot.png")

        checkout_page.finish()
        assert checkout_page.is_complete()