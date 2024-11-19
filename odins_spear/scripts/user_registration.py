from exceptions import OSObjectParseError

def main( api, service_provider_id: str, group_id: str ):

    # Dictionary Descripting Total Users Devices
    registrations_out = {}

    users = api.get.users(
        service_provider_id,
        group_id
    )

    if not users:
        raise OSObjectParseError

    for user in users:

        registration_info = api.get.user_registration(
            user["userId"]
        )

        registrations_out[user["userId"]] = {}

        device_identifier = 1

        for registration_entry in registration_info["registrations"]:

            is_registered = "False"

            if registration_entry["linePort"]:
                is_registered = "True"

            registrations_out[user["userId"]][f"deviceId: {device_identifier}"] = {
                "linePort":     registration_entry["linePort"],
                "deviceName":   registration_entry["deviceName"],
                "isRegistered": is_registered
            }

            device_identifier += 1

    return registrations_out