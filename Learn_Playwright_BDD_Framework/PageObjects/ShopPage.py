from playwright.sync_api import expect


class ShopPage:

    def __init__(self, page):
        self.page_pr = page

    def is_iphonx_displayed(self):
        """
        Verify that iPhone X is displayed on the shop page
        Returns True if iPhone X is found, False otherwise
        """
        # Look for the iPhone X product in the page
        iphone_element = self.page_pr.locator("//h4[contains(text(), 'iPhoneX')]")

        # Using expect to verify it's visible
        try:
            expect(iphone_element).to_be_visible()
            return True
        except AssertionError:
            return False

    def verify_product_exists(self, product_name):
        """
        Generic method to verify if a product exists on the shop page
        """
        product_locator = self.page_pr.locator(f"//h4[contains(text(), '{product_name}')]")
        expect(product_locator).to_be_visible()

