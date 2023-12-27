import json

from odin_api.exceptions import *

def format_filter(filter, type, value):

    if type.lower() == "equal to":
        return f"{filter}={value}" 
    elif type.lower() == "starts with":
        return f"{filter}={value}*" 
    elif type.lower() == "contains":
        return f"{filter}=*{value}*"
    else:
        raise OAUnsupportedFilter
