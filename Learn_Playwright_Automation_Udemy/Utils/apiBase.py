from playwright.sync_api import Playwright

login_payload = {"userEmail": "jeet.zaper@gmail.com", "userPassword": "Radhaswami@103"}
create_order_payload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}




class APIUtils:

    def log_in_api_get_token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)
        api_login_response = api_request_context.post("/api/ecom/auth/login",
                                                      data=login_payload,
                                                      headers={"content-type": "application/json",
                                                               })
        assert api_login_response.ok
        response_dict = api_login_response.json()
        assert response_dict["message"] == "Login Successfully"
        return response_dict["token"]

    def create_order_api(self, pwr: Playwright):
        token = self.log_in_api_get_token(pwr)
        createorder_api_request_context = pwr.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)
        create_order_response = createorder_api_request_context.post("/api/ecom/order/create-order",
                                                                     data=create_order_payload,
                                                                     headers={"Content-type": "application/json",
                                                                              "Authorization": token}
                                                                     )
        print(create_order_response.json())
        response_dict = create_order_response.json()
        assert response_dict["message"] == "Order Placed Successfully"
        return response_dict["orders"][0]


