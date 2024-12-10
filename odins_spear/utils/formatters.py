from .checkers import check_type_filter


def format_filter_value(filter_type, filter_value):
    """Takes in a filter type and the value to filter for. Depenining on the type
    the value is formatted with the correct wild card e.g. 'contains' will add a
    wildcard to the start and end of value *value*

    Args:
        type (str): Either 'equal to', 'contains', 'starts with'
        value (str): value to filter for

    Raises:
        OAUnsupportedFilter: Raised when unsupported filter is requested such as 'ends with'

    Returns:
        str: Formatted filter with the value and correct filter wildcards.
    """

    check_type_filter(filter_type, filter_value)

    filter_type = filter_type.lower()
    if filter_type == "equal to":
        return f"{filter_value}"
    elif filter_type == "starts with":
        return f"{filter_value}*"
    elif filter_type == "contains":
        return f"*{filter_value}*"


def format_int_list_of_numbers(counrty_code: int, numbers: list):
    """Takes a list of integer numbers with no country code and the country code needed.
    This will then return a list of strings with the country code inserted infront of all
    numbers in orginal list.

    Args:
        counrty_code (int): Country code to be added infront of all numbers in list
        numbers (list): List of integer numbers with no country code

    Returns:
        list: List of numbers in string format with the country code added.
    """
    numbers.sort()
    formatted_numbers = [f"+{str(counrty_code)}-{str(num)}" for num in numbers]
    return formatted_numbers


def format_service_instance_profile(data: dict):
    """Adds a blank dict if serviceInstanceProfile is not in data but needed

    Args:
        data (dict): Data to check if serviceInstanceProfile is in
    """

    return data.setdefault("serviceInstanceProfile", {})