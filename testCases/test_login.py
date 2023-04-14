import time

from pageObjects.LoginPage import LoginPage



class Test_001_login:

    # terminal test run
    # pytest -v -s testCases/test_login.py
    # pytest -v -s testCases/test_login.py --browser chrome
    # pytest -v -s --html=results/my_report.html testCases/test_login.py --browser chrome
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get("http://admin-demo.nopcommerce.com")
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            assert False

    def test_login(self, setup):

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get("http://admin-demo.nopcommerce.com")
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        # self.lp.setUserName(self.username)
        self.lp.setUserName("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.clickLogin()
        act_title1 = self.driver.title
        if act_title1 == "Dashboard / nopCommerce administration":
            assert True
            time.sleep(3)
            self.lp.clickLogout()
            time.sleep(3)
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_page_title.png")
            assert False
