import re
import time
from tqdm import tqdm

from odins_spear.exceptions import AOAliasNotFound
import odins_spear.logger as logger

def locate_alias(alias, aliases: list):
    for a in aliases:
        if re.search(rf'\b{alias}\b', a):
            return True
        

def main(api, service_provider_id: str, group_id: str, alias: str):
    """ Locates alias if assigned to broadworks entity. 

    The script searches through various entity types including Auto Attendants (AA),
    Hunt Groups (HG), and Call Centers (CC), as well as individual Users. It employs 
    a retry mechanism for instances where initial attempts to fetch entity details fail.

    The search is conducted in two phases:
    1. Collecting details of AAs, HGs, and CCs and checking for the alias.
    2. If not found, searching through the users for the alias.

    If the alias is found, the method returns a string specifying the type of entity and
    its name or userID. If the alias is not found after checking all entities, an 
    AOAliasNotFound exception is raised.

    :param service_provider_id: Service Prodiver where group is hosted.
    :param group_id: Group where alias is located.
    :param alias: Alias number to identify e.g. 0

    :return str: Returns type and name/ userId of entity where alias located. 
    :raise AOALiasNotFound: If alias not found AOAliasNotFound error raised 
    """   

    RETRY_QUEUE = []
    MAX_RETRIES = 2  
    OBJECT_WITH_ALIAS = []
    
    auto_attendants = api.get.auto_attendants(service_provider_id, group_id)
    hunt_groups = api.get.group_hunt_groups(service_provider_id, group_id)
    call_centers = api.get.group_call_centers(service_provider_id, group_id)
    
    broadwork_entities_user_ids = []
    
    for aa in auto_attendants:
        broadwork_entities_user_ids.append(["AA", aa["serviceUserId"]])
        
    for hg in hunt_groups:
        broadwork_entities_user_ids.append(["HG", hg["serviceUserId"]])
        
    for cc in call_centers:
        broadwork_entities_user_ids.append(["CC", cc["serviceUserId"]])
        
    for broadwork_entity in tqdm(broadwork_entities_user_ids, desc="Fetching AA, HG, and CC details"):
        # add some buffer time for odins api 
        
        formatted = {}
        formatted["type"] = broadwork_entity[0] 
        
        temp_object = ""
        
        try:
            if broadwork_entity[0] == "AA":
                temp_object = api.get.auto_attendant(broadwork_entity[1])
            elif broadwork_entity[0] == "HG":
                temp_object = api.get.group_hunt_group(broadwork_entity[1])
            else:
                temp_object = api.get.group_call_center(broadwork_entity[1])
                
            formatted["name"] = temp_object["serviceInstanceProfile"]["name"]
            formatted["aliases"] = temp_object["serviceInstanceProfile"]["aliases"]
            
            OBJECT_WITH_ALIAS.append(formatted)
            
        except Exception:
            # add a retry count and add this entity to retry queue
            broadwork_entity.append(0)
            RETRY_QUEUE.append(broadwork_entity)
             

    # objects failed in first instance
    if RETRY_QUEUE:
        logger.log_info("Retrying failed instances.")
    while RETRY_QUEUE:
        entity_type, service_user_id, retry_count = RETRY_QUEUE.pop(0)  # Get the first item from the queue
        
        formatted = {}
        formatted["type"] = entity_type
        temp_object = ""
        
        try:
            if entity_type == "AA":
                temp_object = api.get.auto_attendant(service_user_id)
            elif entity_type == "HG":
                temp_object = api.get.group_hunt_group(service_user_id)
            else:
                temp_object = api.get.group_call_center(service_user_id)
                
            formatted["name"] = temp_object["serviceInstanceProfile"]["name"]
            formatted["aliases"] = temp_object["serviceInstanceProfile"]["aliases"]
            
            OBJECT_WITH_ALIAS.append(formatted)
            
        except Exception:
            if retry_count < MAX_RETRIES:
                RETRY_QUEUE.append((entity_type, service_user_id, retry_count + 1))  # Increment retry count and re-add to the queue
            else:
                logger.log_error(f"Failed to process {entity_type} - {service_user_id} after {MAX_RETRIES} retries. Skipping.")

    for broadwork_entity in tqdm(OBJECT_WITH_ALIAS, desc=f"Searching AA, HG, and CC for alias {alias}"):

        if locate_alias(alias, broadwork_entity['aliases']):
            return f"""
        Alias ({alias}) found: {broadwork_entity['type']} - {broadwork_entity['name']}"""
        
    users = api.get.users(service_provider_id, group_id, extended=True)
    logger.log_info("Fetched users.")
    
    for user in tqdm(users, desc=f"Searching Users for alias: {alias}"):

        if locate_alias(alias, user['aliases']):
            return f"\n\n\tAlias ({alias}) found: User - {user['userId']}"
    
    return f"\n\n\tAlias ({alias}) not found."