import random
import time

import pytest
import string
from faker import Faker
from playwright.sync_api import Playwright, expect


@pytest.fixture(scope="module")
def generate_username():
    fake = Faker()
    genusername = fake.name()
    return genusername


@pytest.fixture(scope="module")
def generate_password():
    fake = Faker()
    password = fake.password(length=16, special_chars=False, digits=True, upper_case=True, lower_case=True)
    return password


@pytest.fixture(scope="module")
def generate_email():
    fake = Faker()
    email = fake.email()
    return email


@pytest.fixture(scope="module")
def generate_phonenumber():
    digits = string.digits
    ph_no_list = random.choices(digits, k=10)
    phone_number = "".join(ph_no_list)
    return phone_number


def test_new_registration_client_portal(playwright: Playwright, generate_username, generate_password, generate_email,
                                        generate_phonenumber):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/register")
    #spl_user_name = generate_username.split(" ")
    first_name = generate_username.split(" ")[0]
    last_name = generate_username.split(" ")[1]
    page.get_by_placeholder("First Name").fill(first_name)
    page.get_by_placeholder("Last Name").fill(last_name)
    NewUsername = generate_email
    page.get_by_placeholder("email@example.com").fill(NewUsername)
    page.locator("#userMobile").fill(generate_phonenumber)
    page.get_by_role("combobox").select_option("3: Engineer")
    #page.locator(".mt-3.ng-valid.ng-dirty.ng-touched").click()
    page.get_by_text("Male", exact=True).click()
    NewPassword = generate_password
    page.locator("#userPassword").fill(NewPassword)
    page.locator("#confirmPassword").fill(NewPassword)
    page.get_by_role("checkbox").check()
    page.locator("input.ng-untouched.ng-pristine.ng-invalid")
    expect(page.get_by_role("checkbox")).to_be_checked()
    page.get_by_role("button", name="Register").click()
    expect(page.locator("body")).to_contain_text("Account Created Successfully")
    Email_Password=[NewUsername, NewPassword]
    with open("Playwright_New_User_Credentials.txt", 'a') as text_file:
        for item in Email_Password:
            if "@" in item:
                text_file.write(f"Username: {item}\n")
            else:
                text_file.write(f"Password: {item}\n")
        text_file.write("\n")
        text_file.write("\n")

    time.sleep(5)

