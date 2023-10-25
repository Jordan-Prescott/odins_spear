from typing import List

from odin_api import Api
from . import broadworks_entities as bre

class DataStore:
    """ Local store of objects, when each object is instantiated it is added to
    the appropriate list.

    Singleton design pattern to get store use get_instance().
    """

    __instance = None

    @staticmethod
    def get_instance():
        if DataStore.__instance is None:
            DataStore()
        return DataStore.__instance

    def __init__(self):
        if DataStore.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.apis: List[Api] = []
            self.service_providers: List[bre.ServiceProvider] = []
            self.enterprises: List[bre.Enterprise] = []
            self.groups: List[bre.Group] = []
            self.trunk_groups: List[bre.TrunkGroup] = []
            self.hunt_groups: List[bre.HuntGroup] = []
            self.users: List[bre.User] = []
            self.other_entities = [] #Non-common or custom objects

            DataStore.__instance = self

    def get_group_state(group):
        """ takes in group id and loads group state into broadworks entities.

        :param group: Group object of Broadworks group user would like to load state.
        """
        pass

    def store_object(self, *entities):
        """ Takes in objects within the odin_api and custom and stores in lists
        depending on type.

        :param entity: 
        """

        from . import broadworks_entities
        from odin_api.api import Api

        for e in entities:
            if isinstance(e, Api):
                self.apis.append(e)
            elif isinstance(e, broadworks_entities.ServiceProvider):
                self.service_providers.append(e)
            elif isinstance(e, broadworks_entities.Enterprise):
                self.enterprises.append(e)
            elif isinstance(e, broadworks_entities.Group):
                self.groups.append(e)
            elif isinstance(e, broadworks_entities.TrunkGroup):
                self.trunk_groups.append(e)
            elif isinstance(e, broadworks_entities.HuntGroup):
                self.hunt_groups.append(e)
            elif isinstance(e, broadworks_entities.User):
                self.users.append(e)
    
    def export_store():
        """ exports entire store to json file
        """
        pass

    def __str__(self):
        """ returns complete list of entities in store.
        """
        entities = self.apis + self.enterprises + self.service_providers + self.groups + self.trunk_groups + \
            self.hunt_groups + self.users

        # loops entities and joins into string
        string = lambda e: "\n".join(map(str, e))
        return string(entities)
