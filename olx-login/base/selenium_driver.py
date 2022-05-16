from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import utilities.custom_logger as cl
import logging


class selenium_actions():

    log=cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def byType(self,tip):
        tip=tip.lower()
        if tip == 'xpath':
            return By.XPATH
        elif tip == 'id':
            return By.ID
        elif tip == 'name':
            return By.NAME

    def get_element(self, locator, byt='xpath'):
        type=self.byType(byt)
        element=self.driver.find_element(type, locator)
        return element


    def send_key(self, key, locator, byt='xpath'):
        by=self.byType(byt)
        element = self.get_element(locator, byt)
        element.send_keys(key)


    def click(self, locator, byt='xpath'):
        by=self.byType(byt)
        element = self.get_element(locator, by)
        element.click()

    def element_present(self, locator):
        try:
            element=self.get_element(locator)
            if element is not None:
                self.log.info("Element found")
                return True
        except:
            self.log.info("Element not found")
            return False


