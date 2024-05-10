import re 

def find_number(number: str, number_type: str, broadwork_entities: list):
    for entity in broadwork_entities:
        if hasattr(entity, number_type) and getattr(entity, number_type) == number:
            return entity
    
    if number_type == 'aliases':
        for alias in entity.aliases:
            if re.search(rf'\b{re.escape(alias)}\b', number):
                return entity
                                     
    return None
