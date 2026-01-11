import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Custom_Logger import customLogger as cl


class BasePage:

    def __init__(self, driver):
        self.log = None
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    #log = cl.customLogger(logging.DEBUG)

    def getByType(self, Locator_Type):
        Locator_Type = Locator_Type.lower()

        if Locator_Type == 'id':
            return By.ID

        elif Locator_Type == 'xpath':
            return By.XPATH

        elif Locator_Type == 'class_name':
            return By.CLASS_NAME

        elif Locator_Type == 'name':
            return By.NAME

        elif Locator_Type == 'css_selector':
            return By.CSS_SELECTOR

        elif Locator_Type == 'link_text':
            return By.LINK_TEXT

        elif Locator_Type == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT

        else:
            print("Locator_Type" + Locator_Type + "Not Supported")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")

        return element

    # def getElement(self, Locator, Locator_Type="id"):
    #     try:
    #         LocatorType = Locator_Type.lower()
    #         byType = self.getByType(LocatorType)
    #         element = self.driver.find_element(byType, Locator)
    #         self.log.info("Got the Element ")
    #     except:
    #         self.log.error("Element Not found ")
    #     return element

    def isElementPresent(self, Locator, Locator_type='xpath'):
        try:
            element = self.getElement(Locator, Locator_type)
            if element is not None:
                print("Element Is present")
            else:
                print("Element is not present")
        except:
            print("Element is Not Present. Try Searching Different")

    def clickElement(self, Locator, Locator_type='xpath'):
        global element
        try:
            element = self.getElement(Locator, Locator_type)
            element.click()
            print("Clicked on  Element")
        except:
            print("Element is not present")
        return element

    def sendKeys(self, data, Locator, Locator_Type='id'):
        try:
            element = self.getElement(Locator, Locator_Type)
            element.send_keys(data)
            print("Data Sent on Element")
        except:
            print("Failed to send data on Element")

    def Verify_Title(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
            print("Title Found")
            return self.driver.title
        except:
            print("Title Not Found")

    def get_element_text(self, locator, Locator_Type):
        try:
            element = self.getElement(locator, Locator_Type)
            print(" Captured the Text")
            return element.text
        except:
            print("Failed to Capture Text")

    def Verify_Warning_OR_Error_Messages(self, locator, Locator_Type, Expected_Text):
        try:
            element = self.getElement(locator, Locator_Type)
            print(" Captured the Text")
            return element.text.__contains__(Expected_Text)
        except:
            print("Failed to Capture Text")
