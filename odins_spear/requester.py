import requests
import json

from ratelimit import limits, sleep_and_retry

class Requester():

    # messing around this is one way to do 
    __CALL_RATE_LIMIT = 0
    __TIME_RATE_LIMIT = 0

    def __init__(self, base_url, rate_limit_requests: int = None, rate_limit_time: int = None):

        self.base_url = base_url
        self.headers = {
            'Authorization': "",
            'Content-Type': 'application/json'
        }
        
        Requester.__CALL_RATE_LIMIT = rate_limit_requests if rate_limit_requests else None
        Requester.__TIME_RATE_LIMIT = rate_limit_time if rate_limit_time else None
      
    
    @sleep_and_retry
    @limits(calls= Requester.__CALL_RATE_LIMIT, period=__TIME_RATE_LIMIT, raise_on_limit=True)
    def get(self, endpoint, data=None):
        response = requests.get(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()
    
    @sleep_and_retry
    @limits(calls=2, period=1, raise_on_limit=False)
    def post(self, endpoint, data=None):
        response = requests.post(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()

    @sleep_and_retry
    @limits(calls=2, period=1, raise_on_limit=False)
    def put(self, endpoint, data=None):
        response = requests.put(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()
    
    @sleep_and_retry
    @limits(calls=2, period=1, raise_on_limit=False)
    def delete(self, endpoint, data=None):
        response = requests.delete(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()
    