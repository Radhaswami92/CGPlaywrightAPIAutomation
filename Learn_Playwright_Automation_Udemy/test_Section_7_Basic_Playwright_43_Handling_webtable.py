import time

from playwright.sync_api import Page, expect


def test_handle_web_table_validate_price_rice(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    PriceColIndex = 0
    for index in range(0, page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            PriceColIndex = index
            break
    rice_row = page.locator("tr").filter(has_text="Rice").locator("td").nth(PriceColIndex).text_content()
    #assertion 1
    assert rice_row == "37"
    # assertion 2
    expect(page.locator("tr").filter(has_text="Rice").locator("td").nth(PriceColIndex)).to_have_text("37")

def test_element_hover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    time.sleep(5)
    page.get_by_role("link", name="Top").click()


## use this command to play and record and get the playwright code auto-generated for the web application
## python -m playwright codegen https://rahulshettyacademy.com/AutomationPractise
