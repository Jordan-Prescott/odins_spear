

def main(api, service_provider_id, group_id, user_id, device_type, 
         email, primary_device, webex_feature_pack_name):
    
    DEVICE_NAME = f"{user_id.split('@')[0]}_WBX"
    WEBEX_DEVICE_CONFIGURATION = {
    "endpointType": "accessDeviceEndpoint",
`    "accessDeviceEndpoint": {
     "accessDevice": {
          "deviceType": device_type,
          "deviceName": f"{user_id.split('@')[0]}_WBX",
          "serviceProviderId": service_provider_id,
          "groupId": group_id,
          "deviceLevel": "Group",
     },
     "linePort": user_id,
     }
}
`
    
    # 1. update the email - KB
    
    # 2. update alt user id - KB
    
    # 3. assign feature pack - OC
    
    # 4. enable IMP in service settings (Micheal Clarke 04.09.24) - MC
    enableIMP = {'Integrated IMP': {'isActive': True}}
    api.put.user_service_settings(user_id=user_id, settings=enableIMP)
    
    # 5. build device - OC
    device_name = f"{user_id.split('@')[0]}_WBX_{device_type.upper()}"
        
    # 6. add device to user based on primary flag - JP
    # 
    if primary_device:
       pass
    
    
    # 7. get webex password - JP
    password = api.get.passwords_generate(service_provider_id, group_id)["password"]
    api.put.user_web_authentication_password(user_id, password)
    
    # 8. return formatted data
    webex_user_details = {
         "username": email,
         "password": password,
         "primary_device": primary_device,
         "device_type": device_type
    }
    
    return webex_user_details