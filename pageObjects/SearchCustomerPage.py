from selenium.webdriver.common.by import By

class SearchCustomer:
    txt_email_id = "SearchEmail"
    txt_firstname_id = "SearchFirstName"
    txt_lastname_id = "SearchLastName"
    txt_company_id = "SearchCompany"
    btn_search_id = "search-customers"

    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']/tbody/tr"
    table_cols_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setFirstname(self, firstname):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lastname)

    def setCompany(self, company):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_company_id).send_keys(company)

    def clickSearchBtn(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getNoOfCols(self):
        return len(self.driver.find_elements(By.XPATH, self.table_cols_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table_email = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]").text
            if table_email == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table_name = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[3]").text
            if table_name == name:
                flag = True
                break
        return flag

