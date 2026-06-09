import pytest
from playwright.sync_api import Playwright

from Learn_Playwright_Framework.PageObjects.LoginPage import LoginPage


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my defined browser name"
    )
    parser.addoption(
        "--url_name", action="store", default="staging", help="define the default server"
    )

@pytest.fixture()
def browser_instance(playwright: Playwright, request):
    browser_n = request.config.getoption("browser_name")
    environment = request.config.getoption("url_name")
    if browser_n == "chrome":
        browser = playwright.chromium.launch(headless=True)
    elif browser_n == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        # Prevents UnboundLocalError by creating a default browser instance
        browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    if environment == "staging":
        print("Navigating through fixture")
        page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    elif environment == "pac":
        print("Navigating through PageObjects")
        obj_login = LoginPage(page)
        obj_login.navigate_to_loginpage()
    else:
        page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    yield page
    context.close()
    browser.close()
