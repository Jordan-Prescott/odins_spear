import re

from odin_api.exceptions import AOAliasNotFound

def locate_alias(alias, aliases: list):

    for alias in aliases:
        if re.search(rf'\b{alias}\b', alias):
            return True
        

def main(api, service_provider_id, group_id, alias):
    """ Locates alias if assigned to broadworks entity. 

    Checks:
    - Auto Attendants
    - Call Centers
    - Hunt Groups
    - Users

    :param x:
    :param y:
    :param z:

    :return r:
    """
    
    
    
    # 1. Auto attendant 
    # 2. Hunt Groups
    # 3. Users    
    
    object_with_alias = []
    
    auto_attendants = api.get.auto_attendants(service_provider_id, group_id)
    aa_service_user_ids = []
    for aa in auto_attendants:
        aa_service_user_ids.append(aa["serviceUserId"])
    
    for aa in aa_service_user_ids:
        aa_formatted = {}
        
        auto_attendant = api.get.auto_attendant(aa)
        
        aa_formatted["type"] = "AA"
        aa_formatted["name"] = auto_attendant["serviceInstanceProfile"]["name"]
        aa_formatted["aliases"] = auto_attendant["serviceInstanceProfile"]["aliases"]
        
        object_with_alias.append(aa_formatted)
        
    for aa in object_with_alias:
        if locate_alias(alias, aa['aliases']):
            return f"Alias ({alias}) found: {aa['type']} - {aa['name']}"

    return AOAliasNotFound