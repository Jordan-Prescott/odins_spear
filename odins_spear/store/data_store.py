from typing import List
import json

from ..api import API
from ..utils import parsers
from . import broadwork_entities as bre


class DataStore:
    """Local store of objects, when each object is instantiated it is added to
    the appropriate list.

    Singleton design pattern to get store use get_instance().
    """

    def __init__(self):
        self.apis: List[API] = []
        self.service_providers_enterprises: List[bre.ServiceProvider] = []
        self.groups: List[bre.Group] = []
        self.trunk_groups: List[bre.TrunkGroup] = []
        self.auto_attendants: List[bre.AutoAttendant] = []
        self.call_centers: List[bre.CallCenter] = []
        self.hunt_groups: List[bre.HuntGroup] = []
        self.users: List[bre.User] = []
        self.devices: List[bre.Device] = []
        self.other_entities = []  # Non-common or custom objects

    def build_id_mapping(self):
        """
        Builds mapping of numbers IDs to entity.

        Example: {test@test.com: User, customID: CallCenter}
        """

        self.id_mapping = {}

        entities = (
            self.auto_attendants + self.call_centers + self.hunt_groups + self.users
        )

        for e in entities:
            try:
                self.id_mapping[e.id] = e
            except Exception:
                self.id_mapping[e.service_user_id] = e

    def build_number_mapping(self):
        """
        Builds mapping of numbers (phone numbers, extension, aliases) to entity.

        Example: {101: User, +1-123456789: CallCenter}
        """
        import re

        self.number_mapping = {}

        entities = (
            self.auto_attendants + self.call_centers + self.hunt_groups + self.users
        )

        for e in entities:
            if e.phone_number:
                self.number_mapping[e.phone_number] = e
            if e.extension:
                self.number_mapping[e.extension] = e
            if e.aliases:
                for a in e.aliases:
                    number = re.search(r"\d+", a).group()
                    self.number_mapping[number] = e

    def store_objects(self, *entities) -> None:
        """Takes in objects within the odin_api and custom and stores in lists
        depending on type.

        :param entity: broadwork entities used in odin_api
        """

        for e in entities:
            if isinstance(e, API):
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

    def export_store(self) -> str:
        """Export all objects in the store and their relationships in JSON format."""
        export_data = {}
        object_lists = {
            "apis": self.apis,
            "service_providers": self.service_providers,
            "enterprises": self.enterprises,
            "groups": self.groups,
            "trunk_groups": self.trunk_groups,
            "auto_attendants": self.auto_attendants,
            "call_centers": self.call_centers,
            "hunt_groups": self.hunt_groups,
            "users": self.users,
            "devices": self.devices,
            "other_entities": self.other_entities,
        }

        for key, object_list in object_lists.items():
            export_data[key] = parsers.export_objects(object_list)

        return json.dumps(export_data, indent=2)

    def __str__(self) -> str:
        """returns complete list of entities in store."""
        entities = (
            self.apis
            + self.enterprises
            + self.service_providers
            + self.groups
            + self.trunk_groups
            + self.hunt_groups
            + self.users
        )

        # loops entities and joins into string
        string = lambda e: "\n".join(map(str, e))
        return string(entities)
