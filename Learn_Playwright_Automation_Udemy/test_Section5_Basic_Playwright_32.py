import time

from playwright.sync_api import Page


def test_playwright_sign_in(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name ="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)

