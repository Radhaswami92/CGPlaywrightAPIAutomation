from playwright.sync_api import Page
def test_playwright_shortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")