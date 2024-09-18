

def main(api, service_provider_id, group_id, user_id, device_type, 
         email, primary_device, webex_feature_pack_name):

	device_name = f"{user_id.split('@')[0]}_WBX"

	# 1 update the email & 2. update alt user id - KB

	api.put.user(
    	service_provider_id,
    	group_id, 
    	user_id,
    	{
		"emailAddress": email,
    	"alternateUserId": [
        	{
            	"alternateUserId": email,
            	"description": "Webex"
        	}
    	]
        	}    
	)
	# 3. assign feature pack - OC

	if webex_feature_pack_name:
	
		api.put.user_services(
			user_id  = user_id, 
			service_packs = [webex_feature_pack_name]
		)

	# 4. enable IMP in service settings (Micheal Clarke 04.09.24) - MC
	enableIMP = {'Integrated IMP': {'isActive': True}}
	api.put.user_service_settings(user_id=user_id, settings=enableIMP)

	# 5. build device - OC

	# 6. add device to user based on primary flag - JP
	if primary_device:
		primary_device_configuration = {
			"endpointType": "accessDeviceEndpoint",
			"accessDeviceEndpoint": {
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
		api.put.user(service_provider_id, group_id, user_id, primary_device_configuration)
	else:
		api.post.user_shared_call_appearance_endpoint(
			user_id,
			user_id.replace("@", "_WBX@"),
			device_name
		)
  
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