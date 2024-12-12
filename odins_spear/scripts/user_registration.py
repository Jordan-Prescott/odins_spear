def main(api, service_provider_id: str, group_id: str):

    # Dictionary Descripting Total Users Devices
    registrations_out = {}

    group_registration = api.get.bulk_user_registration(service_provider_id, group_id)

    users = group_registration.get("users", [])

    for user in users:

        user_id = user["profile"]["userId"]
        registrations_out[user_id] = {"registration": []}  # Initialise the dictionary

        for registration in user["data"]["registrations"]:

            device_name = registration["deviceName"]

            line_port = registration["linePort"]

            registrations_out[user_id]["registration"].append({
                "deviceName": device_name,
                "linePort": line_port,
                "registered": True,
            })
            
       
    return registrations_out