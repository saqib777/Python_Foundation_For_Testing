from api.base_client import BaseAPIClient

class AuthAPI(BaseAPIClient):
    def __init__(self):
        super().__init__(
            base_url="https://reqres.in"
        )

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        return self.post("/api/login", json=payload)
