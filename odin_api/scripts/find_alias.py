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
    
    auto_attendants = api.get.auto_attendants()
    aa_service_user_ids = []
    
    for aa in auto_attendants:
        aa_service_user_ids.append(aa["serviceUserId"])
    
    
    return 