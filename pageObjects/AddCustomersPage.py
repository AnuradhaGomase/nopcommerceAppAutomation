import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer():
    # Add Customer Page Objects
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btn_add_customer_xpath = "//a[@href='/Admin/Customer/Create']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstname_xpath = "//input[@id='FirstName']"
    txt_lastname_xpath = "//input[@id='LastName']"
    btn_genderMale_xpath = "//input[@id='Gender_Male']"
    btn_genderFemale_xpath = "//input[@id='Gender_Female']"
    txt_company_name_xpath = "//input[@id='Company']"
    checkbox_isTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    txt_custRoles_xpath = "//ul[@class='select2-selection__rendered']"
    option_custRoles_Admin_xpath = "//li[contains(text(), 'Administrators')]"
    option_custRoles_ForemMode_xpath = "//li[contains(text(), 'Forum Moderators')]"
    option_custRoles_Registered_xpath = "//li[@class='select2-results__option' and contains(text(), 'Registered')]"
    option_custRoles_Guests_xpath = "//li[contains(text(), 'Guests')]"
    option_custRoles_Vendors_xpath = "//li[contains(text(), 'Vendors')]"
    drp_vendorManager_xpath = "//select[@id='VendorId']"
    # options
    # Not a vendor
    # Vendor 1
    # Vendor 2
    checkbox_activ_xpath = "//input[@id='Active']"
    checkbox_custPwdChange_xpath = "//input[@id='MustChangePassword']"
    txt_admComment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"
    btn_saveCont_xpath = "//button[@name='save-continue']"
    lnk_bckToCustLst_xpath = "//a[normalize-space()='back to customer list']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_add_customer_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastName)

    def selectGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.btn_genderMale_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.btn_genderFemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.btn_genderMale_xpath).click()

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.txt_company_name_xpath).send_keys(companyName)

    def clickTaxExemptCheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_isTaxExempt_xpath).click()

    def selectCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txt_custRoles_xpath).click()
        time.sleep(1)
        if role == "Registered":
            # Registered is selected by default
            # self.driver.find_element(By.XPATH, self.option_custRoles_Registered_xpath).click()
            pass
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.option_custRoles_Admin_xpath).click()
        elif role == "Guests":
            time.sleep(1)
            # Set Guest Role
            self.driver.find_element(By.XPATH, self.option_custRoles_Guests_xpath).click()
            # Remove Registered first to set Guest Role
            # self.driver.find_element(By.CSS_SELECTOR, "#select2-SelectedCustomerRoleIds-result-8pos-3").click()
            self.driver.find_element(By.XPATH, self.option_custRoles_Registered_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.option_custRoles_ForemMode_xpath).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.option_custRoles_Vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.option_custRoles_Guests_xpath).click()
        time.sleep(3)
        # self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectManagerOfVendor(self, mgr):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_vendorManager_xpath))
        drp.select_by_visible_text(mgr)

    def clickActiveCheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_activ_xpath).click()

    def clickCustMstChangePwdCheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_custPwdChange_xpath).click()

    def addAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.txt_admComment_xpath).send_keys(comment)

    def clickSaveBtn(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def clickSaveContBtn(self):
        self.driver.find_element(By.XPATH, self.btn_saveCont_xpath).click()

    def clickOnBckToCustLst(self):
        self.driver.find_element(By.XPATH, self.lnk_bckToCustLst_xpath).click()