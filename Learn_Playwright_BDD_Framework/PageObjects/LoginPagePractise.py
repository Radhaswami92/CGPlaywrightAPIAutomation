from playwright.sync_api import expect
from Learn_Playwright_BDD_Framework.PageObjects.ShopPage import ShopPage


class LoginPagePractise:

    def __init__(self, page):
        self.page_pr = page

    def navigate_to_login_practise_page(self):
        self.page_pr.goto("https://rahulshettyacademy.com/loginpagePractise/")

    def enter_username(self, username):
        self.page_pr.locator("#username").fill(username)

    def enter_password(self, password):
        self.page_pr.locator("#password").fill(password)

    def select_user_checkbox(self):
        self.page_pr.locator("input[type='checkbox']").first.check()

    def select_admin_dropdown(self):
        # Select the dropdown and choose "Admin" option
        dropdown = self.page_pr.locator("select.form-control")
        dropdown.select_option("Consultant")  # value attribute for Admin option

    def select_confirmation_checkbox(self):
        # Select the checkbox for terms and conditions
        checkboxes = self.page_pr.locator("input[type='checkbox']")
        checkboxes.last.check()

    def click_signin_button(self):
        self.page_pr.locator("#signInBtn").click()
        # Wait for navigation to shop page
        self.page_pr.wait_for_url("**/angularpractice/shop")
        shop_page_obj = ShopPage(self.page_pr)
        return shop_page_obj

    def login_with_credentials(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.select_user_checkbox()
        self.select_admin_dropdown()
        self.select_confirmation_checkbox()
        return self.click_signin_button()

