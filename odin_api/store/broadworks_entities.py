from odin_api.store.data_store import DataStore
from typing import List


class ServiceProvider:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self.groups: List[Group] = []

        DataStore.get_instance()._add_object_to_store(self, "service_provider")

    def __str__(self):
        return f"Service Provider - id: {self._id}, name: {self._name}, groups: {self.groups}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        if len(new_id) >= 1 and len(new_id) <= 30:
            self._id = new_id

    @id.deleter
    def id(self):
        del self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) >= 1 and len(new_name) <= 80:
            self._name = new_name

    @name.deleter
    def nameid(self):
        del self._name


class Enterprise(ServiceProvider):
    def __init__(self, id, name):

        # JP: Assuemed that ent has all functionality and SP has a subset
        super().__init__(id, name)

        DataStore.get_instance()._add_object_to_store(self, "enterprise")

    def __str__(self):
        return f"Enterprise - id: {self.id}, name: {self.name}, groups: {self.groups}"


class Group:
    def __init__(self, enterprise, id, name, domain, main_number):
        self.enterprise = enterprise
        self._id = id
        self._name = name
        self._domain = domain
        self._main_number = main_number

        self.users: List[User] = []
        self.hunt_groups: List[HuntGroup] = []
        self.trunk_groups: List[TrunkGroup] = []

        self.enterprise.groups.append(self)

        DataStore.get_instance()._add_object_to_store(self, "group")

    def __str__(self):
        return f"Group - enterprise: {self.enterprise.name}, id: {self.id}, name: {self.name}, domain: {self.domain}, " \
               f"users: {self.users}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        if len(new_id) >= 1 and len(new_id) <= 30:
            self._id = new_id

    @id.deleter
    def id(self):
        del self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) >= 1 and len(new_name) <= 80:
            self._name = new_name

    @name.deleter
    def nameid(self):
        del self._name

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, new_domain):
        if len(new_domain) >= 1 and len(new_domain) <= 80:
            self._domain = new_domain

    @domain.deleter
    def nameid(self):
        del self._domain

    @property
    def main_number(self):
        return self._main_number

    @main_number.setter
    def main_number(self, new_number):
        if len(new_number) >= 1 and len(new_number) <= 23:
            self._main_number = new_number

    @main_number.deleter
    def main_number(self):
        del self._main_number


class TrunkGroup(Group):
    def __init__(self, group, name, device, number, users=None):
        self.group = group
        self.name = name
        self.device = device
        self.number = number
        self.users: List[User] = users if users else []

        DataStore.get_instance()._add_object_to_store(self, "trunk_group")

    def __str__(self):
        return f"Trunk Group - group: {self.group.name}, name: {self.name}, device: {self.device} " \
               f"users: {self.users}"


class HuntGroup(Group):
    def __init__(self, group, name, extension, id, number=None, users=None):
        self.group = group
        self.name = name
        self.extension = extension
        self.id = id
        self.number = number
        self.users: List[User] = users if users else []

        DataStore.get_instance()._add_object_to_store(self, "hunt_group")

    def __str__(self):
        return f"Hunt Group - group: {self.group.name}, name: {self.name}, extension: {self.extension} " \
               f"id: {self.id} users: {self.users}"


class User:
    def __init__(self, group: Group, id: str, first_name, last_name, extension):
        self.group = group
        self._id = id 
        self._first_name = first_name
        self._last_name = last_name
        self._extension = extension

        self.group.users.append(self)

        DataStore.get_instance()._add_object_to_store(self, "user")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        if len(new_id) >= 1 and len(new_id) <= 30:
            self._id = new_id

    @id.deleter
    def id(self):
        del self._id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_f_name):
        if len(new_f_name) >= 1 and len(new_f_name) <= 30:
            self._first_name = new_f_name

    @first_name.deleter
    def first_name(self):
        del self._first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_l_name):
        if len(new_l_name) >= 1 and len(new_l_name) <= 30:
            self._last_name = new_l_name

    @last_name.deleter
    def last_name(self):
        del self._last_name

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, new_ext):
        if len(new_ext) >= 1 and len(new_ext) <= 20:
            self._extension = new_ext

    @extension.deleter
    def extension(self):
        del self._extension

    def __str__(self):
        return f"User - group: {self.group.name}, first Name: {self.first_name}, last Name: {self.last_name}, " \
               f"extension: {self.extension}, id: {self.id}"