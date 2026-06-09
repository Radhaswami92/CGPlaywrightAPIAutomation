from playwright.sync_api import Page, Playwright, expect

from Learn_Playwright_Automation_Udemy.Utils.apiBase import APIUtils


def test_storing_token_in_browser_local_storage(playwright: Playwright):
    obj_token = APIUtils()
    login_token = obj_token.log_in_api_get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    browser_context=browser.new_context()
    page = browser_context.new_page()
    page.add_init_script(f"""localStorage.setItem('token', '{login_token}')""")
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/myorders")
    expect(page.get_by_text("Your Orders")).to_be_visible()
    name_index = 0
    for index in range (0, page.locator("table thead tr th").count()):
        if page.locator("table thead tr th").nth(index).filter(has_text="Name").count() > 0:
            name_index = index
            break
    i= 0
    while i < page.locator("table tbody tr").count():
        if page.locator("table tbody tr").nth(i).locator("td").nth(name_index-1).text_content() == "ADIDAS ORIGINAL":
            assert page.locator("table tbody tr").nth(i).locator("th").text_content() == "69bbf6c8f86ba51a651459e0"
            break
        i += 1
