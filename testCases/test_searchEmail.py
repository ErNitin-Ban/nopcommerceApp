import time
import pytest
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.search_Customer import searchCustomer
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_search_CustomerByEmail_004():
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByEmail(self, setup):
        self.logger.info("**********search customer by email 004*************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login successfull***********")

        # self.logger("***********starting search customer by email************")

        self.addCustomer = AddCustomer(self.driver)

        self.addCustomer.click_On_Customer_Menu()
        self.addCustomer.click_On_Customer_Menu_item()



        self.logger.info("*********search by email id***********")

        sercCustomer = searchCustomer(self.driver)
        sercCustomer.setEmail("brenda_lindgren@nopCommerce.com")
        sercCustomer.submitClick()
        time.sleep(5)

        status = sercCustomer.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        assert True == status
        self.logger.info("*********TC SEARCH CUSTOMER BY EMAIL finished.......")


