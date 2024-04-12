import requests
import os

from odins_spear.requester import Requester
from odins_spear.methods import *
from odins_spear.scripter import Scripter
from odins_spear.reporter import Reporter
from odins_spear.exceptions import (OAApiAuthenticationFail, 
                                 AOSessionRefreshFail, 
                                 AOFailedToLocateSession)


class Api:
    
    def __init__(self, base_url: str, username: str, password: str,
                rate_limit: bool = True) -> None:
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
        self.password = os.getenv(password)
        self.rate_limit = rate_limit
        
        self.authorised = False
        self.token = ""
        
        self.requester = Requester(self.base_url, self.rate_limit)
        
        self.get = get.Get(self.requester)
        self.post = post.Post(self.requester)
        self.put = put.Put(self.requester)
        self.delete = delete.Delete(self.requester)
        
        self.scripter = Scripter(api=self)
        self.reporter = Reporter(api=self)
 
 
    def authenticate(self):
        
        try:
            response = self.post.session(self.username, self.password)
            self._update_requester(response)
            return True
        except requests.exceptions.HTTPError:
            raise OAApiAuthenticationFail()
    
    
    def refresh_authorisation(self):
        
        try:
            response = self.put.session()
            self._update_requester(response)
            return True
        except requests.exceptions.HTTPError:
            raise AOSessionRefreshFail()
  
    
    def get_auth_details(self):
        
        try:
            return self.get.session()
        except requests.exceptions.HTTPError:
            raise AOFailedToLocateSession()


    def _update_requester(self, session_response):
        self.token = session_response["token"]
        self.requester.headers["Authorization"] = f"Bearer {self.token}"
        self.authorised = True


    def __str__(self) -> str:
        return f"API - url: {self.base_url}, username: {self.username}, password: {self.password}." \
            f"Authenticated: {self.authorised}"
    