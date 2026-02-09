from src.api.base_client import BaseAPIClient


class AuthAPI(BaseAPIClient):
    LOGIN_ENDPOINT = "/login"

    def login(self, email=None, password=None):
        payload = {}

        if email is not None:
            payload["email"] = email
        if password is not None:
            payload["password"] = password

        return self.post(self.LOGIN_ENDPOINT, json=payload)
