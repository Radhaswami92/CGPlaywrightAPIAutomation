import requests
def request_spec(relative_base_url, **kwargs):
    print(kwargs)
    base_url = "https://rahulshettyacademy.com"
    final_url = f"{base_url}{relative_base_url}"

    header ={"Content-Type":"application/json"}
    with requests.session() as session:
        response =  requests.post(url=final_url, json=kwargs,headers=header)
        #print(response = requests.post(url=final_url, json=kwargs, headers=header).raise_for_status().json())
        response.elapsed.total_seconds()
        assert response.elapsed.total_seconds() <3.0
        return  response.json()



def test_session():
    print(request_spec("/api/ecom/auth/login", userEmail="jeet.zaper@gmail.com", userPassword="Radhaswami@103"))

