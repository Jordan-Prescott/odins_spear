import requests
import os

from .requester import Requester
from .methods import *
from .logger import Logger
from .scripter import Scripter
from .reporter import Reporter
from .exceptions import (OSApiAuthenticationFail, 
                                 OSSessionRefreshFail, 
                                 OSFailedToLocateSession)


class Api:
    
    def __init__(self, base_url: str, username: str, password: str,
                rate_limit: bool = True) -> None:
        """ Connection to Odin API, all interactions with the api are here.

        Args:
            base_url (str): Base url of your odin instance api.
            username (str): Username used when logging into odin account.
            password (str): Password used when logging into odin account stored as virtual environment.
            rate_limit (bool): Enables (True) or Disables (False) rate limiting to 5 calls per second. Defaults to True.
            
        Vars: 
            authorised (bool): Boolean value to indicate if api is authorised.\
            token (str): Token string returned from odin api.
        """
        
        self.base_url = base_url
        self.username = username
        self.password = os.getenv(password)
        self.rate_limit = rate_limit
        
        self.authorised = False
        self.token = ""
        
        self.logger = Logger.get_instance(self.username)
        self._requester = Requester(self.base_url, self.rate_limit, self.logger)
        
        self.get = get.Get(self._requester)
        self.post = post.Post(self._requester)
        self.put = put.Put(self._requester)
        self.delete = delete.Delete(self._requester)
        
        self.scripter = Scripter(api=self)
        self.reporter = Reporter(api=self)
 
 
    def authenticate(self):
        """Authenticates session with username and password supplied by user.

        Raises:
            OSApiAuthenticationFail: Raised if authenticaion fails.

        Returns:
            Bool: Returns True to indicate authentication was successful.
        """
        
        try:
            response = self.post.session(self.username, self.password)
            self._update_requester(response)
            return True
        except requests.exceptions.HTTPError:
            raise OSApiAuthenticationFail()
    
    
    def refresh_authorisation(self):
        """Re-authenticates the session with the API. Used if API key is to expire. 

        Raises:
            OSSessionRefreshFail: Raised if authentication fails.

        Returns:
            Bool: Returns True to indicate authentication was successful.
        """
        
        try:
            response = self.put.session()
            self._update_requester(response)
            return True
        except requests.exceptions.HTTPError:
            raise OSSessionRefreshFail()
  
    
    def get_auth_details(self):
        """Gets current session details. 

        Raises:
            OSFailedToLocateSession: Raised when session details can't be found.
                Most likely because session has expired.

        Returns:
            Dict: Current session details. 
        """
        
        try:
            return self.get.session()
        except requests.exceptions.HTTPError:
            raise OSFailedToLocateSession()


    def _update_requester(self, session_response):
        """When authenticating or re-auth update requester with token so it can make
        api calls 

        Args:
            session_response (obj): Requests mod response.
        """
        self.token = session_response["token"]
        self._requester.headers["Authorization"] = f"Bearer {self.token}"
        self.authorised = True


    def __str__(self) -> str:
        return f"API - url: {self.base_url}, username: {self.username}" \
            f"Authenticated: {self.authorised}"
    