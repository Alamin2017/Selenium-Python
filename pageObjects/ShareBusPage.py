import time
from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class ShareBusPage(BasePage):
    signInButton = (By.XPATH, "//button[normalize-space()='Sign in']")
    Email = (By.XPATH, "//input[@id='email']")
    Pass = (By.XPATH, "//input[@id='password']")
    logInButton = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def ClickSignInButton(self):
        self.do_click(self.signInButton)

    def enterEmail(self, username):
        self.do_send_keys(self.Email, username)

    def enterPass(self, password):
        self.do_send_keys(self.Pass, password)

    def clickLoginInButton(self):
        self.do_click(self.logInButton)
