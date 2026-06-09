from playwright.sync_api import expect


class OrderDetailsPage:

    def __init__(self, page):
        self.page_pr = page


    def validate_order_id(self, api_order_id):
        expect(self.page_pr.locator("body")).to_contain_text("Thank you for Shopping With Us")
        expect(self.page_pr.locator(".col-md-6").filter(has_text="Order Id").locator(".col-text.-main")).to_contain_text(
            api_order_id)