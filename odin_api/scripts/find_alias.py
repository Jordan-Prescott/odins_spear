import re
import time

from tqdm import tqdm

from odin_api.exceptions import AOAliasNotFound
import odin_api.logger as logger

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
    
    retry_queue = []
    max_retries = 2  
    object_with_alias = []
    
    auto_attendants = api.get.auto_attendants(service_provider_id, group_id)
    logger.log_info("List of groups Auto Attendants collected.")
    
    hunt_groups = api.get.group_hunt_groups(service_provider_id, group_id)
    logger.log_info("List of groups Hunt Groups collected.")
    
    call_centers = api.get.group_call_centers(service_provider_id, group_id)
    logger.log_info("List of groups Call Centers collected.")
    
    broadwork_entities_user_ids = []
    
    for aa in auto_attendants:
        broadwork_entities_user_ids.append(["AA", aa["serviceUserId"]])
        
    for hg in hunt_groups:
        broadwork_entities_user_ids.append(["HG", hg["serviceUserId"]])
        
    for cc in call_centers:
        broadwork_entities_user_ids.append(["CC", cc["serviceUserId"]])
        
    for broadwork_entity in tqdm(broadwork_entities_user_ids, desc="Collecting AA, HG, and CC details"):
        # add some buffer time for odins api 
        time.sleep(0.5)
        
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
            
            object_with_alias.append(formatted)
            
        except Exception:
            
            # add a retry count and add this entity to retry queue
            broadwork_entity.append(0)
            retry_queue.append(broadwork_entity)
             

    # objects failed in first instance
    logger.log_info("Retrying failed instances.")
    while retry_queue:
        entity_type, service_user_id, retry_count = retry_queue.pop(0)  # Get the first item from the queue
        try:
            if entity_type == "AA":
                temp_object = api.get.auto_attendant(service_user_id)
            elif entity_type == "HG":
                temp_object = api.get.group_hunt_group(service_user_id)
            else:
                temp_object = api.get.group_call_center(service_user_id)
        except Exception:
            if retry_count < max_retries:
                retry_queue.append((entity_type, service_user_id, retry_count + 1))  # Increment retry count and re-add to the queue
            else:
                logger.log_error(f"Failed to process {entity_type} - {service_user_id} after {max_retries} retries. Skipping.")

    for broadwork_entity in tqdm(object_with_alias, desc=f"Searching AA, HG, and CC for alias: {alias}"):
        if locate_alias(alias, broadwork_entity['aliases']):
            return f"Alias ({alias}) found: {broadwork_entity['type']} - {broadwork_entity['name']}"
        
    users = api.get.users(service_provider_id, group_id)
    logger.log_info("List of groups Users collected.")
    
    for user in tqdm(users, desc=f"Searching Users for alias: {alias}"):
         if locate_alias(alias, user['aliases']):
            return f"Alias ({alias}) found: {broadwork_entity['type']} - {broadwork_entity['name']}"

    return AOAliasNotFound