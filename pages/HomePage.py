from PageObjectLibrary import PageObject


class HomePage(PageObject):
    """Keywords for the Home page of the demo app

    There are no keywords defined for this page. However, by
    creating this empty page object we can still use the
    PageObjectLibrary keywords "Go to page" and "The current
    page should be"
    """

    PAGE_TITLE = "Türkiye'nin En Büyük Online Alışveriş Sitesi Hepsiburada.com"
    PAGE_URL = "/"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
    }
