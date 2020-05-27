from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TIMEOUT = 10


class BasePage:
    def __init__(self, driver=Firefox()):
        self.driver = driver
        self.driver.get('https://www.facebook.com')

    def type_in(self, text, element):
        element.send_keys(text)

    def click(self, element):
        element.click()

    def find(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_elements(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def find_child(self, parent, xpath):
        parent.find_element_by_xpath(xpath)

    def wait_element_visible(self, xpath, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element

    def wait_elements_visible(self, xpath, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        return element
