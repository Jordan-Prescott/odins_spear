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
    
    highest_number = 0
    formatted_numbers = []
    
    for num in numbers:
        if num > highest_number:
            pass