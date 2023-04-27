import time

import pytest


@pytest.mark.usefixtures("init_driver")
class Test_Google:


    def test_title(self):

        self.driver.get("https://www.facebook.com/")
        time.sleep(3)
        # assert self.driver.title == "Google"

    def test_print_2(self):
        self.driver.get("https://github.com/")
        time.sleep(3)
