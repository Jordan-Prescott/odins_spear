from ..requester import Requester


class BaseEndpoint:
    def __init__(self):
        self._requester = Requester.get_instance()
