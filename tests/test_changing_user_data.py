import pytest
import allure
import json
import requests
from config import URL
from data import EMAIL_DEFAULT, PASSWORD_DEFAULT, NAME_DEFAULT
from helpers import get_registration_user, get_registration_user_no_password
class TestChangingUserData:

    @allure.title('Успешное изменение данных пользователя с авторизацией')
    def test_changing_user_data_authorization_true(self):
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

        email_double, name_double = get_registration_user_no_password()
        updated_user = {
            "email": email_double,
            "name": name_double
        }
        response = requests.patch(f"{URL}api/auth/user", headers={'Authorization': f'{accessToken}'

        }, data=updated_user)


        assert 200 == response.status_code
        assert '{"success":true,"user":{"email":' in response.text


    @allure.title('Успешное изменение данных рандомного сгенерированного пользователя с авторизацией')
    def test_changing_random_user_data_authorization_true(self):
        email, name, password = get_registration_user()
        response = requests.post(f"{URL}api/auth/register", data={
            "email": email,
            "password": password,
             "name": name
        })

        r = response.json()
        accessToken = r["accessToken"]

        email_double, name_double = get_registration_user_no_password()
        updated_user = {
            "email": email_double,
            "name": name_double
        }
        response = requests.patch(f"{URL}api/auth/user", headers={'Authorization': f'{accessToken}'

        }, data=updated_user)

        assert 200 == response.status_code
        assert '{"success":true,"user":{"email":' in response.text


    @allure.title('Неудачная попытка изменение данных пользователя без авторизации и с существующей почтой')
    def test_changing_user_data_no_authorization_email_true(self):
        response = requests.post(f"{URL}api/auth/register", data={
            "email": EMAIL_DEFAULT,
            "password": PASSWORD_DEFAULT,
             "name": NAME_DEFAULT
        })
        email, name, password = get_registration_user()
        response = requests.post(f"{URL}api/auth/register", data={
            "email": email,
            "password": password,
             "name": name
        })
        r = response.json()
        accessToken = r["accessToken"]

        updated_user = {
            "email": 'm89067536142@yandex.ru',
            "name": 'Maria'
        }
        response = requests.patch(f"{URL}api/auth/user", headers={'Authorization': f'{accessToken}'

        }, data=updated_user)


        assert 403 == response.status_code
        assert '{"success":false,"message":"User with such email already exists"}' == response.text

    @allure.title('Неудачная попытка изменение данных пользователя без авторизации')
    def test_changing_user_data_no_authorization(self):
        email, name, password = get_registration_user()
        response = requests.post(f"{URL}api/auth/register", data={
            "email": email,
            "password": password,
             "name": name
        })

        updated_user = {
            "email": EMAIL_DEFAULT,
            "name": 'Maria'
        }
        response = requests.patch(f"{URL}api/auth/user", data=updated_user)

        assert 401 == response.status_code
        assert '{"success":false,"message":"You should be authorised"}' == response.text
