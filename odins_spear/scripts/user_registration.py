def main(api, service_provider_id: str, group_id: str):
    # Dictionary Descripting Total Users Devices
    registrations_out = {}

    group_registration = api.regsitration.get_bulk_user_registration(
        service_provider_id, group_id
    )

    users = group_registration.get("users", [])

    for user in users:
        user_id = user["profile"]["userId"]
        registrations_out[user_id] = {"registration": {}}  # Initialise the dictionary

        for registration in user["data"]["registrations"]:
            device_name = registration["deviceName"]

            registrations_out[user_id]["registration"][device_name] = {
                "registered": True
            }  # All devices listed under the "registrations" attribute must be registered, so always True.

    return registrations_out
