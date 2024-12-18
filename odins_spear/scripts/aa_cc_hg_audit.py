from tqdm import tqdm


def main(api, service_provider_id: str, group_id: str) -> dict:
    return_data = {"auto_attendants": [], "call_centers": [], "hunt_groups": []}

    for entity_type, api_method in [
        ("auto_attendants", api.auto_attendants.get_auto_attendants),
        ("call_centers", api.call_centers.get_group_call_centers),
        ("hunt_groups", api.hunt_groups.get_group_hunt_groups),
    ]:
        entities = api_method(service_provider_id, group_id)
        for entity in tqdm(
            entities, desc=f"Analysing {entity_type.replace("_", " ").title()}"
        ):
            services = api.services.get_user_services_assigned(entity["serviceUserId"])
            return_data[entity_type].append(
                {
                    "serviceUserId": entity["serviceUserId"],
                    "type": entity.get("type", "None"),
                    "services": services.get("userServices", []),
                }
            )

    return return_data
