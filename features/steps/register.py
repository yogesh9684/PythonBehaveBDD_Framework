import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from features.pages.HomePage import HomePage
from features.pages.Registration import Registration

options = Options()
options.add_argument("--log-level=3")  # Suppress most logs
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service("E:\\browser_drivers\\chromedriver.exe"), options=options)
options.add_argument("--no-sandbox")


@when(u'I Enter all the Valid Details into the Register Page')
def step_impl(context):
    #Opening_from_Home_Page
    context.home_page = HomePage(context.driver)
    context.home_page.click_My_Account()
    time.sleep(3)
    context.home_page.click_on_register()
    #Opening_Registration_page
    context.registration_page = Registration(context.driver)
    time.sleep(3)
    context.registration_page.Enter_FirstName()
    context.registration_page.Enter_LastName()
    context.registration_page.Enter_EmailAddress()
    context.registration_page.Enter_Telephone()
    context.registration_page.Enter_password()
    context.registration_page.Enter_Confirm_Password()
    context.registration_page.Click_I_Agree_Checkbox()

@when(u'Then I click on Register Button')
def step_impl(context):
    context.registration_page = Registration(context.driver)
    context.registration_page.Click_on_Register_Button()
    time.sleep(10)

@then(u'Register Successful Message will be displayed')
def step_impl(context):
    context.registration_page = Registration(context.driver)
    context.registration_page.Register_Successful_Message()

@then(u'User already exist message will be displayed')
def step_impl(context):
    context.registration_page = Registration(context.driver)
    context.registration_page.User_Already_Exist()

@when(u'I do not enter any mandatory details on the Registration page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_My_Account()
    context.home_page.click_on_register()
    # Opening_Registration_page
    context.registration_page = Registration(context.driver)
    context.registration_page.Enter_FirstName_Empty()
    context.registration_page.Enter_LastName_Empty()
    context.registration_page.Enter_EmailAddress_Empty()
    context.registration_page.Enter_Telephone_Empty()
    context.registration_page.Enter_password_Empty()
    context.registration_page.Enter_Confirm_Password_Empty()
    context.registration_page.Click_I_Agree_Checkbox()


@then(u'Error Message will be displayed to user')
def step_impl(context):
    context.registration_page = Registration(context.driver)
    context.registration_page.First_Name_Warning()
    context.registration_page.Last_Name_Warning()
    context.registration_page.Email_address_Warning()
    context.registration_page.Telephone_Warning()
    context.registration_page.Password_Warning()

@when(u'I do not enter any mandatory details on the Registration page and privacy policy')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_My_Account()
    context.home_page.click_on_register()
    # Opening_Registration_page
    context.registration_page = Registration(context.driver)
    context.registration_page.Enter_FirstName_Empty()
    context.registration_page.Enter_LastName_Empty()
    context.registration_page.Enter_EmailAddress_Empty()
    context.registration_page.Enter_Telephone_Empty()
    context.registration_page.Enter_password_Empty()
    context.registration_page.Enter_Confirm_Password_Empty()


@then(u'Privacy Error Message will be displayed to User')
def step_impl(context):
    context.registration_page = Registration(context.driver)
    context.registration_page.Privacy_policy()