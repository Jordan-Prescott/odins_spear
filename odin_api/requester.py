
class requester():
    
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.headers = {
            'Authorization': '',
            'Content-Type': 'application/json'
        }
        self.token = ""
        
    
    