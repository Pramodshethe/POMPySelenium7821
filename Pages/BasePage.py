from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_ele(self, locater):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locater)).click()

    def send_keys_on_ele(self, locater, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locater)).send_keys(text)
