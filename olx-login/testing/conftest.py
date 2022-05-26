from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from configfiles.webdriverfactory import WebDriverFactory

@pytest.fixture(scope="class")
def oneTimesetUp1(request, browser2):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser2)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


@pytest.fixture()
def setUp1():
    print("Before every method")

    yield
    print("After every method")

def pytest_addoption(parser):
    parser.addoption("--browser2")

@pytest.fixture(scope="session")
def browser2(request):
    return request.config.getoption("--browser2")

