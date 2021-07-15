from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class Test_login(BaseTest):

    def test_login_to_app(self):
        self.logintoapp = LoginPage(self.driver)
        self.logintoapp.login_to_app(TestData.username, TestData.password)
