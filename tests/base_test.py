import json
import string
import random
from unittest import TestCase

from selenium.webdriver import Firefox


class BaseTest(TestCase):
    def setUp(self):
        self.setup_credentials()
        self.setup_driver()

    def tearDown(self):
        self.driver.quit()

    def setup_credentials(self):
        def read(key):
            with open('secret/credentials.json') as f:
                credentials = json.load(f)
            return credentials[key]
        self.email = lambda: read('email')
        self.password = lambda: read('password')

    @staticmethod
    def random_letters(n):
        characters = string.ascii_letters + string.digits
        return ''.join(random.sample(characters, n))

    def setup_driver(self):
        self.driver = Firefox()
