import requests as req

session = req.Session()
session.trust_env = False

baseUrl = "http://localhost:25000/api"


class TFA:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def authUser(self, user_token):
        urlData = {
            "access_token": self.access_token,
            "user_token": user_token,
        }

        response = session.post(f'{baseUrl}/access', json=urlData)

        data = {
            "status": response.status_code,
            "data": response.json()
        }

        return data
