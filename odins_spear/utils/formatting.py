from odins_spear.exceptions import *

def format_filter(filter, type, value):
    if type.lower() == "equal to":
        return f"{filter}={value}" 
    elif type.lower() == "starts with":
        return f"{filter}={value}*" 
    elif type.lower() == "contains":
        return f"{filter}=*{value}*"
    else:
        raise OAUnsupportedFilter
    
    
def format_list_of_numbers(counrty_code: int, numbers: list):
    numbers.sort()
    
    formatted_numbers = [f'+{str(counrty_code)}-{str(num)}' for num in numbers]
    return formatted_numbers