from odin_api import requester

class Post():
    def __init__(self):
        self.requester = requester.get_instance()
    