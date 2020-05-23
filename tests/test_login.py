from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test_positive_login(self):
        LoginPage.log_in(self.email, self.password)
        HomePage.log_out()

    def test_negative_login(self):
        wrong_email = self.random_letters(15) + '@' + self.random_letters(15)
        wrong_password = self.random_letters(31)
        self.assertRaises(LoginPage.log_in(self.email, wrong_password))
        self.assertRaises(LoginPage.log_in(wrong_email, self.password))
        self.assertRaises(LoginPage.log_in(wrong_email, wrong_password))
