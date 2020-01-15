from PageObjectLibrary import PageObject


class CheckoutPage(PageObject):
    """Keywords for the Home page of the demo app

    There are no keywords defined for this page. However, by
    creating this empty page object we can still use the
    PageObjectLibrary keywords "Go to page" and "The current
    page should be"
    """

    PAGE_TITLE = "Ödeme Bilgileri"
    PAGE_URL = "/ayagina-gelsin/odeme"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
    }