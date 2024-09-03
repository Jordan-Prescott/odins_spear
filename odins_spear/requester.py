import requests
import json

from ratelimit import limits, sleep_and_retry
class Requester():


    def __init__(self, base_url: str, rate_limit: bool, logger: object = None):
        self.base_url = base_url
        self.headers = {
            'Authorization': "",
            'Content-Type': 'application/json'
        }
        self.rate_limit = rate_limit
        self.logger = logger
    
    
    def get(self, endpoint, data=None, params=None):
        return self._request(requests.get, endpoint, data, params)

    
    def post(self, endpoint, data=None):
        return self._request(requests.post, endpoint, data)

    
    def put(self, endpoint, data=None):
        return self._request(requests.put, endpoint, data)

    
    def delete(self, endpoint, data=None):
        return self._request(requests.delete, endpoint, data)


    def _request(self, method, endpoint, data=None, params=None):
        
        


        if self.rate_limit:
            return self._rate_limited_request(method, endpoint, data, params)
        else:
            response = method(
                url=self.base_url + endpoint,
                headers=self.headers,
                data=json.dumps(data if data is not None else {}),
                params=(params if params is not None else {})
            )
            self.logger._log_request(endpoint=endpoint, response_code=response.status_code)
            response.raise_for_status()
            if isinstance(response.json(), list):
                return response.request.body
            return response.json()

        

    @sleep_and_retry
    @limits(calls=5, period=1)
    def _rate_limited_request(self, method, endpoint, data=None, params=None):
        response = method(
            url=self.base_url + endpoint,
            headers=self.headers,
            data=json.dumps(data if data is not None else {}),
            params=(params if params is not None else {})
        )
        self.logger._log_request(endpoint=endpoint, response_code=response.status_code)
        response.raise_for_status()
        if isinstance(response.json(), list):
            return response.request.body
        return response.json()
    