import json

def json_to_dictionary(json_data: str):
    try:
        return json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return False