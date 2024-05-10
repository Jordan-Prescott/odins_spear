import re 

def find_number(number: str, number_type: str, broadwork_entities: list):
    for entity in broadwork_entities:
        if number_type == 'phone number' and number in entity.phone_number:
            return entity
        elif number_type == 'extension' and number in entity.extension:
            return entity
        elif number_type == 'aliases':
            for alias in entity.aliases:
                if re.search(rf'\b{re.escape(alias)}\b', number):
                    return entity
                       
    return None
