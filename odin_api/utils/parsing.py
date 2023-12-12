import json

from dataclasses import is_dataclass, fields
from typing import List, Any, Dict

from odin_api.store.broadwork_entities import *

#TODO: for small objects that dont need custom parsing could be grouped into edge objects function

def camel_case(s):
    parts = iter(s.split('_'))
    return next(parts) + ''.join(i.capitalize() for i in parts)

def serialise_service_provider() -> str:
    pass

def serialise_group() -> str:
    pass

def serialise_trunk_group() -> str:
    pass

def serialise_aa_key() -> str:
    pass

def serialise_aa_menu() -> str:
    pass

def serialise_auto_attendant() -> str:
    pass

def serialise_hunt_group() -> str:
    pass

def serialise_user(user, return_json:bool = False) -> str:
   #TODO: TrunkAddressing needs addressing. Not sure what data that is aimed at object doesnt store data needed.
   
    serialised_user = {}
    
    for field in fields(user):
        value = getattr(user, field.name)
        
        if isinstance(value, list):
            if field.name == "aliases":
                serialised_user[field.name] = value
            elif field.name == "alternate_user_id":
                serialised_user[camel_case(field.name)] = [
                    {"description": a, "alternateUserId": a}
                    for a in value
                ]         
        elif is_dataclass(value):
            if isinstance(value, Department):
                serialised_user["department"] = serialise_department(value)
            elif isinstance(value, Device):
                serialised_user["accessDeviceEndpoint"] = serialise_device(value)  
            elif isinstance(value, Address):
                serialised_user["address"] = serialise_address(value)
            elif isinstance(value, TrunkGroup):
                serialised_user["trunkAddressing"] = serialise_trunk_group(value)
        else:
            serialised_user[camel_case(field.name)] = value
              
    if return_json:
        return json.dumps(serialised_user)
    return serialised_user

def serialise_device() -> str:
    pass

def serialise_contact(contact, return_json:bool = False) -> str:
    
    data = {}
    
    for field in fields(contact):
        value = getattr(contact, field.name)
        data[camel_case(field.name)] = value
        
    if return_json:
        return json.dumps(data)
    return data

def serialise_address(address, return_json:bool = False) -> str:
    
    data = {}
    
    for field in fields(address):
        value = getattr(address, field.name)
        data[camel_case(field.name)] = value
        
    if return_json:
        return json.dumps(data)
    return data

def serialise_department(department, return_json:bool = False) -> str:
    
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
