import json

def json_to_dictionary(json_data: str):
    try:
        return json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None
    
    
def dictionary_to_json(python_dictionary):
    try:
        json_data = json.dumps(python_dictionary)
        return json_data
    except Exception as e:
        # Handle any exceptions that may occur during JSON encoding
        print(f"Error converting dictionary to JSON: {str(e)}")
        return None