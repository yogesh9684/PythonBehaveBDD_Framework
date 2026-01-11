from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from features.pages.HomePage import HomePage

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.set_capability("goog:loggingPrefs", {"browser": "SEVERE"})
driver = webdriver.Chrome(service=Service("E:\\browser_drivers\\chromedriver.exe"), options=options)


@given(u'I am on the WebPage')
def step_impl(context):
    pass

@when(u'User enters the Valid Product on Search Bar')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.Search_element()


@when(u'User clicks on Search button')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_search_button()


@then(u'Application Displays the Product Matching the Search Criteria')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.product_displayed()


@when(u'User enters the InValid Product on Search Bar')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.Invalid_product_search()


@then(u'Application Displays the Error Message Search Not found')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.Search_Element_Not_Found()

@when(u'User do not enter anything on search bar')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.Blank_search()
