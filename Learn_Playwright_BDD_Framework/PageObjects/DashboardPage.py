from Learn_Playwright_Framework.PageObjects.OrderHistoryPage import OrderHistoryPage
class DashboardPage:

    def __init__(self, page):
        self.page_pr = page


    def navigate_to_order_history_page(self):
        self.page_pr.get_by_role("button", name="ORDERS").click()
        ordr_his_page_obj = OrderHistoryPage(self.page_pr)
        return ordr_his_page_obj
