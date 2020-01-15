from PageObjectLibrary import PageObject
import unittest
from unittest import TestCase


class ProductPage(PageObject, unittest.TestResult):
    """Keywords for the Home page of the demo app

    There are no keywords defined for this page. However, by
    creating this empty page object we can still use the
    PageObjectLibrary keywords "Go to page" and "The current
    page should be"
    """

    PAGE_TITLE = "JBL Tune T220 TWS Bluetooth Kulaklık - Siyah Fiyatı"
    PAGE_URL = "/jbl-tune-t220-tws-bluetooth-kulaklik-siyah-p-HBV00000P435S"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
        "productReviewsTab_element": "id=productReviewsTab",
        "review_yes_element": "xpath=//*[contains(@class, 'yes backToTopVisible')]",
    }

    def mark_a_comment_as_helpful(self):
        self.selib.scroll_element_into_view(self.locator.productReviewsTab_element)
        self.selib.click_element(self.locator.productReviewsTab_element)
        self.selib.click_element(self.locator.review_yes_element)


