import time
from behave import *
from features.pages.Account import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I am on the Login Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_My_Account()
    context.login_page = context.home_page.click_Login()

@when(u'I Enter the Username as "{email}" and Password as "{password}"')
def step_impl(context, email, password):
    #context.login_page = LoginPage(context.driver)
    context.login_page.Enter_UserName(email)
    context.login_page.Enter_Password(password)


@when(u'Clicked on Login Button')
def step_impl(context):
    context.login_page.Click_on_Login()
    time.sleep(3)


@then(u'Logged In Successfully Message will be displayed')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    context.account_page.After_Login_Message()


@when(u'I Enter the invalid Username as "{email}" and Invalid Password as "{password}"')
def step_impl(context, email, password):
    #context.login_page = LoginPage(context.driver)
    context.login_page.Enter_UserName(email)
    context.login_page.Enter_Password(password)


@then(u'Proper Error Message will be displayed')
def step_impl(context):
    #context.login_page = LoginPage(context.driver)
    context.login_page.Entering_the_Invalid_Username_and_Password_Error_Message()


@when(u'I don\'t Enter any UserName and Password"')
def step_impl(context):
    #context.login_page = LoginPage(context.driver)
    context.login_page.Click_on_Login()
    context.login_page.Not_Entering_the_username_and_Password()
