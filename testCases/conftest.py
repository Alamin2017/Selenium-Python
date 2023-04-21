from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='class')
def setup():
    browser = "chrome"
    if browser == "chrome":
        # option = Options()
        # option.add_argument('--disable-notifications')
        # s = Service("E:\Soft\Python_PyCharm\chromedriver.exe")
        # driver = webdriver.Chrome(service=s, options=option)
        # driver.maximize_window()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        print("Launching Chrome Browser")
        return driver
    elif browser == 'firefox':
        # s = Service("E:\Soft\Python_PyCharm\geckodriver.exe")
        # driver = webdriver.Firefox(service=s)
        # driver.maximize_window()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        print("Launching Firefox Browser")
        return driver

    elif browser == 'edge':
        # s = Service("E:\Soft\Python_PyCharm\msedgedriver.exe")
        # driver = webdriver.Edge(service=s)
        # driver.maximize_window()
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver.maximize_window()
        print("Launching Edge Browser")
        return driver

def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")
