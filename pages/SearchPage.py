from PageObjectLibrary import PageObject


class SearchPage(PageObject):
    """Keywords for the Home page of the demo app

    There are no keywords defined for this page. However, by
    creating this empty page object we can still use the
    PageObjectLibrary keywords "Go to page" and "The current
    page should be"
    """

    PAGE_TITLE = "bluetooth kulaklık - Hepsiburada"
    PAGE_URL = "/ara?q=bluetooth+kulaklık"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
        "search_input": "id=productSearch",
        "search_button": "id=buttonProductSearch",
        "filter_brand_element": "xpath=//*[@placeholder='Marka ara']",
        "filter_brand_option_element": "xpath=//*[@title='JBL']",
        "filter_price_min_element": "xpath=//*[@placeholder='En az']",
        "filter_price_max_element": "xpath=//*[@placeholder='En çok']",
        "filter_price_submit_element": "xpath=//*[contains(@class, 'range-contain-row right')]",
        "filter_color_element": "xpath=//*[@title='Siyah']",
        "product_image_element": "xpath=//*[contains(@class, 'product-image-wrapper')]",
    }

    def user_searches_for(self, searchtext):
        with self._wait_for_page_refresh():
            self.selib.input_text(self.locator.search_input, searchtext)
            self.selib.click_button(self.locator.search_button)

    def filter_search_results_with_brand(self, brandtext):
        with self._wait_for_page_refresh():
            self.selib.scroll_element_into_view(self.locator.filter_brand_element)
            self.selib.input_text(self.locator.filter_brand_element, brandtext)
            self.selib.click_element(self.locator.filter_brand_option_element)

    def filter_search_results_with_price_between(self, price_min_text, price_max_text):
        with self._wait_for_page_refresh():
            self.selib.scroll_element_into_view(self.locator.filter_price_min_element)
            self.selib.input_text(self.locator.filter_price_min_element, price_min_text)
            self.selib.input_text(self.locator.filter_price_max_element, price_max_text)
            self.selib.click_element(self.locator.filter_price_submit_element)

    def filter_search_results_with_color(self, colortext):
        with self._wait_for_page_refresh():
            self.selib.scroll_element_into_view(self.locator.filter_color_element)
            self.selib.click_element(self.locator.filter_color_element)

    def choose_a_product_from_filtered_results_and_open_comments_tab(self):
        with self._wait_for_page_refresh():
            self.selib.click_element(self.locator.product_image_element)