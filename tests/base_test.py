import json
import string
import random
from unittest import TestCase


class BaseTest(TestCase):
    def setUp(self):
        self.setup_credentials()

    def setup_credentials(self):
        with open('secret/credentials.json') as f:
            credentials = json.load(f)
        self.email = credentials['email']
        self.password = credentials['password']

    @staticmethod
    def random_letters(n):
        characters = string.ascii_letters + string.digits
        return ''.join(random.sample(characters, n))
