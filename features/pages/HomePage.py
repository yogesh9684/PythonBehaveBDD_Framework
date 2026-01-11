import time
from selenium.webdriver.common.by import By

from features.pages.Base_Page import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.Registration import Registration


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    My_Account_Xpath = "//span[text()='My Account']"
    Register_Button_Xpath = "//li[@class='dropdown open']//li[1]"
    Login_Button_Xpath = "//li[@class='dropdown open']//li[2]"
    Search_Name = "search"
    Search_Icon_Xpath = "//div[@id='search']//button"
    Product_Link_Text = "HP LP3065"
    Error_Message_text = "//div[@id='content']//p[2]"

    def click_My_Account(self):
        self.clickElement(self.My_Account_Xpath, Locator_type='xpath')
        #self.driver.find_element(By.XPATH, self.My_Account_Xpath).click()

    def click_on_register(self):
        self.clickElement(self.Register_Button_Xpath, Locator_type='xpath')
        #self.driver.find_element(By.XPATH, self.Register_Button_Xpath).click()

    def click_Login(self):
        self.clickElement(self.Login_Button_Xpath, Locator_type='xpath')
        #self.driver.find_element(By.XPATH, self.Login_Button_Xpath).click()
        return LoginPage(self.driver)

    def Search_element(self):
        self.sendKeys("HP", self.Search_Name, Locator_Type='name')
        # self.driver.find_element(By.NAME, self.Search_Name).send_keys("HP")
        time.sleep(5)

    def click_search_button(self):
        self.clickElement(self.Search_Icon_Xpath, Locator_type='xpath')
        #self.driver.find_element(By.XPATH, self.Search_Icon_Xpath).click()
        time.sleep(5)

    Product_Displayed = "HP LP3065"

    def product_displayed(self):
        assert self.Verify_Warning_OR_Error_Messages(self.Product_Link_Text, Locator_Type='link_text',
                                                     Expected_Text="HP LP3065")
        #assert self.isElementPresent(self.Product_Link_Text,Locator_type='link_text')
        #assert self.driver.find_element(By.LINK_TEXT, self.Product_Link_Text).is_displayed()
        time.sleep(2)

    def Invalid_product_search(self):
        self.sendKeys("XRPgddg", self.Search_Name, Locator_Type='name')
        #self.driver.find_element(By.NAME, self.Search_Name).send_keys("XRPgddg")
        time.sleep(5)

    expected_text = 'There is no product that matches the search criteria.'

    def Search_Element_Not_Found(self):
        assert self.Verify_Warning_OR_Error_Messages(self.Error_Message_text, Locator_Type='xpath',
                                                     Expected_Text='There is no product that matches the search criteria.')
        #assert self.driver.find_element(By.XPATH, self.Error_Message_text).text.__eq__(self.expected_text)

    def Blank_search(self):
        self.clickElement(self.Search_Name,Locator_type='name')
        #self.driver.find_element(By.NAME, self.Search_Name).send_keys("")
