import pytest
import allure
import json
import requests
from config import URL
from data import EMAIL_DEFAULT, PASSWORD_DEFAULT, NAME_DEFAULT
class TestGetListOrder:

    @allure.title('Получение заказов пользователя с авторизацией')
    def test_get_list_order_with_authorization(self):
        response = requests.post(f"{URL}api/auth/register", data={
            "email": EMAIL_DEFAULT,
            "password": PASSWORD_DEFAULT,
             "name": NAME_DEFAULT
        })
        response = requests.post(f"{URL}api/auth/login", data={
            "email": EMAIL_DEFAULT,
            "password": PASSWORD_DEFAULT,
             "name": NAME_DEFAULT
        })
        r = response.json()
        accessToken = r["accessToken"]

        response = requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'}, data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        })
        response = requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'}, data={"ingredients": ["61c0c5a71d1f82001bdaaa70","61c0c5a71d1f82001bdaaa71"]
        })
        response = requests.get(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'

        })

        assert 200 == response.status_code
        assert '{"success":true,"orders":' in response.text


    @allure.title('Получение заказов пользователя без авторизации')
    def test_get_list_order_no_authorization(self):
        response = requests.post(f"{URL}api/auth/register", data={
            "email": EMAIL_DEFAULT,
            "password": PASSWORD_DEFAULT,
             "name": NAME_DEFAULT
        })
        response = requests.post(f"{URL}api/auth/login", data={
            "email": EMAIL_DEFAULT,
            "password": PASSWORD_DEFAULT,
             "name": NAME_DEFAULT
        })

        response = requests.post(f"{URL}api/orders", data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        })
        response = requests.post(f"{URL}api/orders", data={"ingredients": ["61c0c5a71d1f82001bdaaa70","61c0c5a71d1f82001bdaaa71"]
        })
        response = requests.get(f"{URL}api/orders")


        assert 401 == response.status_code
        assert '{"success":false,"message":"You should be authorised"}' == response.text
