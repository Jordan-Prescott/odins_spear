
from odin_api.utils.exceptions import *

def format_filter(self, filter, type, value):
          
    if type.lower() == "equal to":
        return f"{filter}={value}" 
    elif type.lower() == "starts with":
        return f"{filter}={value}*" 
    else: #contains
        return f"{filter}=*{value}*"