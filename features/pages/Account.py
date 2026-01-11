from selenium.webdriver.common.by import By
from features.pages.Base_Page import BasePage


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    exp_text = "Edit your account information"
    After_Login_Expected_Text_xpath="//div[@id='content']/ul[1]/li[1]/a"

    def After_Login_Message(self):
        assert self.Verify_Warning_OR_Error_Messages(self.After_Login_Expected_Text_xpath,Locator_Type='xpath',Expected_Text="Edit your account information")
        #assert self.driver.find_element(By.XPATH,self.After_Login_Expected_Text_xpath ).text.__eq__(self.exp_text)


