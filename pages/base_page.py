from selenium.webdriver import Firefox


class BasePage:
    def __init__(self, driver=Firefox()):
        self.driver = driver

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
