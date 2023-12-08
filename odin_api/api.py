import requests
import os

from odin_api.utils.exceptions import *
from odin_api.scripter import Scripter
from odin_api.utils.oa_logger import logger
from odin_api.utils import parsing
from odin_api.store import broadwork_entities as bre


class Api:
    """ Connection to Odin API, all interactions with the api are here.

    :param base_url: Base url of your odin instance api.
    :param username: Username used when logging into odin account.
    :param password: Password used when logging into odin account stored as virtual environment.
    
    :var authorised: Boolean value to indicate if api is authorised.
    :var token: Token string returned from odin api.
    """
    
    logger = logger
    
    def __init__(self, base_url, username, password) -> None:
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
    
    def get_user_by_id(self, user: bre.User):
        
        endpoint = f"/users?userId={user.id}"
        
        return self._requester("get", endpoint)
    
    def post_user(self, user: bre.User):
        
        endpoint = "users"
        
        parsing.serialise_user(user)
        
        # response = requests.get(
        #     url=self.base_url + endpoint,
        #     headers=self.headers,
        #     data={}
        # )
        
        # response.raise_for_status()
        # return response.json()

    # DEVICE
    
    # CUSTOM
    
    # internal to api
    
    def _requester(self, request_type, endpoint, data={}):
        """ sends request to api, this is used in all functions.
        """
        
        if request_type.lower() == 'get':
            response = requests.get(
            url=self.base_url + endpoint,
            headers=self.headers,
            data=data
        )
            response.raise_for_status()
            return response.json()
        
        elif request_type.lower() == 'post':
            response = requests.post(
            url=self.base_url + endpoint,
            headers=self.headers,
            data=data
        )
            response.raise_for_status()
            return response.json()
                
        elif request_type.lower() == 'put':
            response = requests.put(
            url=self.base_url + endpoint,
            headers=self.headers,
            data=data
        )
            response.raise_for_status()
            return response.json() 
        
        elif request_type.lower() == 'delete':
            response = requests.delete(
            url=self.base_url + endpoint,
            headers=self.headers,
            data=data
        )
            response.raise_for_status()
            return response.json()  
        
        else:
            raise OARequestTypeError     

    def __str__(self) -> str:
        return f"API - url: {self.base_url}, username: {self.username}, " \
            f"password: {self.password}, Authenticated: {self.authorised}"
    