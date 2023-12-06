import json

from dataclasses import is_dataclass, fields
from typing import List, Any, Dict

from odin_api.store.broadwork_entities import *

#TODO: for small objects that dont need custom parsing could be grouped into edge objects function

def camel_case(s):
    parts = iter(s.split('_'))
    return next(parts) + ''.join(i.capitalize() for i in parts)

def serialize_service_provider() -> str:
    pass

def serialize_group() -> str:
    pass

def serialize_trunk_group() -> str:
    pass

def serialize_aa_key() -> str:
    pass

def serialize_aa_menu() -> str:
    pass

def serialize_auto_attendant() -> str:
    pass

def serialize_hunt_group() -> str:
    pass

def serialise_user(user, return_json:bool = False) -> str:
   
    data = {}
    
    for field in fields(user):
        value = getattr(user, field.name)
        
        if isinstance(value, list) and value and is_dataclass(value[0]):
            
            #TODO: Add in logic for alternateUserId, aliases
            
            if value == "aliases":
                # serialized_list = [serialize_dataclass(item) for item in value]
                # data[camel_case(field.name)] = serialized_list
                pass
        elif is_dataclass(value):
            if isinstance(value, Department):
                data["department"] = serialize_department(value)
            elif isinstance(value, Device):
                data["accessDeviceEndpoint"] = serialize_device(value)  
            elif isinstance(value, Address):
                data["address"] = serialize_address(value)
            elif isinstance(value, TrunkGroup):
                data["trunkAddressing"] = serialize_trunk_group(value)
        else:
            data[camel_case(field.name)] = value
            
            
    if return_json:
        return json.dumps(data)
    return data

def serialize_device() -> str:
    pass

def serialize_contact(contact, return_json:bool = False) -> str:
    
    data = {}
    
    for field in fields(contact):
        value = getattr(contact, field.name)
        data[camel_case(field.name)] = value
        
    if return_json:
        return json.dumps(data)
    return data

def serialize_address(address, return_json:bool = False) -> str:
    
    data = {}
    
    for field in fields(address):
        value = getattr(address, field.name)
        data[camel_case(field.name)] = value
        
    if return_json:
        return json.dumps(data)
    return data

def serialize_department(department, return_json:bool = False) -> str:
    
    data = {}
    
    for field in fields(department):
        value = getattr(department, field.name)
        data[camel_case(field.name)] = value
        
    if return_json:
        return json.dumps(data)
    return data
    



        


















def export_objects(object_list: List) -> List[dict]:
    """_summary_

    Args:
        object_list (List): _description_

    Returns:
        List[dict]: _description_
    """
    exported_objects = []

    for obj in object_list:
        exported_object = {
            'type': obj.__class__.__name__,
            'data': self.export_object_data(obj)
        }
        exported_objects.append(exported_object)

    return exported_objects

def export_object_data(obj) -> dict:
    """_summary_

    Args:
        obj (_type_): _description_

    Returns:
        dict: _description_
    """
    object_data = {}

    # Add attributes
    for attr, value in vars(obj).items():
        object_data[attr] = value

    # Add relationships (if applicable)
    if hasattr(obj, 'groups'):
        object_data['groups'] = self.export_objects(obj.groups)
    # Add other relationships as needed

    return object_data
