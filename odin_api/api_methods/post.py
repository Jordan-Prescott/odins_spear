import requests

from odin_api.utils.exceptions import *

class Post():
    def __init__(self, requester):
        self.requester = requester
        
    def session(self, username, password):
        
        endpoint = "/auth/token"
        
        data={
            "username": username,
            "password": password
        }
        
        return self.requester.post(endpoint, data=data)
        
    def user(self, user):
        """_summary_

        Args:
            user (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        endpoint = "users"
        
        return self.requester.post(endpoint, data=user)
    
    