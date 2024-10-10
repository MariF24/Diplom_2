import pytest
import allure
import json
import requests
from config import URL
from data import EMAIL_DEFAULT, PASSWORD_DEFAULT, NAME_DEFAULT

class TestSignInUser:

    @allure.title('Успешная авторизация пользователя')
    def test_sign_in_user_true(self):
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
        assert 200 == response.status_code
        assert '{"success":true,"accessToken":"Bearer' in response.text

    @allure.title('Неудачная авторизация пользователя с неверным логином и паролем')
    def test_sign_in_user_false(self):
        response = requests.post(f"{URL}api/auth/register", data={
            "email": EMAIL_DEFAULT,
            "password": PASSWORD_DEFAULT,
            "name": NAME_DEFAULT
        })

        response = requests.post(f"{URL}api/auth/login", data={
            "email": 't89067536142@yandex.ru',
            "password": '1234567',
            "name": NAME_DEFAULT
        })

        assert 401 == response.status_code
        assert '{"success":false,"message":"email or password are incorrect"}' == response.text