import pytest
import allure
import json
import requests
from config import URL
from data import EMAIL_DEFAULT, PASSWORD_DEFAULT, NAME_DEFAULT
from helpers import get_registration_user, get_registration_user_no_password
class TestCreateOrder:

    @allure.title('Успешное создание заказа с авторизацией')
    def test_create_order_true(self):
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

        response = requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'

        }, data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        })


        assert 200 == response.status_code
        assert '{"success":true,"name":' in response.text



    @allure.title('Неудачная попытка создания заказа с неверным хэшем ингредиентов с авторизацией')
    def test_create_order_incorrect_ingredients(self):
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

        response = requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'}, data={"ingredients": ["",""]
        })

        assert 500 == response.status_code
        assert 'Internal Server Error' in response.text

    @allure.title('Неудачная попытка создания заказа с отсутствием ингредиентов с авторизацией')
    def test_create_order_no_ingredients(self):
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

        response = requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'}, data={"ingredients": []
        })


        assert 400 == response.status_code
        assert '{"success":false,"message":"Ingredient ids must be provided"}' == response.text


    @allure.title('Успешное создание заказа без авторизации')
    def test_create_order_no_authorization(self):
        response = requests.post(f"{URL}api/orders", data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        })

        assert 200 == response.status_code #без авторизации заказ успешно создан
        assert '{"success":true,"name":' in response.text



