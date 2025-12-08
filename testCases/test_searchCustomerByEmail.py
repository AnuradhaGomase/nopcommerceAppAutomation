import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomersPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup_for_login):
        self.logger.info("***** Test_004_SearchCustomerByEmail *****")
        self.driver = setup_for_login
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Search Customer By Email Test *****")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.logger.info("***** Searching customer by email ID *****")
        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.setEmail("brenda_lindgren@nopCommerce.com")
        self.searchCust.clickSearchBtn()
        time.sleep(1)
        status = self.searchCust.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        assert True == status
        self.logger.info("***** Test_004_SearchCustomerByEmail Finished *****")
        self.driver.close()
