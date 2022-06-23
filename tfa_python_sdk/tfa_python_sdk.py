class TFA:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def authUser(self, user_token):
        return {'aid': self.access_token, 'uid': user_token}