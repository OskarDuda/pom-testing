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
        log_out_xpath = "//span[@class='_54nh']"
        log_out_button = self.find_elements(log_out_xpath)[-1]
        self.click(log_out_button)

    def get_login_anchor(self):
        xpath = "//a[@id='pageLoginAnchor']"
        login_anchor = self.find(xpath)
        return login_anchor
