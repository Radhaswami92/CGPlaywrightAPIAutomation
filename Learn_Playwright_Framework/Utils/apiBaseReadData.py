import json

from playwright.sync_api import Playwright

get_all_product_payload ={"productName": "","minPrice": "null","maxPrice": "null","productCategory": [],"productSubCategory": "","productFor": []}

base_url="https://rahulshettyacademy.com"

with open("Learn_Playwright_Framework/Data/payload.json") as file_read:
    Login_Payload = json.load(file_read)


class ReadAPIUtils:


    def login_api_token(self, pwrght:Playwright):
        api_request_context = pwrght.request.new_context(base_url=base_url, ignore_https_errors=True)
        login_api_response = api_request_context.post(url="/api/ecom/auth/login",
                                                      data=Login_Payload,
                                                      headers={"content-type": "application/json"})
        response_dict= login_api_response.json()
        login_message = response_dict["message"]
        assert login_message == "Login Successfully"
        token = response_dict["token"]
        return token


    def get_all_products(self, playrght:Playwright):
        api_request_context = playrght.request.new_context(base_url=base_url, ignore_https_errors=True)
        token = self.login_api_token(playrght)
        get_product_api_response = api_request_context.post(url="/api/ecom/product/get-all-products",
                                                      data=get_all_product_payload,
                                                      headers={"authorization":token,
                                                               "content-type":"applicaion/json"})
        response_dict = get_product_api_response.json()
        assert response_dict["message"] == "All Products fetched Successfully"
        return response_dict["data"]
