

def main(api, service_provider_id, group_id, user_id, device_type, 
         email, primary_device, webex_feature_pack_name):
    
    # 1. update the email - KB
    
    # 2. update alt user id - KB
    
    # 3. assign feature pack - OC
    
    # 4. enable IMP in service settings (Micheal Clarke 04.09.24) - MC
    enableIMP = {'Integrated IMP': {'isActive': True}}
    magic.put.user_service_settings(user_id=user_id, settings=enableIMP)
    
    # 5. build device - OC
        
    # 6. add device to user based on primary flag - JP
    
    # 7. get webex password - JP
    
    # 8. return formatted data
    '''
    username - webex
    password - webex
    primary_device
    device_type 
    '''
    
    pass