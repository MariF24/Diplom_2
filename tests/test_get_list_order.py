import pytest
import allure
import json
import requests
from config import URL
from data import EMAIL_DEFAULT, PASSWORD_DEFAULT, NAME_DEFAULT, RESPONSE_CODE_200, PART_OF_TEXT_CREATE_USER_GET_LIST_ORDER_200, RESPONSE_CODE_401, TEXT_NO_AUTORIZATION_401
class TestGetListOrder:

    @allure.title('Получение заказов пользователя с авторизацией')
    def test_get_list_order_with_authorization(self, registration_and_sign_in_and_delete_user):
        r = registration_and_sign_in_and_delete_user.json()
        accessToken = r["accessToken"]

        requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'}, data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        })
        requests.post(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'}, data={"ingredients": ["61c0c5a71d1f82001bdaaa70","61c0c5a71d1f82001bdaaa71"]
        })
        response = requests.get(f"{URL}api/orders", headers={'Authorization': f'{accessToken}'

        })

        assert RESPONSE_CODE_200 == response.status_code
        assert PART_OF_TEXT_CREATE_USER_GET_LIST_ORDER_200 in response.text


    @allure.title('Получение заказов пользователя без авторизации')
    def test_get_list_order_no_authorization(self):

        requests.post(f"{URL}api/auth/register", data={
            "email": EMAIL_DEFAULT,
            "password": PASSWORD_DEFAULT,
             "name": NAME_DEFAULT
        })

        requests.post(f"{URL}api/orders", data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        })
        requests.post(f"{URL}api/orders", data={"ingredients": ["61c0c5a71d1f82001bdaaa70","61c0c5a71d1f82001bdaaa71"]
        })
        response = requests.get(f"{URL}api/orders")


        assert RESPONSE_CODE_401 == response.status_code
        assert TEXT_NO_AUTORIZATION_401 == response.text
