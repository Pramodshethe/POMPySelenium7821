from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    email = (By.ID, "txtUsername")
    password = (By.ID, "txtPassword")
    submitbtn = (By.ID, "btnLogin")
    forgetlink = (By.ID, "forgotPasswordLink")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.URL)

    def login_to_app(self, username, password):
        self.send_keys_on_ele(self.email, username)
        self.send_keys_on_ele(self.password, password)
        self.click_on_ele(self.submitbtn)
