import pytest
import allure
import json
import requests
from config import URL
from data import RESPONSE_CODE_200, PART_OF_TEXT_CREATE_USER_ORDER_200, RESPONSE_CODE_500, PART_OF_TEXT_500, RESPONSE_CODE_400, TEXT_USER_CREATE_ORDER_NO_INGREDIENTS_400
class TestCreateOrder:

    @allure.title('Успешное создание заказа с авторизацией')
    def test_create_order_true(self, registration_and_sign_in_and_delete_user):

        r = registration_and_sign_in_and_delete_user.json()
        accessToken = r["accessToken"]

        response = requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'

        }, data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        })

        assert RESPONSE_CODE_200 == response.status_code
        assert PART_OF_TEXT_CREATE_USER_ORDER_200 in response.text




    @allure.title('Неудачная попытка создания заказа с неверным хэшем ингредиентов с авторизацией')
    def test_create_order_incorrect_ingredients(self, registration_and_sign_in_and_delete_user):

        r = registration_and_sign_in_and_delete_user.json()
        accessToken = r["accessToken"]

        response = requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'}, data={"ingredients": ["",""]
        })

        assert RESPONSE_CODE_500 == response.status_code
        assert PART_OF_TEXT_500 in response.text

    @allure.title('Неудачная попытка создания заказа с отсутствием ингредиентов с авторизацией')
    def test_create_order_no_ingredients(self, registration_and_sign_in_and_delete_user):

        r = registration_and_sign_in_and_delete_user.json()
        accessToken = r["accessToken"]

        response = requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'}, data={"ingredients": []
        })


        assert RESPONSE_CODE_400 == response.status_code
        assert TEXT_USER_CREATE_ORDER_NO_INGREDIENTS_400 == response.text


    @allure.title('Успешное создание заказа без авторизации')
    def test_create_order_no_authorization(self):
        response = requests.post(f"{URL}api/orders", data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        })

        assert RESPONSE_CODE_200 == response.status_code #без авторизации заказ успешно создан
        assert PART_OF_TEXT_CREATE_USER_ORDER_200 in response.text



