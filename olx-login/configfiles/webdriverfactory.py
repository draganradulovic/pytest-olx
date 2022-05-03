"""

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

"""

from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser2):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser2

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://www.olx.ba/"

        if self.browser == "firefox":
            driver=webdriver.Firefox(executable_path=r"C:\Program Files\Mozilladriver\geckodriver.exe")
        elif self.browser == "chrome":
            driver=webdriver.Chrome(executable_path=r"C:\Program Files\Chromedriver\chromedriver.exe")
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver