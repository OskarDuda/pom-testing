import json
import string
import random
from unittest import TestCase


class BaseTest(TestCase):
    def setUp(self):
        self.setup_credentials()

    def setup_credentials(self):
        def read(key):
            with open('secret/credentials.json') as f:
                credentials = json.load(f)
            return credentials[key]
        self.email = lambda: read(['email'])
        self.password = lambda: read(['password'])

    @staticmethod
    def random_letters(n):
        characters = string.ascii_letters + string.digits
        return ''.join(random.sample(characters, n))
