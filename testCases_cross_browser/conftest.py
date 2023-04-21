from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=['chrome', 'edge', 'firefox'], scope='class')
def init_driver(request):
    if request.param == "chrome":
        # option = Options()
        # option.add_argument('--disable-notifications')
        # s = Service("E:\Soft\Python_PyCharm\chromedriver.exe")
        # driver = webdriver.Chrome(service=s, options=option)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        request.cls.driver = driver

    elif request.param == "edge":
        # s = Service("D:\2021Project\msedgedriver.exe")
        # driver = webdriver.Edge(service=s)
        # driver.maximize_window()
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver.maximize_window()
        request.cls.driver = driver
    elif request.param == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        request.cls.driver = driver

    request.cls.driver = driver
    yield
    driver.quit()
