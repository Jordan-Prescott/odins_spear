import requests
import os
import json
import typing

from odin_api.utils.exceptions import *
from odin_api.scripter import Scripter
from odin_api.utils.oa_logger import logger
from odin_api.api_methods import *
from odin_api.requester import Requester


class Api:

    logger = logger
    
    filters = [
        "macAddress", "lastName", "firstName", "dn",
        "emailAddress", "userId", "extension"
    ]
    
    def __init__(self, base_url, username, password) -> None:
        """ Connection to Odin API, all interactions with the api are here.

        Args:
            base_url (str): Base url of your odin instance api.
            username (str): Username used when logging into odin account.
            password (str): Password used when logging into odin account stored as virtual environment.
            
        Vars: 
            authorised (bool): Boolean value to indicate if api is authorised.\
            token (str): Token string returned from odin api.
        """
        
        self.base_url = base_url
        self.username = username
        self.password = os.getenv(password, default=None)
        self.authenticated = False
        
        self.requester = Requester(self.base_url)
        
        self.get = get.Get(self.requester)
        self.post = post.Post(self.requester)
        self.put = put.Put(self.requester)
        self.delete = delete.Delete(self.requester)
        
        self.scripter = Scripter(api=self)

        
    # SESSION
    def authenticate(self) -> None:
        """ makes a POST request with the U and P to URL and attempts to authenticate.
        if successful api object is update else it throws an exception.
        """
        try:
            response = self.post.session(self.username, self.password)
        except requests.exceptions.HTTPError:
            raise OAApiAuthenticationFail()
        
        self.requester.token = response["token"]
        self.requester.headers['Authorization'] = f'Bearer {self.token}'
        
        self.authenticated = True

        
    def __str__(self) -> str:
        return f"API - url: {self.base_url}, username: {self.username}, " \
            f"Authenticated: {self.authenticated}"
    