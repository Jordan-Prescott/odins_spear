from odin_api import requester

class Get():
    def __init__(self):
        self.requester = requester.get_instance()
    