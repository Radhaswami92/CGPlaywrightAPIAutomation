import requests
import responses
from lxml.html.diff import token
AUTH_TOKEN = ""
USER_ID = ""

def login_request_specification(endpoint, **kwargs):
    global AUTH_TOKEN
    global USER_ID
    base_url = "https://rahulshettyacademy.com"
    header = {"Content-Type": "application/json"}
    response = requests.post(url = base_url+endpoint, json= kwargs, headers=header)
    response_dict = response.json()
    AUTH_TOKEN = response_dict["token"]
    USER_ID = response_dict["userId"]

    return response_dict


def get_orders_page_data():
    response_dict =login_request_specification("/api/ecom/auth/login", userEmail="jeet.zaper@gmail.com",
                                userPassword="Radhaswami@103")

    response = requests.get(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/"+USER_ID,
                  headers={"Content_Type":"application/json", "Authorization":AUTH_TOKEN})

    response_dict_order= response.json()
    return response_dict_order

@responses.activate
def test_mock_orders_page():

    responses.add(responses.get, url="https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/"+USER_ID,
                  json={"data":[], "message":"No Orders"}, headers={"Content_Type":"application/json", "Authorization":AUTH_TOKEN}, status=304)

    result =get_orders_page_data()
    print(result)











