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

@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", cred_data_list)
def test_login_and_validate_orderId(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login_payload = {"userEmail": user_credentials["username"], "userPassword": user_credentials["password"]}

    api_base_class_obj = APIUtils()
    api_order_id = api_base_class_obj.create_order_api(playwright, login_payload)

    login_page_obj = LoginPage(page)
    login_page_obj.navigate_to_loginpage()

    page.locator("#userEmail").fill(user_credentials["username"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["password"])

    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text(" Login Successfully ")).to_be_visible()

    page.get_by_role("button", name="ORDERS").click()

    page.locator("tbody tr").filter(has_text=api_order_id).get_by_role("button", name="View").click()
    expect(page.locator("body")).to_contain_text("Thank you for Shopping With Us")
    expect(page.locator(".col-md-6").filter(has_text="Order Id").locator(".col-text.-main")).to_contain_text(
        api_order_id)
    time.sleep(5)


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
