
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
    
    