from features.pages.Base_Page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    Input_Email_ID = "input-email"
    Input_Password = "input-password"
    Login_Button_Xpath = "//input[@type='submit']"

    def Enter_UserName(self, email_id):
        self.sendKeys(email_id, self.Input_Email_ID, Locator_Type='ID')
        #self.driver.find_element(By.ID, self.Input_Email_ID).send_keys(email_id)

    def Enter_Password(self, password_id):
        self.sendKeys(password_id, self.Input_Password, Locator_Type='ID')
        #self.driver.find_element(By.ID, self.Input_Password).send_keys(password_id)

    def Click_on_Login(self):
        self.clickElement(self.Login_Button_Xpath, Locator_type='xpath')
        #self.driver.find_element(By.XPATH, self.Login_Button_Xpath).click()

    Error_Message_Xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def Entering_the_Invalid_Username_and_Password_Error_Message(self):
        assert self.Verify_Warning_OR_Error_Messages(self.Error_Message_Xpath, Locator_Type='xpath',
                                                     Expected_Text="Warning: No match for E-Mail Address and/or "
                                                                   "Password.")

        # assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__eq__(
        #     self.expected_error)

    Error_Message = 'Warning: No match for E-Mail Address and/or Password.'
    Error_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    Click_Login_Button = "//input[@type='submit']"

    def Not_Entering_the_username_and_Password(self):
        self.clickElement(self.Click_Login_Button, Locator_type='xpath')
        assert self.Verify_Warning_OR_Error_Messages(self.Error_xpath, Locator_Type='xpath',
                                                     Expected_Text="Warning: No match for E-Mail Address and/or "
                                                                   "Password.")

        # assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__eq__(
        #     self.Error_Message)
