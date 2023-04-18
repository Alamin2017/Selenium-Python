from Configurations.config import TestData
from pageObjects.ShareBusPage import ShareBusPage
import time
import utilities.CustomLogger as cl


class Test_ShareBus:

    log = cl.customLogger()

    def test_just(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(TestData.ShareBus_url)
        self.log.info("url is open")
        time.sleep(2)
        self.lp = ShareBusPage(self.driver)
        self.lp.ClickSignInButton()
        self.log.info("click signin button")
        time.sleep(2)
        self.lp.enterEmail(TestData.username)
        self.log.info("Enter username")
        time.sleep(2)
        self.lp.enterPass(TestData.password)
        self.log.info("Enter Password")
        time.sleep(3)
        self.lp.clickLoginInButton()
        self.log.info("click submit button")
        time.sleep(10)
        self.driver.close()
