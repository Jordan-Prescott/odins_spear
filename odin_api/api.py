import requests

from odin_api.exceptions import *
from odin_api.store import Store


class Api:
    """ Connection to Odin API, all interactions with the api are here.
    """
    def __init__(self, url, username, password) -> None:
        self.url = url
        self.username = username
        self.password = password
        self.authorised = False
        self.token = ""

        Store.get_instance().apis.append(self)

    def authenticate(self) -> None:
        """ makes a POST request with the U and P to URL and attempts to authenticate.
        if successful api object is update else it throws an exception.
        """
        endpoint = "/auth/token"
        try:
            response = requests.post(
                self.url + endpoint,
                data={
                    "username": self.username,
                    "password": self.password
                }
            )
            response.raise_for_status()

            self.token = response.json()["token"]
            self.authorised = True
        except requests.exceptions.HTTPError:
            raise OAApiAuthenticationFail()

    def __str__(self):
        return f"API - url: {self.url}, username: {self.username}, " \
            f"password: {self.password}, Authenticated: {self.authorised}"