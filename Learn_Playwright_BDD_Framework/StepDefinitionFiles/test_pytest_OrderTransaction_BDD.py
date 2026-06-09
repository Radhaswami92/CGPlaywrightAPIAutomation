import pytest
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios

from Learn_Playwright_BDD_Framework.PageObjects.LoginPage import LoginPage
from Learn_Playwright_BDD_Framework.Utils.apiBase import APIUtils

scenarios(r"C:\Users\JIBISWAS\PycharmProjects\FirstAutomationSetting\Learn_Playwright_BDD_Framework\features\OrderTransaction.feature")


@pytest.fixture()
def shared_data():
    return {}


@given(parsers.parse("the order is placed successfully via API endpoint with {username} and {password}"))
def create_order_via_api(playwright: Playwright, username, password, shared_data):
    login_payload = {"userEmail": username, "userPassword": password}
    api_base_class_obj = APIUtils()
    api_order_id = api_base_class_obj.create_order_api(playwright, login_payload)
    shared_data["login_payload"] = login_payload
    shared_data["api_order_id"] = api_order_id


@given("user lands on login Page")
def user_lands_on_login_page(shared_data, browser_instance):
    login_page_obj = LoginPage(browser_instance)
    shared_data["login_page_obj"] = login_page_obj


@when(parsers.parse("user logs in with {username} and {password}"))
def user_logs_in_with_username_password(username, password, shared_data):
    dash_page_obj = shared_data["login_page_obj"].login(username, password)
    shared_data["dash_page_obj"] = dash_page_obj


@when("navigate to Order History Page")
def navigate_to_Order_History_Page(shared_data):
    order_his_page_obj = shared_data["dash_page_obj"].navigate_to_order_history_page()
    shared_data["order_his_page_obj"] = order_his_page_obj


@when("user select the order and navigates to order details page")
def user_select_the_order_and_navigates_to_order_details_page(shared_data):
    order_details_page = shared_data["order_his_page_obj"].navigate_to_order_details_page(shared_data["api_order_id"])
    shared_data["order_dtl_page_obj"] = order_details_page


@then("user sucessfully validates the order id in the UI")
def user_sucessfully_validates_the_order_id_in_the_UI(shared_data):
    shared_data["order_dtl_page_obj"].validate_order_id(shared_data["api_order_id"])
