from typing import List
import json

from odin_api import Api
from odin_api.utils import parsing
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
            self.auto_attendants: List[bre.AutoAttendant] = []
            self.call_centers: List[bre.CallCenter] = []
            self.hunt_groups: List[bre.HuntGroup] = []
            self.users: List[bre.User] = []
            self.devices: List[bre.Device] = []
            self.other_entities = [] #Non-common or custom objects

            DataStore.__instance = self
            
    def get_group_state(api: Api, group: bre.Group):
        """ takes in group id and loads group state into broadworks entities.

        :param api: API object used to send requests to create group state in store.
        :param group: Group object of Broadworks group user would like to load state.
        """
    pass

    def store_object(self, *entities):
        """ Takes in objects within the odin_api and custom and stores in lists
        depending on type.

        :param entity: broadwork entities used in odin_api
        """

        for e in entities:
            if isinstance(e, Api):
                self.apis.append(e)
            elif isinstance(e, bre.ServiceProvider):
                self.service_providers.append(e)
            elif isinstance(e, bre.Enterprise):
                self.enterprises.append(e)
            elif isinstance(e, bre.Group):
                self.groups.append(e)
            elif isinstance(e, bre.TrunkGroup):
                self.trunk_groups.append(e)
            elif isinstance(e, bre.AutoAttendant):
                self.auto_attendants.append(e)
            elif isinstance(e, bre.CallCenter):
                self.call_centers.append(e)
            elif isinstance(e, bre.HuntGroup):
                self.hunt_groups.append(e)
            elif isinstance(e, bre.User):
                self.users.append(e)
            elif isinstance(e, bre.Device):
                self.devices.append(e)
            else:
                self.other_entities.append(e)
    
    def export_store(self) -> str:
        """Export all objects in the store and their relationships in JSON format."""
        export_data = {}
        object_lists = {
            'apis': self.apis,
            'service_providers': self.service_providers,
            'enterprises': self.enterprises,
            'groups': self.groups,
            'trunk_groups': self.trunk_groups,
            'auto_attendants': self.auto_attendants,
            'call_centers': self.call_centers,
            'hunt_groups': self.hunt_groups,
            'users': self.users,
            'devices': self.devices,
            'other_entities': self.other_entities
        }

        for key, object_list in object_lists.items():
            export_data[key] = parsing.export_objects(object_list)

        return json.dumps(export_data, indent=2)

    def __str__(self) -> str:
        """ returns complete list of entities in store.
        """
        entities = self.apis + self.enterprises + self.service_providers + self.groups + self.trunk_groups + \
            self.hunt_groups + self.users

        # loops entities and joins into string
        string = lambda e: "\n".join(map(str, e))
        return string(entities)
