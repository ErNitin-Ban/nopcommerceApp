#for py test always test cases name start with test eg : test_Login
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    # baseUrl = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"

#Now we getting the hardcoded values using readproperties.py file
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("***************Test_001_Login***************")
        self.logger.info("***************Verify Home page title***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_Title = self.driver.title

        if act_Title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***************homePageTitle is passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("***************homePageTitle is Failed***************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***************test_login started***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        #Create an object to call class of LoginPage from Page Object class
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title


        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************test_login started Passed***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("***************test_login Failed***************")
            assert False






