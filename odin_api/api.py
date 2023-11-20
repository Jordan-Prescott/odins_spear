import requests
import os

from odin_api.utils.exceptions import *
from odin_api.scripter import Scripter


class Api:
    """ Connection to Odin API, all interactions with the api are here.

    :param base_url: Base url of your odin instance api.
    :param username: Username used when logging into odin account.
    :param password: Password used when logging into odin account.
    
    :var authorised: Boolean value to indicate if api is authorised.
    :var token: Token string returned from odin api.
    """
    def __init__(self, base_url, username, password) -> None:
        self.base_url = base_url
        self.username = username
        self.password = os.getenv(password, default=None)
        self.authorised = False
        self.token = ""
        self.scripter = Scripter(self)

    # SESSION
    def authenticate(self) -> None:
        """ makes a POST request with the U and P to URL and attempts to authenticate.
        if successful api object is update else it throws an exception.
        """
        endpoint = "api/v2/auth/token"
        try:
            response = requests.post(
                self.base_url + endpoint,
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

    # GROUP

    # TRUNK GROUP

    # HUNT GROUP

    # AUTO ATTENDANT 

    # CALL CENTER 

    # USER 

    # DEVICE
    
    # internal to api
    
    def _requester():
        """ sends request to api, this is used in all functions.
        """
                
        return

    def __str__(self) -> str:
        return f"API - url: {self.base_url}, username: {self.username}, " \
            f"password: {self.password}, Authenticated: {self.authorised}"
    