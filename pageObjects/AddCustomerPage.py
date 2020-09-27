from selenium.webdriver.support.ui import Select
import time

class AddCustomer:

    # Element
    lnkCustomer_menu_xpath = "//a[@href='#']//span[contains(text(), 'Customers')]"
    lnkCustomer_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_firstName_id = "FirstName"
    txt_lastName_id = "LastName"
    rd_Gender_id_Male = "Gender_Male"
    rd_Gender_id_Female = "Gender_Female"
    txt_Dob_id = "DateOfBirth"
    txt_Company_id = "Company"
    txt_AdminComment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"

    #Roles selector element
    txt_customerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lst_itemAdministration_xpath = "//li[contains(text(), 'Administrators')']"
    lst_itemRegistered_xpath = "//li[contains(text(), 'Registered')']"
    lst_itemGuests_xpath = "//li[contains(text(), 'Guests')']"
    lst_itemVendors_xpath = "//li[contains(text(), 'Vendors')']"
    lst_itemForum_Moderators_xpath = "//li[contains(text(), 'Forum Moderators')']"

    #Vendor dropdown
    drpVendor_id = "VendorId"




    #Action method using constructor

    def __init__(self, driver):
        self.driver = driver

    def click_On_Customer_Menu(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_xpath).click()

    def click_On_Customer_Menu_item(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menuitem_xpath).click()

    def click_add_new(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def set_first_name(self, first_name):
        self.driver.find_element_by_id(self.txt_firstName_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_id(self.txt_lastName_id).send_keys(last_name)


    def set_dob(self, dob):
        self.driver.find_element_by_id(self.txt_Dob_id).send_keys(dob)

    def set_company_name(self, company_name):
        self.driver.find_element_by_id(self.txt_Company_id).send_keys(company_name)

    def set_admin_content(self, admin_content):
        self.driver.find_element_by_id(self.txt_AdminComment_id).send_keys(admin_content)

    def click_Save(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()


    # Gender Code

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rd_Gender_id_Male).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rd_Gender_id_Female).click()
        else:
            self.driver.find_element_by_id(self.rd_Gender_id_Male).click()



    # Vendor Code

    def setManageVendor(self, value):
        drp = Select(self.driver.find_element_by_id(self.drpVendor_id))
        drp.select_by_visible_text(value)


    # Roles Code

    def set_customer_role(self,role):
        self.driver.find_element_by_xpath(self.txt_customerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemRegistered_xpath)

        elif role == 'Administrator':
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemAdministration_xpath)

        elif role == 'Guests':
            time.sleep(3)
            #Am remove this because guest and registered cannot be same
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemAdministration_xpath)

        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemVendors_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemGuests_xpath)

        time.sleep(3)
        self.driver.execute_script("argument[0].click()", self.listitem)


