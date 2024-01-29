from tqdm import tqdm

import odins_spear.logger as logger

def main(api, service_provider_id: str, group_id: str, user_id: str):
    """ identify a user's associations with Call Centers (CC), Hunt Groups (HG), 
    and Pick Up Groups.
    
    Args:
        service_provider_id (str): Service Provider where the group is hosted.
        group_id (str): Group where the User is located.
        user_id (str): Target user ID.
        
        
    Returns:
        str: Formatted output of the user showing all CC, HG, and Pick Up user is assigned to.
    """
    
    USER_DATA = {
        "user_id": user_id,
        "first_name": None,
        "last_name": None,
        "extension": None,
        "phone_number": None,
        "services": None,
        "feature_packs": None,
        "hunt_groups": [],
        "call_centers": [],
        "pick_up_group": None
    }
    
    user = api.get.user_report(user_id)
    USER_DATA["first_name"] = user["firstName"]
    USER_DATA["last_name"] = user["lastName"]
    USER_DATA["extension"] = user["extension"]
    USER_DATA["phone_number"] = user["phoneNumber"]
    USER_DATA["services"] = user["userServices"]
    USER_DATA["feature_packs"] = user["servicePacks"]
    
    
    pick_up_group = api.get.call_pickup_group_user(service_provider_id, group_id, user_id)
    USER_DATA["pick_up_group"] = pick_up_group[0]["name"]
    
    hunt_groups = api.get.group_hunt_group_user(service_provider_id, group_id, user_id)
    for hg in hunt_groups:
        USER_DATA["hunt_groups"].append(hg["serviceUserId"])
    
    call_centers = api.get.user_call_center(user_id)
    for cc in call_centers["callCenters"]:
        USER_DATA["call_centers"].append(cc["serviceUserId"])
        
    print("User Data:")
    for key, value in USER_DATA.items():
        if isinstance(value, list):
            value = ', '.join(map(str, value))
        elif value is None:
            value = "N/A"
        print(f"\t{key.replace('_', ' ').title()}: {value}")