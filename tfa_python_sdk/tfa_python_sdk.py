import requests as req

class TFA:
    def __init__(self, access_token) -> None:
        self.access_token = access_token
        self.testUrl = "http://localhost:8000"
        self.baseUrl = "https://tele-fa-api.herokuapp.com"

    def authUser(self, user_token):
        urlData = {
            "access_token": self.access_token,
            "user_token": user_token,
        }

        response = req.post(f'{self.baseUrl}/api/auth/access', json = urlData)

        data = {
            "status": response.status_code,
            "data": response.json()
        }

        return data