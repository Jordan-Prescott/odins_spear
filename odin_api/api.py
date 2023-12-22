import requests
import os
import json
import typing

from odin_api.utils.exceptions import *
from odin_api.scripter import Scripter
from odin_api.utils.oa_logger import logger


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

    # AUTO ATTENDANTS
    
    def get_auto_attendants(self, service_provider_id, group_id):
        """_summary_

        Args:
            service_provider_id (_type_): _description_
            group_id (_type_): _description_

        Returns:
            _type_: _description_
        """

        endpoint = f"/auto-attendants?serviceProviderId={service_provider_id}&groupId={group_id}"
        
        return self._requester("get", endpoint)
        
    # REPORTS  
    
    def get_user_report(self, user_id):
        """ Detailed report of user including services and service packs assigned.

        Args:
            user_id (str): Target user id of user.

        Returns:
            dict: Detailed report of user including services and service packs.
        """
        
        endpoint = f"/users/reports/users?userId={user_id}"
        
        return self._requester("get", endpoint)

    # USER 
    
    def get_users(self, servive_provider_id: str =None, group_id: str =None, 
                  filter: str =None, filter_type: str =None, filter_value: str =None,
                  limit: int =None):
        """
        Returns list of users depending on filter criteria.
        
        Args:
            servive_provider_id (str, optional): Service or Enterprise ID,
            top level object. Defaults to None.
            group_id (str, optional): Group ID where user is hosted. Defaults to None.
            filter (str, optional): Filter criteria, supported filters below. Defaults to None.
            filter_type (str, optional): Options: equal to, starts with, or contains. Defaults to None.
            filter_value (str, optional): Value filtering on e.g. firstName. Defaults to None.
            limit (int, optional): Limits the amount of values API returns. Defaults to None.

        Returns:
            dict: List of users.
            
        #### Supported Filters
        macAddress: search by device
        lastName: filter by lastName
        firstName: filter by firstName
        dn: filter by dn
        emailAddress: filter by emailAddress
        userId: filter by userId
        extension: filter by extension
        
        #### Examples
        Get all users in Enterprise ent1
        GET /api/v2/users?serviceProviderId=ent1

        Get all users in Group grp1
        GET /api/v2/users?serviceProviderId=ent1&groupId=grp1

        Get up to 10 users in the system with a last name that contains smith
        GET /api/v2/users?lastName=*smith*&limit=10

        Get the users in grp1 that have a phone number that starts with 513333
        GET /api/v2/users?serviceProviderId=ent1&groupId=grp1&dn=513333*
        """
        
        endpoint = f"/users?"

        if servive_provider_id:
            endpoint += f"serviceProviderId={servive_provider_id}"
            if group_id:
                endpoint += f"&groupId={group_id}"
        if filter:       
            if servive_provider_id:
                endpoint += "&"   
            endpoint += f"{self._format_filter(filter, filter_type, filter_value)}"   
        if limit:
            # TODO: Limit is failing when needed, odin to resolve
            endpoint += f"&limit={limit}"

        return self._requester("get", endpoint)
    
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

    def _format_filter(self, filter, type, value):
        
        if filter not in self.filters:
                raise OAUnsupportedFilter
            
        if type.lower() == "equal to":
            return f"{filter}={value}" 
        elif type.lower() == "starts with":
            return f"{filter}={value}*" 
        else: #contains
            return f"{filter}=*{value}*"
    
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
    