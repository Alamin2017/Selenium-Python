from Configurations.config import TestData

import time
import pytest
from pageObjects.LoginPage2 import LoginPage2

import utilities.CustomLogger as cl


class Test_Bkash:

    log = cl.customLogger()

    # pytest -v -s --alluredir="C:\Users\hp\PycharmProjects\Selenium_Python\allure_report" testCases/test_bkash.py --browser chrome

    def test_bkashurlopen(self, setup):
        self.driver = setup
        self.driver.get(TestData.Bkash_url)
        time.sleep(3)
        self.log.info("bkash url is open")

    def test_hubspot(self, setup):
        self.driver = setup
        self.driver.get(TestData.BASE_URL)
        time.sleep(3)
        self.lp = LoginPage2(self.driver)
        time.sleep(2)
        title = self.lp.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
        time.sleep(2)
        flag = self.lp.is_signup_link_exists()
        assert flag
        time.sleep(2)
        self.lp.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(3)
        self.log.info("test_hubspot test is done")


    def test_title2(self, setup):
        self.driver = setup
        self.driver.get(TestData.BASE_URL)
        time.sleep(3)
        self.lp = LoginPage2(self.driver)
        time.sleep(3)
        title2 = self.lp.get_title__2()
        print(title2)
        assert title2 == TestData.LOGIN_PAGE_TITLE
        self.log.info("test title assertion is done")
