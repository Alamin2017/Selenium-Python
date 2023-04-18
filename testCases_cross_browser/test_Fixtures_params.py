import time

import pytest


@pytest.mark.usefixtures("init_driver")
class Test_Google:

    def test_title(self):
        self.driver.get("https://www.google.com/")
        time.sleep(3)
        assert self.driver.title == "Google"
