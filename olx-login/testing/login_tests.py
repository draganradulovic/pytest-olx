from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import home_page_login
from testing.conftest import *
import sys
import pytest
import unittest
import time


@pytest.mark.usefixtures("oneTimesetUp1", "setUp1")
class login_tests_olx(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classsetUp(self, oneTimesetUp1):
        print("Izvrsio setup")
        self.lp = home_page_login(self.driver)

    @pytest.mark.run(order=2)
    def test_positive_login(self):
        self.driver.refresh()
        self.lp.login("QAtestingOnly", "testtest789")
        result=self.lp.is_loggedin()
        assert result == True

    @pytest.mark.run(order=1)
    def test_negative_login(self):
        self.lp.login("dragan", "123789")
        result = self.lp.is_loggedin()
        assert result == False
