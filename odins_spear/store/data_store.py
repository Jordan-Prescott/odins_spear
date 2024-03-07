from typing import List
import json

from odins_spear import api
from odins_spear.utils import parsing
from . import broadwork_entities as bre

class DataStore:
    """ Data store for objects in program. 

    Note: Singleton design pattern to get store use get_instance().
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
            self.apis: List[api.Api] = []
            self.service_providers_enterprises: List[bre.ServiceProvider] = []
            self.groups: List[bre.Group] = []
            self.trunk_groups: List[bre.TrunkGroup] = []
            self.auto_attendants: List[bre.AutoAttendant] = []
            self.call_centers: List[bre.CallCenter] = []
            self.hunt_groups: List[bre.HuntGroup] = []
            self.users: List[bre.User] = []
            self.devices: List[bre.Device] = []

            DataStore.__instance = self


    def store_object(self, *entities) -> None:
        """ Takes in a list/ single Broadwork enetities and saves them to the correct list.

        Args: 
            entities (args): broadwork entities such as user, hunt group, call center etc.
        """      
        
        for e in entities:
            if isinstance(e, api.Api):
                self.apis.append(e)
            elif isinstance(e, bre.ServiceProvider):
                self.service_providers_enterprises.append(e)
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
    
    
    def export_store_to_json(self) -> str:
        """Creates a JSON output of all the entities in Data Store.

        Returns:
            str: JSON output of all entities in Data Store.
        """
        
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
        }

        for key, object_list in object_lists.items():
            export_data[key] = parsing.export_objects(object_list)

        return json.dumps(export_data, indent=2)


    def __str__(self) -> str:
        
        entities = self.apis + self.enterprises + self.service_providers + self.groups + \
        self.trunk_groups + self.hunt_groups + self.users
            
        string = lambda e: "\n".join(map(str, e))
        
        return string(entities)
