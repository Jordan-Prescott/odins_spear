import requests
import os
import json

from odin_api.utils.exceptions import *
from odin_api.scripter import Scripter
from odin_api.utils.oa_logger import logger
from odin_api.utils import parsing


class Api:

    logger = logger
    
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
        self.authorised = False
        self.scripter = Scripter(api=self)
        self.headers = {
            'Authorization': '',
            'Content-Type': 'application/json'
        }
        self.token = ""

        
    # SESSION
    def authenticate(self) -> None:
        """ makes a POST request with the U and P to URL and attempts to authenticate.
        if successful api object is update else it throws an exception.
        """
        
        endpoint = "/auth/token"
        data={
            "username": self.username,
            "password": self.password
        }
        
        try:
            response = self._requester("post", endpoint, data=data)
        except requests.exceptions.HTTPError:
            raise OAApiAuthenticationFail()
        
        self.token = response["token"]
        self.headers['Authorization'] = f'Bearer {self.token}'
        self.authorised = True

    # GROUP

    # TRUNK GROUP

    # HUNT GROUP

    # AUTO ATTENDANT 

    # CALL CENTER 

    # USER 
    
    def get_user_by_id(self, user_id):
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        endpoint = f"/users?userId={user_id}"
        
        return self._requester("get", endpoint)
    
    def post_user(self, user):
        """_summary_

        Args:
            user (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        endpoint = "users"
        
        return self._requester("post", endpoint, data=user)

    # DEVICE
    
    # CUSTOM
    
    # internal to api
    
    def _requester(self, request_type, endpoint, data=None):
        """ sends request to api, this is used in all functions.
        """
        
        if request_type.lower() == 'get':
            response = requests.get(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
            response.raise_for_status()
            return response.json()
        
        elif request_type.lower() == 'post':
            response = requests.post(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
            response.raise_for_status()
            return response.json()
                
        elif request_type.lower() == 'put':
            response = requests.put(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
            response.raise_for_status()
            return response.json() 
        
        elif request_type.lower() == 'delete':
            response = requests.delete(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
            response.raise_for_status()
            return response.json()  
        
        else:
            raise OARequestTypeError     

    def __str__(self) -> str:
        return f"API - url: {self.base_url}, username: {self.username}, " \
            f"password: {self.password}, Authenticated: {self.authorised}"
    