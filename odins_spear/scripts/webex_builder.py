def main(
    api,
    service_provider_id,
    group_id,
    user_id,
    device_type,
    email,
    primary_device,
    webex_feature_pack_name,
    enable_integarated_imp,
):
    print("Start.\n")
    # Update the email & alt user id
    email_alt_userid = {
        "emailAddress": email,
        "alternateUserId": [{"alternateUserId": email, "description": "Webex"}],
    }

    try:
        api.put.user(service_provider_id, group_id, user_id, updates=email_alt_userid)
        print("Updated email and alt user ID.")
    except Exception as e:
        print(f"\tERROR: Failed to update users email and alt user ID. Detail: {e}")

    # Assign feature pack
    try:
        if webex_feature_pack_name:
            api.put.user_services(
                user_id=user_id, service_packs=[webex_feature_pack_name]
            )
        print(f"Added feature: {webex_feature_pack_name}")
    except Exception as e:
        print(
            f"\tERROR: Failed to add feature - {webex_feature_pack_name}. Detail: {e}"
        )

    # enable IMP in service settings
    if enable_integarated_imp:
        enable_IMP = {"Integrated IMP": {"isActive": True}}
        try:
            api.put.user_service_settings(user_id=user_id, settings=enable_IMP)
            print("Enabled integrated IMP.")
        except Exception as e:
            print(f"\tERROR: Failed to enable Integrated IMP. Detail: {e}")

    # build device
    device_name = f"{user_id.split('@')[0]}_WBX"
    device_password = api.get.password_generate(service_provider_id, group_id)[
        "password"
    ]

    device_payload = {
        "useCustomUserNamePassword": "true",
        "accessDeviceCredentials": {
            "userName": device_name,
            "password": device_password,
        },
        "userName": device_name,
    }

    try:
        api.post.group_device(
            service_provider_id=service_provider_id,
            group_id=group_id,
            device_name=device_name,
            device_type=device_type,
            payload=device_payload,
        )
        print("Built device.")
    except Exception as e:
        print(f"\tERROR: Failed to build device. Detail: {e}")

    # Add device to user based on primary flag - JP
    if primary_device:
        primary_device_configuration = {
            "endpointType": "accessDeviceEndpoint",
            "accessDeviceEndpoint": {
                "accessDevice": {
                    "deviceType": device_type,
                    "deviceName": device_name,
                    "serviceProviderId": service_provider_id,
                    "groupId": group_id,
                    "deviceLevel": "Group",
                },
                "linePort": user_id,
            },
        }
        try:
            api.put.user(
                service_provider_id, group_id, user_id, primary_device_configuration
            )
            print("Added device to user as primary.")
        except Exception as e:
            print(f"\tERROR: Failed to add device as primary. Detail: {e}")
    else:
        try:
            api.post.user_shared_call_appearance_endpoint(
                user_id, user_id.replace("@", "_WBX@"), device_name
            )
            print("Added device as shared call appearance.")
        except Exception as e:
            print(f"\tERROR: Failed to add devie as shared call appearance. Detail {e}")

    # Get webex password
    try:
        password = api.get.password_generate(service_provider_id, group_id)["password"]
        api.put.user_web_authentication_password(user_id, password)
        print("Set webex password.")
    except Exception as e:
        print(f"\tERROR: Failed to set webex password. Detail {e}")

    # Return formatted data
    webex_user_details = {
        "username": email,
        "password": password,
        "primary_device": primary_device,
        "device_type": device_type,
    }

    print("\nEnd.")
    return webex_user_details
