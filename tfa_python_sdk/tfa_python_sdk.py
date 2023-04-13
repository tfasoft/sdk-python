import requests as req

baseUrl = "https://api.tfasoft.com/api"


class TFA:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def authUser(self, user_token):
        urlData = {
            "access_token": self.access_token,
            "user_token": user_token,
        }

        response = req.post(f'{baseUrl}/access', json=urlData)

        data = {
            "status": response.status_code,
            "data": response.json()
        }

        return data
