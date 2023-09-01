from typing import List


class Store:
    """ Local store of objects, when each object is instantiated it is added to
    the appropriate list.

    Singleton design pattern to get store use get_instance().
    """

    __instance = None

    @staticmethod
    def get_instance():
        if Store.__instance is None:
            Store()
        return Store.__instance

    def __init__(self):
        if Store.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.apis = []
            self.enterprises = []
            self.service_providers = []
            self.groups = []
            self.trunk_groups = []
            self.hunt_groups = []
            self.users = []

            Store.__instance = self