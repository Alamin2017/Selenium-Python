from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        option = Options()
        option.add_argument('--disable-notifications')
        s = Service("E:\Soft\Python_PyCharm\chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=option)
        driver.maximize_window()
        # option = Options()
        # option.add_argument('--disable-notifications')
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=option)
        print("Launching Chrome Browser")
        return driver
    elif browser == 'firefox':
        option = Options()
        option.add_argument("--disable-notifications")
        s = Service("E:\Soft\Python_PyCharm\geckodriver.exe")
        driver = webdriver.Firefox(service=s, options=option)
        driver.maximize_window()
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching Firefox Browser")
        return driver
    else:

        s = Service("E:\Soft\Python_PyCharm\msedgedriver.exe")
        driver = webdriver.Edge(service=s)
        driver.maximize_window()
        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge Browser")
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
