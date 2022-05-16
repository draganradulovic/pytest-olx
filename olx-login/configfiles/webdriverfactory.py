"""

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

"""
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser2):

        self.browser = browser2

    def getWebDriverInstance(self):

        baseURL = "https://www.olx.ba/"

        if self.browser == "firefox":
            driver=webdriver.Firefox(executable_path=r"C:\Program Files\Mozilladriver\geckodriver.exe")
        elif self.browser == "chrome":
            driver=webdriver.Chrome(executable_path=r"C:\Program Files\Chromedriver\chromedriver.exe")
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
