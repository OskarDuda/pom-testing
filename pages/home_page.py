from pages.base_page import BasePage


class HomePage(BasePage):
    def get_top_bar(self):
        xpath = "//div[@id='js_7']"
        top_bar = self.find(xpath)
        return top_bar

    def get_home_page_button(self):
        xpath = "//div[@id='u_0_f']"
        parent = self.get_top_bar()
        home_page_button = self.find_child(parent, xpath)
        return home_page_button

    def log_out(self):
        dropdown_button = self.get_login_anchor()
        self.click(dropdown_button)
        log_out_xpath = "//div[@aria-label='Konto']//div[@role='button']"
        log_out_button = self.wait_elements_visible(log_out_xpath)[-2]
        self.click(log_out_button)

    def get_login_anchor(self):
        # xpath = "//a[@id='pageLoginAnchor']"
        xpath = "//div[@aria-label='Konto']"
        login_anchor = self.find(xpath)
        return login_anchor
