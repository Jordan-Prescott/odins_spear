import json

from odins_spear.store import broadwork_entities as bre

def json_to_dictionary(json_data: str):
    try:
        return json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None
    
    
def dictionary_to_json(python_dictionary: dict):
    try:
        json_data = json.dumps(python_dictionary)
        return json_data
    except Exception as e:
        # Handle any exceptions that may occur during JSON encoding
        print(f"Error converting dictionary to JSON: {str(e)}")
        return None
    

def auto_attendant_to_bre_object(auto_attendant: dict):
    
    
    business_menus = ("businessHoursMenu", "afterHoursMenu")
    business_hours_menu = bre.AAMenu("businessHoursMenu")
    business_hours_menu_keys = []
    after_hours_menu = bre.AAMenu("afterHoursMenu")
    after_hours_menu_keys = []
    
    for menu in business_menus:
        for key in auto_attendant[menu]["keys"]:
            pass