from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test_login_positive(self):
        page = LoginPage(self.driver)
        page.log_in(self.email, self.password)

        page = HomePage(self.driver)
        page.log_out()

    def test_login_fails_with_incorrect_password(self):
        wrong_password = lambda: self.random_letters(31)
        page = LoginPage(self.driver)
        self.assertRaises(Exception, page.log_in(self.email, wrong_password))

    def test_login_fails_with_incorrect_email(self):
        wrong_email = lambda: self.random_letters(15) + '@' + self.random_letters(15)
        page = LoginPage(self.driver)
        self.assertRaises(Exception, page.log_in(wrong_email, self.password))

    def test_login_fails_with_incorrect_credentials(self):
        wrong_email = lambda: self.random_letters(15) + '@' + self.random_letters(15)
        wrong_password = lambda: self.random_letters(31)
        page = LoginPage(self.driver)
        self.assertRaises(Exception, page.log_in(wrong_email, wrong_password))
