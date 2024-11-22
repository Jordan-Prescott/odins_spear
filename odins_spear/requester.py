import requests
import json
from .exceptions import OSApiResponseError

from ratelimit import limits, sleep_and_retry
class Requester():

    def __init__(self, base_url: str, rate_limit: bool, logger: object = None):
        """Requester is the object that handles all request to and from the API. 
        Each method object will manage the setting up of the request however it is Requester
        that will send and receive the data. 

        Args:
            base_url (str): Base URL of API
            rate_limit (bool): Rate limit flag which will limit to 5 calls per 1 second
            logger (object, optional): Logger object for logging requests. Defaults to None.
        """
        
        self.base_url = base_url
        self.headers = {
            'Authorization': "",
            'Content-Type': 'application/json'
        }
        self.rate_limit = rate_limit
        self.logger = logger
    
    
    # get, post, put, delete methods takes in data and params and returns method type to _request
    def get(self, endpoint, data=None, params=None):
        return self._request(requests.get, endpoint, data, params)

    
    def post(self, endpoint, data=None):
        return self._request(requests.post, endpoint, data)

    
    def put(self, endpoint, data=None):
        return self._request(requests.put, endpoint, data)
    
    
    def delete(self, endpoint, data=None, params=None):
        return self._request(requests.delete, endpoint, data, params)


    def _request(self, method, endpoint, data=None, params=None):
        """Handles an API request with or without rate limiting.

        Args:
            method (request obj): Request module method type either GET, POST, PUT, DELETE
            endpoint (str): Specific API endpoint for functionality
            data (dict, optional): Python dict used in payload data if needed. Defaults to None.
            params (dict, optional): Parameters used in endpoint if needed. Defaults to None.

        Returns:
            API data: Data returned from API on completion of API call.
        """
        
        # if rate limiting is enabled uses _rate_limited_request where limiting is in place.
        if self.rate_limit:
            return self._rate_limited_request(method, endpoint, data, params)
        else:
            response = method(
                url=self.base_url + endpoint,
                headers=self.headers,
                data=json.dumps(data if data is not None else {}),
                params=(params if params is not None else {})
            )

            # if logger used log request
            if self.logger:
                self.logger._log_request(endpoint=endpoint, response_code=response.status_code)
                
            # flags errors if any returned from the API
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException:
                raise OSApiResponseError(response)
            else:
                return response.json()
        

    @sleep_and_retry
    @limits(calls=5, period=1)
    def _rate_limited_request(self, method, endpoint, data=None, params=None):
        """Handles an API request with rate limiting.
        """
        
        response = method(
            url=self.base_url + endpoint,
            headers=self.headers,
            data=json.dumps(data if data is not None else {}),
            params=(params if params is not None else {})
        )
        
        # if logger used log request
        if self.logger:
            self.logger._log_request(endpoint=endpoint, response_code=response.status_code)
        
        # flags errors if any returned from the API
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException:
            raise OSApiResponseError(response)
        else:
            return response.json()
    