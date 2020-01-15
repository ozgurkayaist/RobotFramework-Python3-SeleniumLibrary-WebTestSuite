from PageObjectLibrary import PageObject

from robot.libraries.BuiltIn import BuiltIn


class LoginPage(PageObject):
    PAGE_TITLE = "Üye Giriş Sayfası – Hepsiburada.com"
    PAGE_URL = "/uyelik/giris?ReturnUrl=%2f"

    _locators = {
        "username": "id=email",
        "password": "id=password",
        "submit_button": "xpath=//*[@id='form-login']/div[4]/button",
    }

    def user_logs_in_with_credentials(self, username, password):
        #config = BuiltIn().get_variable_value("${CONFIG}")
        self.enter_username(username)
        self.enter_password(password)
        with self._wait_for_page_refresh():
            self.click_the_submit_button()

    def enter_username(self, username):
        """Enter the given string into the username field"""
        self.selib.input_text(self.locator.username, username)

    def enter_password(self, password):
        """Enter the given string into the password field"""
        self.selib.input_text(self.locator.password, password)

    def click_the_submit_button(self):
        """Click the submit button, and wait for the page to reload"""
        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.submit_button)