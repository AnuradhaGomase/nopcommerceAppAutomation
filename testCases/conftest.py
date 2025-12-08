from selenium import webdriver
from seleniumbase import Driver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    return driver

@pytest.fixture()
def setup_for_login():
    driver = Driver(uc=True, browser='chrome')
    return driver

#################################### To get browser from command line at run time ######################################

def pytest_addoption(parser):       #this will gate value from CLI or hooks
    parser.addoption("--mybrowser")

@pytest.fixture()
def browser(request):               #this will return the Browser value to setup method
    return request.config.getoption("--mybrowser")


#################################### PyTest HTML Reports #######################################
from pytest_metadata.plugin import metadata_key

# hook for adding env info into report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Nop Commerce'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['Tester'] = 'Anaa'

# hook for delete/modify env info in report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop("Plugins", None)