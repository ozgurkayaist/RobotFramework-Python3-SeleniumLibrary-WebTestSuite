from PageObjectLibrary import PageObject

from robot.libraries.BuiltIn import BuiltIn


class BasketPage(PageObject):
    PAGE_TITLE = "Sepetim"
    PAGE_URL = "/ayagina-gelsin/sepetim"

    _locators = {
        "product_element": "xpath=//span[contains(@class, 'PriceComponent')]",
        "add_basket_element": "id=addToCart",
        "my_basket_element": "id=shoppingCart",
        "submit_basket_items_button": "xpath=//*[@id='short-summary']/div[1]/div[2]/button",
        "submit_delivery_button": "xpath=//*[@id='short-summary']/div[1]/div[2]/button",
    }

    def adds_a_homepage_product_to_basket(self):
        with self._wait_for_page_refresh():
            self.select_product()
            self.add_to_basket()
            self.driver.get("https://www.hepsiburada.com" + self.PAGE_URL)

    def navigate_to_credit_card_checkout_page(self):
        with self._wait_for_page_refresh():
            self.submit_basket_items()
            self.submit_delivered_items()

    def select_product(self):
        self.selib.click_element(self.locator.product_element)

    def add_to_basket(self):
        self.selib.click_element(self.locator.add_basket_element)

    def submit_basket_items(self):
        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.submit_basket_items_button)

    def submit_delivered_items(self):
        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.submit_delivery_button)

