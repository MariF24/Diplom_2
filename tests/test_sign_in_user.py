import pytest
import allure
import json
import requests
from config import URL
from data import NAME_DEFAULT, RESPONSE_CODE_200, PART_OF_TEXT_CREATE_USER_SIGN_IN_200, RESPONSE_CODE_401, TEXT_NO_AUTORIZATION_WITH_INCORRECT_LOGIN_PASSWORD_401

class TestSignInUser:

    @allure.title('Успешная авторизация пользователя')
    def test_sign_in_user_true(self, registration_and_sign_in_and_delete_user):
        response = registration_and_sign_in_and_delete_user

        assert RESPONSE_CODE_200 == response.status_code
        assert PART_OF_TEXT_CREATE_USER_SIGN_IN_200 in response.text

    @allure.title('Неудачная авторизация пользователя с неверным логином и паролем')
    def test_sign_in_user_false(self):

        response = requests.post(f"{URL}api/auth/login", data={
            "email": 't89067536142@yandex.ru',
            "password": '1234567',
            "name": NAME_DEFAULT
        })

        assert RESPONSE_CODE_401 == response.status_code
        assert TEXT_NO_AUTORIZATION_WITH_INCORRECT_LOGIN_PASSWORD_401 == response.text