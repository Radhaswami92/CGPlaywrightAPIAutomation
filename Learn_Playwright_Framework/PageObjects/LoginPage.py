from playwright.sync_api import expect
from Learn_Playwright_Framework.PageObjects.DashboardPage import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page_pr = page

    def navigate_to_loginpage(self):
        self.page_pr.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def login(self, username, password):
        self.page_pr.locator("#userEmail").fill(username)
        self.page_pr.get_by_placeholder("enter your passsword").fill(password)

        self.page_pr.get_by_role("button", name="Login").click()
        expect(self.page_pr.get_by_text(" Login Successfully ")).to_be_visible()
        dashboard_page_obj = DashboardPage(self.page_pr)
        return dashboard_page_obj
