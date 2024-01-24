import requests
import json

class Requester():

    def __init__(self, base_url):

        self.base_url = base_url
        self.headers = {
            'Authorization': "",
            'Content-Type': 'application/json'
        }
    
    def get(self, endpoint, data=None):
        response = requests.get(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint, data=None):
        response = requests.post(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None):
        response = requests.put(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint, data=None):
        response = requests.delete(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()
    