import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from Learn_Playwright_Framework.PageObjects.LoginPage import LoginPage
from Learn_Playwright_Framework.Utils.apiBaseReadData import ReadAPIUtils

from Learn_Playwright_Framework.Utils.apiBase import APIUtils

with open("Learn_Playwright_BDD_Framework/Data/credentials.json") as credential_file:
    test_data = json.load(credential_file)
    cred_data_list = test_data["Credentials"]


@pytest.mark.parametrize("user_credentials", cred_data_list)
def test_login_and_validate_orderId(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    username = user_credentials["username"]
    password = user_credentials["password"]
    login_payload = {"userEmail": username, "userPassword": password}

    api_base_class_obj = APIUtils()
    api_order_id = api_base_class_obj.create_order_api(playwright, login_payload)

    login_page_obj = LoginPage(page)
    login_page_obj.navigate_to_loginpage()

    dash_page_obj = login_page_obj.login(username, password)

    order_his_page_obj = dash_page_obj.navigate_to_order_history_page()

    order_dtl_page_obj = order_his_page_obj.navigate_to_order_details_page(api_order_id)

    order_dtl_page_obj.validate_order_id(api_order_id)

    time.sleep(5)

    context.close()


def test_login_and_validate_products_displayed(playwright: Playwright):
    read_obj = ReadAPIUtils()
    products_list_dashboard = read_obj.get_all_products(playwright)
    api_product_names = []
    for product in products_list_dashboard:
        api_product_names.append(product["productName"])
    print(api_product_names)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator("#userEmail").fill("jeet.zaper@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Radhaswami@103")
    page.get_by_role("button", name="Login").click()
    # Below used css regular expression
    expect(page.locator("div[class*='toast-success']")).to_contain_text(" Login Successfully ")
    # had to use .first.wait_for() otherwise all_text_contents() function does not wait for
    page.locator("//div[@class='card-body']/h5/b").first.wait_for()
    ui_product_list = page.locator("//div[@class='card-body']/h5/b").all_text_contents()

    print(ui_product_list)
    assert ui_product_list == api_product_names
