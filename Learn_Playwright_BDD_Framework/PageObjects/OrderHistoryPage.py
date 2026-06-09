from Learn_Playwright_Framework.PageObjects.OrderDetailsPage import OrderDetailsPage
class OrderHistoryPage:

    def __init__(self, page):
        self.page_pr = page

    def navigate_to_order_details_page(self, api_order_id):
        self.page_pr.locator("tbody tr").filter(has_text=api_order_id).get_by_role("button", name="View").click()
        ordr_dtl_page_obj = OrderDetailsPage(self.page_pr)
        return ordr_dtl_page_obj
