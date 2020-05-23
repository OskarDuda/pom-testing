from pages.base_page import BasePage


class LoginPage(BasePage):
    def get_email_input(self):
        xpath = "//input[@id='email']"
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def get_password_input(self):
        xpath = "//input[@id='pass']"
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def get_log_in_button(self):
        xpath = "//label[@id='loginbutton']"
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def log_in(self, email, password):
        email_input_box = self.get_email_input()
        password_input_box = self.get_password_input()
        log_in_button = self.get_log_in_button()
        self.type_in(email(), email_input_box)  # TODO implement lazy email
        self.type_in(password(), password_input_box)  # TODO implement lazy password
        self.click(log_in_button)
