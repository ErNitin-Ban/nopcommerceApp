import pytest
import time
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
from selenium import webdriver


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_AddCustomer(self, setup):
        self.logger.info("************Test_003_Add_customer")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login Successfull*********")

        self.logger.info("**********Starting add Customer List********")
        self.addCustomer = AddCustomer(self.driver)

        self.addCustomer.click_On_Customer_Menu()
        self.addCustomer.click_On_Customer_Menu_item()

        self.addCustomer.click_add_new()

        self.logger.info("*****Add Customer Info *******")
        # self.email = random_generator() + "@gmail.com"
        self.addCustomer.set_email("neal@yah.com")
        self.addCustomer.set_password("test123")
        # self.addCustomer.set_customer_role("Guests")
        self.addCustomer.setManageVendor("Vendor 2")
        self.addCustomer.setGender("Male")
        self.addCustomer.set_first_name("Neil")
        self.addCustomer.set_last_name("Banchanan")
        self.addCustomer.set_dob("9/7/2020")
        self.addCustomer.set_company_name("Developer")
        self.addCustomer.set_admin_content("Testing Automation....")
        self.addCustomer.click_Save()

        self.logger.info("********saving customer info*********")

        self.logger.info("********adding validation*********")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)

        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("******Add Customer test has been Passed**********")

        else:
            self.driver.save_screenshot(".\\Screenshots"+ "test_customer_scr.png")
            self.logger.info("******Add Customer test has been Failed**********")
            assert True == False

        self.driver.close()
        self.logger.info("********Ending Test Case Title Test*********")





def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))