import pytest
import allure
import json
import requests
from config import URL
from helpers import get_registration_user, get_registration_user_no_password
from data import EMAIL_DEFAULT, PASSWORD_DEFAULT, NAME_DEFAULT

class TestCreateUser:

    @allure.title('Успешное создание пользователя')
    def test_create_fake_user_true(self):
        email, name, password = get_registration_user()
        response = requests.post(f"{URL}api/auth/register", data={
            "email": email,
            "password": password,
             "name": name
        })

        assert 200 == response.status_code
        assert '{"success":true,"user":{"email":' in response.text

    @allure.title('Неудачная попытка создания пользователя без указания пароля')
    def test_create_fake_user_without_password_false(self):
        email_double, name_double = get_registration_user_no_password()
        response = requests.post(f"{URL}api/auth/register", data={
            "email": email_double,
             "name": name_double
        })

        assert 403 == response.status_code
        assert '{"success":false,"message":"Email, password and name are required fields"}' == response.text

    @allure.title('Неудачная попытка создания уже созданного пользователя')
    def test_create_created_user_false(self):

        response = requests.post(f"{URL}api/auth/register", data={
            "email": EMAIL_DEFAULT,
            "password": PASSWORD_DEFAULT,
             "name": NAME_DEFAULT
        })
        response = requests.post(f"{URL}api/auth/register", data={
            "email": EMAIL_DEFAULT,
            "password": PASSWORD_DEFAULT,
            "name": NAME_DEFAULT
        })

        assert 403 == response.status_code
        assert '{"success":false,"message":"User already exists"}' == response.text
