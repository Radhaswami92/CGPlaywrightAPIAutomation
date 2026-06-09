import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from Learn_Playwright_Framework.PageObjects.LoginPage import LoginPage
from Learn_Playwright_Framework.Utils.apiBaseReadData import ReadAPIUtils

from Learn_Playwright_Framework.Utils.apiBase import APIUtils

with open("Learn_Playwright_Framework/Data/credentials.json") as credential_file:
    test_data = json.load(credential_file)
    cred_data_list = test_data["Credentials"]


@pytest.mark.parametrize("user_credentials", cred_data_list)
def test_login_and_validate_orderId(playwright: Playwright, browser_instance, user_credentials):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = browser_instance
    username = user_credentials["username"]
    password = user_credentials["password"]
    login_payload = {"userEmail": username, "userPassword": password}

    api_base_class_obj = APIUtils()
    api_order_id = api_base_class_obj.create_order_api(playwright, login_payload)

    login_page_obj = LoginPage(browser_instance)
    # login_page_obj.navigate_to_loginpage()
    # execution is getting handling through terminal

    dash_page_obj = login_page_obj.login(username, password)

    order_his_page_obj = dash_page_obj.navigate_to_order_history_page()

    order_dtl_page_obj = order_his_page_obj.navigate_to_order_details_page(api_order_id)

    order_dtl_page_obj.validate_order_id(api_order_id)

    time.sleep(5)


## Terminal COmmands to run the test case in parallel mode and generate html report
# python -m pytest -n 3 --html=Pytest_Reports/Parallel_Execution_Report.html
#pre-requisite (intall the pytest-html using command pip install pytest-html)

with open("Learn_Playwright_Framework/Data/payload.json") as fil_read:
    login_payload = json.load(fil_read)

@pytest.mark.smoke
def test_login_and_validate_products_displayed(playwright: Playwright, browser_instance):
    read_obj = ReadAPIUtils()
    products_list_dashboard = read_obj.get_all_products(playwright)
    api_product_names = []
    for product in products_list_dashboard:
        api_product_names.append(product["productName"])
    print(api_product_names)

    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://rahulshettyacademy.com/client/#/auth/login") ### REPLACED BY BROWSER_INSTANCE_FIXTURE IN CONFTEST.PY

    page = browser_instance

    login_page_obj = LoginPage(page)
    login_page_obj.login(login_payload["userEmail"], login_payload["userPassword"])
    ##### Below replaced by the method navigate

    # page.locator("#userEmail").fill(login_payload["userEmail"])
    # page.get_by_placeholder("enter your passsword").fill(login_payload["userPassword"])
    # page.get_by_role("button", name="Login").click()

    # Below used css regular expression

    expect(page.locator("div[class*='toast-success']")).to_contain_text(" Login Successfully ")

    # had to use .first.wait_for() otherwise all_text_contents() function does not wait for
    page.locator("//div[@class='card-body']/h5/b").first.wait_for()
    ui_product_list = page.locator("//div[@class='card-body']/h5/b").all_text_contents()

    print(ui_product_list)
    assert ui_product_list == api_product_names
