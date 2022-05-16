from selenium import webdriver
from pages.login_page import home_page_login
from testing.conftest import *
import pytest
import unittest
from ddt import ddt, unpack, data
from utilities.read_csv import read_from_csv


@pytest.mark.usefixtures("oneTimesetUp1", "setUp1")
@ddt
class login_tests_olx(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classsetUp(self, oneTimesetUp1):
        print("Izvrsio setup")
        self.lp = home_page_login(self.driver)

    @pytest.mark.run(order=1)
    @data(*read_from_csv(r"C:\Users\User\PycharmProjects\letskodeit\utilities\positive_test_data.csv"))
    @unpack
    def test_positive_login(self, name, password):
        self.driver.refresh()
        self.lp.login(name, password)
        result=self.lp.is_loggedin()
        assert result == True

    @pytest.mark.run(order=2)
    @data(*read_from_csv(r"C:\Users\User\PycharmProjects\letskodeit\utilities\negative_test_data.csv"))
    @unpack
    def test_negative_login(self,name, password):
        self.lp.login(name, password)
        result = self.lp.is_loggedin()
        assert result == False
