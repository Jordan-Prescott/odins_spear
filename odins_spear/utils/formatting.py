from ..exceptions import *

def format_filter_value(type, value):
    """_summary_

    Args:
        type (_type_): _description_
        value (_type_): _description_

    Raises:
        OAUnsupportedFilter: _description_

    Returns:
        _type_: _description_
    """
    if type.lower() == "equal to":
        return f"{value}" 
    elif type.lower() == "starts with":
        return f"{value}*" 
    elif type.lower() == "contains":
        return f"*{value}*"
    else:
        raise OSUnsupportedFilter
    
    
def format_int_list_of_numbers(counrty_code: int, numbers: list):
    """_summary_

    Args:
        counrty_code (int): _description_
        numbers (list): _description_

    Returns:
        _type_: _description_
    """
    numbers.sort()
    
    formatted_numbers = [f'+{str(counrty_code)}-{str(num)}' for num in numbers]
    return formatted_numbers