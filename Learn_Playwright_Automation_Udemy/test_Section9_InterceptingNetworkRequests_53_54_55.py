import time

from playwright.sync_api import Page, expect
No_order_payload= {"data":[],"message":"No Orders"}
No_products_payload= {"data":[], "count":0, "message":""}

def intercept_url(route):

    route.fulfill(
        json=No_order_payload
    )


def test_validate_network_interception_order_page(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_url)
    page.get_by_placeholder("email@example.com").fill("jeet.zaper@gmail.com")
    page.locator("#userPassword").fill("Radhaswami@103")
    page.get_by_role("button", name="Login").click()
    #below using xpath
    expect(page.locator("//div[@aria-label='Login Successfully']")).to_be_visible()
    page.get_by_role("button", name="ORDERS").click()
    expect(page.locator(".mt-4.ng-star-inserted")).to_contain_text("You have No Orders to show at this time.")


def intercept_network_product_display_page_url(route):
    route.fulfill(
        json=No_products_payload
    )


def test_validate_network_interception_product_display_home_page(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.route("https://rahulshettyacademy.com/api/ecom/product/get-all-products", intercept_network_product_display_page_url)
    page.get_by_placeholder("email@example.com").fill("jeet.zaper@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Radhaswami@103")
    page.get_by_text("Login").click()
    expect(page.locator("//div[@aria-label='Login Successfully']")).to_be_visible()
    time.sleep(10)

def intercept__request_for_order_different_user(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69e797b6f86ba51a6579d7bb")

def test_validate_authorization_of_order_with_different_user_id(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept__request_for_order_different_user)
    page.get_by_placeholder("email@example.com").fill("jeet.zaper@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Radhaswami@103")
    page.get_by_text("Login").click()
    expect(page.locator("//div[@aria-label='Login Successfully']")).to_be_visible()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    expect(page.locator(".blink_me")).to_contain_text("you are not authorize to view this order", ignore_case=True)
    time.sleep(10)