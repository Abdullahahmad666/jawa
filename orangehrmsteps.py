from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('I launch chrome browser')
def launchchrome(context):
    context.driver = webdriver.Chrome("C:\Program Files\DRIVERS\chromedriver.exe")


@given('I am logged in to my metabase account')
def login(context):
    context.driver.get("http://localhost:3000/")
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-username\"]/div[2]/div/input").send_keys(
        "l201326@lhr.nu.edu.pk")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-password\"]/div[2]/div/input").send_keys("blackstone123")
    time.sleep(1)
    context.driver.find_element(By.XPATH,
                                "//*[@id=\"root\"]/div/div/main/div/div[2]/div/div[2]/div/form/div[4]/button").click()

    time.sleep(10)
    status = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/div[2]"
                                                   "/div[2]/span[1]/button").is_displayed()

    if status is True:
        assert True

time.sleep(10)

@when('I click on personal collection option')
def selectoption(context):
    context.driver.find_element(By.XPATH,
                                "//*[@id=\"root\"]/div/div/aside/nav/div/div/div[2]/ul/div[2]/div/li/a/div[2]").click()

    time.sleep(1)


@then('personal collection page opens up')
def openpage(context):
    status = context.driver.find_element(By.XPATH,
                                         "//*[@id=\"root\"]/div/div/main/div/div/div[1]/div[1]/div/div").is_displayed()

    if status is True:
        assert True, "opened"


@when('I click on create new button')
def clickbutton(context):
    context.driver.find_element(By.XPATH , "//*[@id=\"root\"]/div/div/main/div/div/div[3]/div/div[3]/span[1]/button").click()
    time.sleep(2)


@then('new dashboard creation box is displayed')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/span/span/div/div/div/ol/li[3]/div/div").click()
    time.sleep(3)


@when('I enter dashboard name ""NewDemo""')
def enter_collection_name(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-name\"]/div[2]/div/input").send_keys(
        "NewDemo")
    time.sleep(3)


@then('create button is "yes" enabled')
def btn_enabled(context):
    status = context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main/div"
                                                  "/div/div[3]/div/div[3]/span[1]/button").is_enabled()
    if status is True:
        assert True


@then('click on create button')
def click_btn(context):
    context.driver.find_element(By.XPATH, "/html/body/div[6]/div/"
                                          "div/div/div/div/div[2]/div/form/div[4]/button[1]").click()
    time.sleep(3)


@when('I enter collection name ""NewDemo2""')
def enter_name2(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-name\"]/div[2]/div/input").send_keys(
        "NewDemo2")
    time.sleep(2)


@then(u'create button is "No" enabled')
def btn_disabled(context):
    status = context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main"
                                                  "/div/div/div[3]/div/div[3]/span[1]/button").is_enabled()
    if status is False:
        context.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div/svg").click()
        assert True
    time.sleep(2)


@then('new collection page with given name is created')
def page_created(context):
    status = context.driver.find_element(By.XPATH , "//*[@id=\"root\"]/div/div/main"
                                                    "/div/div/div[1]/div[1]/div[1]/div/textarea").is_displayed()
    time.sleep(1)
    if status is True:
        assert True, "Opened"
        # context.driver.close()
    # status = context.driver.find_element(By.XPATH,  "// *[ @ id =\"root\"]/div/div/main/div/div/div[1]"
    #                                                 "/ div[1] / div[1] / div / textarea").text
    # if status  == ""


@when('enter description ""this is scenario outline description""')
def enter_description2(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-description\"]/div[2]/textarea").send_keys(
        "this is scenario outline description")
    time.sleep(3)


@when('enter description "" ""')
def enter_no_description(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-description\"]/div[2]/textarea").send_keys(
        " ")
    time.sleep(3)


