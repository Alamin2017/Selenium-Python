from Configurations.config import TestData
from pageObjects.ShareBusPage import ShareBusPage
import time


class Test_ShareBus:

    def test_just(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(TestData.ShareBus_url)
        time.sleep(2)
        self.lp = ShareBusPage(self.driver)
        self.lp.ClickSignInButton()
        self.lp.enterEmail("brainstation23@yopmail.com")
        self.lp.enterPass("Pass@1234")
        time.sleep(3)
        self.lp.clickLoginInButton()
        time.sleep(10)
        self.driver.close()
