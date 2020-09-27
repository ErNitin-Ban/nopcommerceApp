#for py test always test cases name start with test eg : test_Login
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_Login:
    # baseUrl = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"

#Now we getting the hardcoded values using readproperties.py file
    baseUrl = ReadConfig.getApplicationUrl()
    path = ".//TestData/LoginData.xlsx"
    # username = ReadConfig.getUsername() #No need because it will came from excel
    # password = ReadConfig.getPassword() #No need because it will came from excel

    logger = LogGen.loggen()



    def test_login_ddt(self,setup):
        self.logger.info("***************test_login started DDT test***************")
        self.logger.info("***************test_login started***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        #Create an object to call class of LoginPage from Page Object class
        self.lp = Login(self.driver)

        #excel utils code

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows in excel", self.rows)

        lst_status = [] #Empty List variable we need to create
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"


            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**********DDT Test is Passed**********")
                    self.lp.clickLogout()

                    lst_status.append("Pass")
                    time.sleep(5)

                elif self.exp == "Fail":
                    self.logger.info("**********DDT Test Case Failed**********")
                    lst_status.append("Fail")
                    self.driver.close()
                    time.sleep(5)


        #     elif act_title != exp_title: #Negative Test Case Code
        #         if self.exp == "Pass":
        #             self.logger.info("**********DDT Test is Failed**********")
        #             self.lp.clickLogout()
        #             lst_status.append("Fail")
        #
        #         elif self.exp == "Fail":
        #             self.logger.info("**********DDT Test Case Passed**********")
        #             self.lp.clickLogout()
        #             lst_status.append("Pass")
        #
        # if "Fail" not in lst_status:
        #     self.logger.info("Login DDT Test Passed")
        #     self.driver.close()
        #     assert True
        #
        # else:
        #     self.logger.info("Login DDT is Failed")
        #     self.driver.close()
        #     assert False












