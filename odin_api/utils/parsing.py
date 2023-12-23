import json

from odin_api.utils.exceptions import *

def format_filter(self, filter, type, value):

    if type.lower() == "equal to":
        return f"{filter}={value}" 
    elif type.lower() == "starts with":
        return f"{filter}={value}*" 
    elif type.lower() == "contains":
        return f"{filter}=*{value}*"
    else:
        raise OAUnsupportedFilter















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
