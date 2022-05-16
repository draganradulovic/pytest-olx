from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from base.selenium_driver import selenium_actions
import time


class home_page_login(selenium_actions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _login_homepage_button="//*[@id='loginbtn']"
    _ime_field="//*[@id='username']"
    _sifra_field="//*[@id='password']"
    _login_button="//*[@id='btnlogin1']"
    _messages_link="//*[@id='porukel']"

    def open_login_form(self):
        self.get_element(self._login_homepage_button).click()

    def type_name(self, ime):
        self.send_key(ime, self._ime_field)

    def type_password(self, sifra):
        self.send_key(sifra, self._sifra_field)

    def click_login_btn(self):
        self.click(self._login_button)

    def login(self, ime, sifra):
        self.open_login_form()
        self.type_name(ime)
        self.type_password(sifra)
        self.click_login_btn()

    def is_loggedin(self):
        x=self.element_present(self._messages_link)
        return x








