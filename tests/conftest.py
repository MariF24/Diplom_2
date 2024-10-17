import pytest
from data import EMAIL_DEFAULT, PASSWORD_DEFAULT, NAME_DEFAULT
from config import URL
import requests
@pytest.fixture(scope='function') # фикстура, которая регистрирует и удаляет пользователя
def registration_and_sign_in_and_delete_user():
    requests.post(f"{URL}api/auth/register", data={
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

    yield response

    requests.delete(f"{URL}api/auth/user", headers={'Authorization': f'{accessToken}'})



