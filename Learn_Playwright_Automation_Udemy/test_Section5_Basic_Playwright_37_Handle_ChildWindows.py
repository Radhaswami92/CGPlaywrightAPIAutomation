import time

from playwright.sync_api import Page, expect


def test_playwright_sign_in(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    ##css_selector(Tagname-appcard)
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    black_berry_product = page.locator("app-card").filter(has_text="Blackberry")
    black_berry_product.get_by_role("button").click()

    page.get_by_text("Checkout").click()

    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)


def test_handle_child_windows_and_validate_email(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_window:
        page.locator(".blinkingText").get_by_text("Free Access").click()
        child_page = new_window.value
        val_text = child_page.locator(".im-para.red").text_content()
        print(val_text)
        ## assertion1
        expect(child_page.locator(".im-para.red")).to_contain_text("mentor@rahulshettyacademy.com")
        #expect(val_text).to_contain_text("mentor@rahulshettyacademy.com")
        email = val_text.split("at")[1].split("with")[0].strip()
        print(email)
        ##assertion2
        assert email == "mentor@rahulshettyacademy.com"
        time.sleep(5)




