import requests
import json
from ratelimit import limits, sleep_and_retry

class Requester():

    def __init__(self, base_url, rate_limit: bool = True):
        self.base_url = base_url
        self.headers = {
            'Authorization': "",
            'Content-Type': 'application/json'
        }
        self.rate_limit = rate_limit
    
    
    def get(self, endpoint, data=None):
        return self._request(requests.get, endpoint, data)

    
    def post(self, endpoint, data=None):
        return self._request(requests.post, endpoint, data)

    
    def put(self, endpoint, data=None):
        return self._request(requests.put, endpoint, data)

    
    def delete(self, endpoint, data=None):
        return self._request(requests.delete, endpoint, data)


    def _request(self, method, endpoint, data=None):
        if self.rate_limit:
            return self._rate_limited_request(method, endpoint, data)
        else:
            response = method(
                url=self.base_url + endpoint,
                headers=self.headers,
                data=json.dumps(data if data is not None else {})
            )
            response.raise_for_status()
            return response.json()
        

    @sleep_and_retry
    @limits(calls=1, period=10)
    def _rate_limited_request(self, method, endpoint, data=None):
        response = method(
            url=self.base_url + endpoint,
            headers=self.headers,
            data=json.dumps(data if data is not None else {})
        )
        response.raise_for_status()
        return response.json()
    