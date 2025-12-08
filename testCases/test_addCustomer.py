import random
import string

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomersPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup_for_login):
        self.logger.info("***** Test_003_AddCustomer *****")
        self.driver = setup_for_login
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Add Customer Test *****")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddNew()

        self.logger.info("***** Providing Customer Info *****")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Anu")
        self.addCust.setLastName("Gor")
        self.addCust.selectGender("Female")
        self.addCust.setCompanyName("Uber")
        self.addCust.clickTaxExemptCheckbox()
        self.addCust.selectCustomerRoles("Guests")
        self.addCust.selectManagerOfVendor("Vendor 1")
        self.addCust.clickActiveCheckbox()
        self.addCust.clickActiveCheckbox()
        self.addCust.clickCustMstChangePwdCheckbox()
        self.addCust.addAdminComment("New test user created")
        self.addCust.clickSaveBtn()
        self.logger.info("***** Saving Customer Info *****")

        self.logger.info("***** Add Customer Validation Started *****")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "customer has been added successfully" in self.msg:
            assert True == True
            self.logger.info("***** Add Customer Test Passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.error("***** Add Customer Test Failed *****")
            assert True == False

        self.driver.close()
        self.logger.info("***** End of Test_003_AddCustomer *****")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))