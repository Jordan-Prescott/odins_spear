import json


def json_to_dictionary(json_data: str):
    """Loads JSON into a Python Dict.

    Args:
        json_data (str): JSON data in a string format.

    Returns:
        Dict: Python dictionary of JSON data.
    """
    try:
        return json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None


def dictionary_to_json(python_dict: dict):
    """Takes in a Python dictionary and converts to JSON.

    Args:
        python_dict (dict): Python dictionary.

    Returns:
        Str: JSON data in string format.
    """
    try:
        return json.dumps(python_dict)
    except Exception as e:
        # Handle any exceptions that may occur during JSON encoding
        print(f"Error converting dictionary to JSON: {str(e)}")
        return None
