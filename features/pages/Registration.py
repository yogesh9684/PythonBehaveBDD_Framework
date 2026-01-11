import time
from datetime import datetime

from selenium.webdriver.common.by import By

from features.pages.Base_Page import BasePage


class Registration(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    First_Name = "input-firstname"
    Last_Name = "input-lastname"
    Email_Address = "input-email"
    Telephone = "input-telephone"
    Password = "input-password"
    Confirm_Password = "input-confirm"
    I_Agree_Checkbox = "//input[@name='agree']"
    Register_Button = "//input[@type='submit']"
    Register_Successful_Message_Text = "//div[@id='content']//p[1]"
    User_already_Exist_Message = "//div[@class='alert alert-danger alert-dismissible']"
    # Warning Message
    First_Name_Warning_Xpath = "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    Last_Name_Warning_Xpath = "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    Email_Address_Warning_Xpath = "//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    Telephone_Warning_Xpath = "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"
    Password_Warning_Xpath = "//div[contains(text(),'Password must be between 4 and 20 characters!')]"
    Privacy_Policy_Xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def Enter_FirstName(self):
        self.sendKeys("Arjun",self.First_Name,Locator_Type='id')
        #self.driver.find_element(By.ID, self.First_Name).send_keys('Arjun')

    def Enter_FirstName_Empty(self):
        self.sendKeys("",self.First_Name,Locator_Type='id')
        #self.driver.find_element(By.ID, self.First_Name).send_keys('')

    def Enter_LastName(self):
        self.sendKeys("Mahabharata",self.Last_Name,Locator_Type='id')
        #self.driver.find_element(By.ID, self.Last_Name).send_keys('Mahabharata')

    def Enter_LastName_Empty(self):
        self.sendKeys("",self.Last_Name,Locator_Type='id')
        #self.driver.find_element(By.ID, self.Last_Name).send_keys('')

    def Enter_EmailAddress(self):
        # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%H_%S")
        # new_email = "test" + time_stamp + "@gmail.com"
        self.sendKeys("test968_20@test.com",self.Email_Address,Locator_Type='id')
        # new_email="test9684@test.com"
        # self.driver.find_element(By.ID, self.Email_Address).send_keys(new_email)

    def Enter_EmailAddress_Empty(self):
        self.sendKeys("",self.Email_Address,Locator_Type='id')
        #self.driver.find_element(By.ID, self.Email_Address).send_keys('')

    def Enter_Telephone(self):
        self.sendKeys("9822962617",self.Telephone,Locator_Type='id')
        #self.driver.find_element(By.ID, self.Telephone).send_keys('9822962617')

    def Enter_Telephone_Empty(self):
        self.sendKeys("",self.Telephone,Locator_Type='id')
        #self.driver.find_element(By.ID, self.Telephone).send_keys('')

    def Enter_password(self):
        self.sendKeys("123456",self.Password,Locator_Type='id')
        #self.driver.find_element(By.ID, self.Password).send_keys('123456')

    def Enter_password_Empty(self):
        self.sendKeys("",self.Password,Locator_Type='id')
        #self.driver.find_element(By.ID, self.Password).send_keys('')

    def Enter_Confirm_Password(self):
        self.sendKeys("123456",self.Confirm_Password,Locator_Type='id')
        #self.driver.find_element(By.ID, self.Confirm_Password).send_keys('123456')

    def Enter_Confirm_Password_Empty(self):
        self.sendKeys("",self.Confirm_Password,Locator_Type='id')
        #self.driver.find_element(By.ID, self.Confirm_Password).send_keys('')

    def Click_I_Agree_Checkbox(self):
        self.clickElement(self.I_Agree_Checkbox,Locator_type='xpath')
        #self.driver.find_element(By.XPATH, self.I_Agree_Checkbox).click()

    def Click_on_Register_Button(self):
        self.clickElement(self.Register_Button,Locator_type='xpath')
        #self.driver.find_element(By.XPATH, self.Register_Button).click()

    Success_Message = "Congratulations! Your new account has been successfully created!"

    def Register_Successful_Message(self):
        assert self.Verify_Warning_OR_Error_Messages(self.Register_Successful_Message_Text,Locator_Type='xpath',Expected_Text="Congratulations! Your new account has been successfully created!")
        # assert self.driver.find_element(By.XPATH, self.Register_Successful_Message_Text).text.__contains__(
        #     self.Success_Message)

    Already_Exist = "Warning: E-Mail Address is already registered!"

    def User_Already_Exist(self):
        assert self.Verify_Warning_OR_Error_Messages(self.User_already_Exist_Message, Locator_Type='xpath',
                                                     Expected_Text="Warning: E-Mail Address is already registered!")
        #assert self.driver.find_element(By.XPATH, self.User_already_Exist_Message).text.__contains__(self.Already_Exist)

    Expected_First_Name_Warning = "First Name must be between 1 and 32 characters!"

    def First_Name_Warning(self):
        assert self.Verify_Warning_OR_Error_Messages(self.First_Name_Warning_Xpath, Locator_Type='xpath',
                                                     Expected_Text="First Name must be between 1 and 32 characters!")
        # assert (self.driver.find_element(By.XPATH, self.First_Name_Warning_Xpath).text.__contains__(
        #     self.Expected_First_Name_Warning))

    Expected_Last_Name_Warning = "Last Name must be between 1 and 32 characters!"

    def Last_Name_Warning(self):
        assert self.Verify_Warning_OR_Error_Messages(self.Last_Name_Warning_Xpath, Locator_Type='xpath',
                                                     Expected_Text="Last Name must be between 1 and 32 characters!")

        # assert (self.driver.find_element(By.XPATH, self.Last_Name_Warning_Xpath).text.__contains__(
        #     self.Expected_Last_Name_Warning))

    Expected_Email_Address_Warning = "E-Mail Address does not appear to be valid!"

    def Email_address_Warning(self):
        assert self.Verify_Warning_OR_Error_Messages(self.Email_Address_Warning_Xpath, Locator_Type='xpath',
                                                     Expected_Text="E-Mail Address does not appear to be valid!")

        # assert (self.driver.find_element(By.XPATH, self.Email_Address_Warning_Xpath).text.__contains__(
        #     self.Expected_Email_Address_Warning))

    Expected_Telephone_Warning = "Telephone must be between 3 and 32 characters!"

    def Telephone_Warning(self):
        assert self.Verify_Warning_OR_Error_Messages(self.Telephone_Warning_Xpath, Locator_Type='xpath',
                                                     Expected_Text="Telephone must be between 3 and 32 characters!")

        # assert (self.driver.find_element(By.XPATH, self.Telephone_Warning_Xpath).text.__contains__(
        #     self.Expected_Telephone_Warning))

    Expected_Password_Warning = "Password must be between 4 and 20 characters!"

    def Password_Warning(self):
        assert self.Verify_Warning_OR_Error_Messages(self.Password_Warning_Xpath, Locator_Type='xpath',
                                                     Expected_Text="Password must be between 4 and 20 characters!")

        # assert (self.driver.find_element(By.XPATH, self.Password_Warning_Xpath).text.__contains__(
        #     self.Expected_Password_Warning))

    Privacy_Error_Message = "Warning: You must agree to the Privacy Policy!"

    def Privacy_policy(self):
        assert self.Verify_Warning_OR_Error_Messages(self.Privacy_Policy_Xpath, Locator_Type='xpath',
                                                     Expected_Text="Warning: You must agree to the Privacy Policy!")

        # assert self.driver.find_element(By.XPATH, self.Privacy_Policy_Xpath).text.__contains__(
        #     self.Privacy_Error_Message)
