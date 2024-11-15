def main(api, service_provider_id: str, group_id: str):

    registrations_out = {}
    users = api.get.users(service_provider_id, group_id)

    for user in users:

        registration_info = api.get.user_registration(
            user["userId"]
        )

        registrations_out[user["userId"]] = {}

        DeviceID = 1

        for registration_entry in registration_info["registrations"]:

            is_registered = "False"

            if registration_entry["linePort"]:
                is_registered = "True"

            registrations_out[user["userId"]][f"DeviceID: {DeviceID}"] = {
                "LinePort": registration_entry["linePort"],
                "Device": registration_entry["deviceName"],
                "Registered": is_registered
            }

            DeviceID += 1
    return registrations_out