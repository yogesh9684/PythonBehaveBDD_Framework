import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from Utilities import ConfigReader
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration('basic info', 'url'))
    context.driver.implicitly_wait(10)


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
        name="failed_screenshot", attachment_type=allure.attachment_type.PNG)
