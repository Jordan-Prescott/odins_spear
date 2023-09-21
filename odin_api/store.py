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
            self.other_entities = [] #Non-common or custom objects

            Store.__instance = self
    
    def _add_object_to_store(self, entity, entity_type):
        if entity_type == "api" and entity not in self.apis:
            self.apis.append(entity)
        elif entity_type == "enterprise" and entity not in self.enterprises:
            self.enterprises.append(entity)
        elif entity_type == "service_provider" and entity not in self.service_providers:
            self.service_providers.append(entity)
        elif entity_type == "group" and entity not in self.groups:
            self.groups.append(entity)
        elif entity_type == "trunk_group" and entity not in self.trunk_groups:
            self.trunk_groups.append(entity)
        elif entity_type == "hunt_group" and entity not in self.hunt_groups:
            self.hunt_groups.append(entity)
        elif entity_type == "user" and entity not in self.users:
                self.users.append(entity)
        else:
            self.other_entities.append(entity)
        

    def get_group_state(group_id):
        """ takes in group id and loads group state into broadworks entities
        """
        pass

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
