class searchCustomer():
    #Add Customer page
   txt_email_Id = "SearchEmail"
   txt_fName_Id = "SearchFirstName"
   txt_lName_Id = "SearchLastName"
   txt_submitBtn_Id = "search-customers"
    #Table xpaths
   tblSearch_ResultXpath = "//table[@role='grid']"
   table_Xpath = "//table[@id='customers-grid']"
   tblRowXpath = "//table[@id='customers-grid']//tbody/tr"
   tblColumnXpath = "//table[@id='customers-grid']//tbody/tr/td"

   def __init__(self,driver):
       self.driver = driver

   def setEmail(self,email):
       self.driver.find_element_by_id(self.txt_email_Id).clear()
       self.driver.find_element_by_id(self.txt_email_Id).send_keys(email)

   def setFname(self,fname):
       self.driver.find_element_by_id(self.txt_fName_Id).clear()
       self.driver.find_element_by_id(self.txt_fName_Id).send_keys(fname)

   def setLname(self,lname):
       self.driver.find_element_by_id(self.txt_lName_Id).clear()
       self.driver.find_element_by_id(self.txt_lName_Id).send_keys(lname)

   def submitClick(self):
       self.driver.find_element_by_id(self.txt_submitBtn_Id).click()

   def getNoOfRows(self):
       return len(self.driver.find_elements_by_xpath(self.tblRowXpath))

   def getNoOfColumns(self):
       return len(self.driver.find_elements_by_xpath(self.tblColumnXpath))


   def searchCustomerByEmail(self,email):
       flag = False
       for r in range(1, self.getNoOfRows()+1):
           table = self.driver.find_element_by_xpath(self.table_Xpath)
           emailId = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text

           if emailId == email:
               flag = True
               break
       return flag


   def searchCustomerByName(self,Name):
       flag = False
       for r in range(1, self.getNoOfRows()+1):
           table = self.driver.find_element_by_xpath(self.table_Xpath)
           name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
           if name == Name:
               flag = True
               break
       return flag