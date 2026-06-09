import requests
AUTH_TOKEN = ""
USER_ID = ""

class CommonRequest:
    def __init__(self, endpoint, **kwargs):
        self.__endpoint=endpoint
        self.__header_dictionary ={"Content-Type": "application/json", **kwargs}

    def request_spec(self, method, **kwargs):
        base_url = "https://rahulshettyacademy.com"
        url = base_url + self.__endpoint
        session = requests.Session()
        response = session.request(method =method, url=url, json=kwargs, headers = self.__header_dictionary)
        return response.json()



    def req_login_spec_api(self):
        global AUTH_TOKEN
        global USER_ID
        obj_common_req = CommonRequest("///api/ecom/auth/login")

        response_dict = obj_common_req.request_spec("post", userEmail="jeet.zaper@gmail.com",
                                                    userPassword="Radhaswami@103")

        AUTH_TOKEN = response_dict["token"]
        USER_ID = response_dict["userId"]

        print(response_dict)
    


def test_get_orders_page_data():
    response_dict =login_request_specification("/api/ecom/auth/login", userEmail="jeet.zaper@gmail.com",
                                userPassword="Radhaswami@103")

    response = requests.get(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/"+USER_ID,
                  headers={"Content_Type":"application/json", "Authorization":AUTH_TOKEN})

    response_dict_order= response.json()
    return response_dict_orde





