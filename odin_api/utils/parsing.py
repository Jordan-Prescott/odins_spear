import json

from dataclasses import is_dataclass, fields
from typing import List, Any, Dict, Type

from .bre_profile_matrix import MATRIX

def camel_case(s):
    parts = iter(s.split('_'))
    return next(parts) + ''.join(i.capitalize() for i in parts)


def serialise_user(user) -> str:
    data = MATRIX["USER"]
    
    for field in fields(user):
        value = getattr(user, field.name)
        
        if is_dataclass(value):
            continue
            serialized_value = serialize_dataclass(value)
            if serialized_value is not None:
                data[camel_case(field.name)] = serialized_value
        elif isinstance(value, list) and value and is_dataclass(value[0]):
            continue
            serialized_list = [serialize_dataclass(item) for item in value]
            data[camel_case(field.name)] = serialized_list
        else:
            data[camel_case(field.name)] = value
        


def serialize_dataclass(instance: Any, visited: set = None) -> Dict:
    if visited is None:
        visited = set()

    if id(instance) in visited:
        return None  # Skip already visited objects

    visited.add(id(instance))

    result = {}

    for field in fields(instance):
        value = getattr(instance, field.name)

        if is_dataclass(value):
            # serialized_value = serialize_dataclass(value, visited)
            # if serialized_value is not None:
            #     result[camel_case(field.name)] = serialized_value
            continue
        elif isinstance(value, list) and value and is_dataclass(value[0]):
            serialized_list = [serialize_dataclass(item, visited) for item in value]
            result[camel_case(field.name)] = serialized_list
        else:
            result[camel_case(field.name)] = value

    return result


def json_to_oa_object():
    return























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
