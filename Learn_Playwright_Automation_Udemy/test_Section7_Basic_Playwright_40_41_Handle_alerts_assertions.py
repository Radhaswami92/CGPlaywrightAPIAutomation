import time

from playwright.sync_api import Page, expect


def test_playwright_assertions(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)


def test_playwright_handle_alerts(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("#confirmbtn").click()
    time.sleep(5)


def test_playwright_handle_frames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page_frame_1 = page.frame_locator("#courses-iframe")
    page_frame_1.get_by_role("link", name="All Access plan").click()
    expect(page_frame_1.locator("body")).to_contain_text("All Access Subscription")
    time.sleep(5)