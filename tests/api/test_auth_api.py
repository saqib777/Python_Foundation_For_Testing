import pytest
from api.auth_api import AuthAPI

@pytest.fixture
def auth_api():
    return AuthAPI()


def test_login_success(auth_api):
    response = auth_api.login(
        email="eve.holt@reqres.in",
        password="cityslicka"
    )

    assert response.status_code == 200
    assert "token" in response.json()


def test_login_missing_password(auth_api):
    response = auth_api.login(
        email="eve.holt@reqres.in",
        password=""
    )

    assert response.status_code == 400
    assert "error" in response.json()


def test_login_missing_email(auth_api):
    response = auth_api.login(
        email="",
        password="cityslicka"
    )

    assert response.status_code == 400


def test_login_invalid_credentials(auth_api):
    response = auth_api.login(
        email="wrong@email.com",
        password="wrong"
    )

    assert response.status_code == 400


def test_login_response_time(auth_api):
    response = auth_api.login(
        email="eve.holt@reqres.in",
        password="cityslicka"
    )

    assert response.elapsed.total_seconds() < 2
