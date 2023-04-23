import time


class Test_Google:
    # pytest -v -s testCases_browser_setup/test_google.py

    def test_fixture(self, setup):
        self.driver = setup
        self.driver.get("https://www.google.com/")
        print("Test fixture is done")
        time.sleep(3)
        assert self.driver.title == "Google"
        self.driver.close()

    def test_browser(self, setup):
        self.driver = setup
        self.driver.get("https://www.facebook.com/")
        time.sleep(3)
        self.driver.close()
