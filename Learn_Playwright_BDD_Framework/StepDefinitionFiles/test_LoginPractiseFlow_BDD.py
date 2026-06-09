import pytest
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios

from Learn_Playwright_BDD_Framework.PageObjects.LoginPagePractise import LoginPagePractise
from Learn_Playwright_BDD_Framework.PageObjects.ShopPage import ShopPage

scenarios(r"C:\Users\JIBISWAS\PycharmProjects\FirstAutomationSetting\Learn_Playwright_BDD_Framework\features\LoginPractiseFlow.feature")


@pytest.fixture()
def shared_data():
    return {}


@given("user navigates to login practice page")
def user_navigates_to_login_practice_page(browser_instance, shared_data):
    login_page_obj = LoginPagePractise(browser_instance)
    login_page_obj.navigate_to_login_practise_page()
    shared_data["login_page_obj"] = login_page_obj
    shared_data["page"] = browser_instance


@when(parsers.parse("user enters username as '{username}' and password as '{password}'"))
def user_enters_credentials(username, password, shared_data):
    login_page_obj = shared_data["login_page_obj"]
    login_page_obj.enter_username(username)
    login_page_obj.enter_password(password)


@when("user selects the user checkbox")
def user_selects_the_user_checkbox(shared_data):
    login_page_obj = shared_data["login_page_obj"]
    login_page_obj.select_user_checkbox()


@when("user selects admin from dropdown")
def user_selects_admin_from_dropdown(shared_data):
    login_page_obj = shared_data["login_page_obj"]
    login_page_obj.select_admin_dropdown()


@when("user selects the confirmation checkbox")
def user_selects_the_confirmation_checkbox(shared_data):
    login_page_obj = shared_data["login_page_obj"]
    login_page_obj.select_confirmation_checkbox()


@when("user clicks the Sign In button")
def user_clicks_the_sign_in_button(shared_data):
    login_page_obj = shared_data["login_page_obj"]
    shop_page_obj = login_page_obj.click_signin_button()
    shared_data["shop_page_obj"] = shop_page_obj


@then("user should be navigated to the shop page")
def user_should_be_navigated_to_the_shop_page(shared_data):
    page = shared_data["page"]
    assert page.url == "https://rahulshettyacademy.com/angularpractice/shop"


@then("user should verify that iPhoneX is displayed on the shop page")
def user_should_verify_iphonex_is_displayed(shared_data):
    shop_page_obj = shared_data["shop_page_obj"]
    assert shop_page_obj.is_iphonx_displayed() == True

