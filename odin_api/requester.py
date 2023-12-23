import requests
import json
class requester():
    
    __instance = None

    @staticmethod
    def get_instance():
        if requester.__instance is None:
            requester()
        return requester.__instance
    
    def __init__(self, base_url, username, password):
        if requester.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.base_url = base_url
            self.username = username
            self.password = password
            self.headers = {
                'Authorization': '',
                'Content-Type': 'application/json'
            }
            self.token = ""
        
        requester.__instance = self
    
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