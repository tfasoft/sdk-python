import requests as req

class TFA:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def authUser(self, user_token):
        return req.get(f'https://tele-fa-api.herokuapp.com/api/access/{self.access_token}/{user_token}').json()