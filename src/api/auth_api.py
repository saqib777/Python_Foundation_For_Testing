from api.base_client import BaseAPIClient



class AuthAPI:
    def __init__(self):
        self.client = BaseAPIClient(
            base_url="https://reqres.in/api",
            headers={"Content-Type": "application/json"}
        )

    def login(self, email=None, password=None):
        payload = {}

        if email is not None:
            payload["email"] = email
        if password is not None:
            payload["password"] = password

        return self.client.post("/login", json=payload)
