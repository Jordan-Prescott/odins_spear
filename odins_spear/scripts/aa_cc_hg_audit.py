from tqdm import tqdm


def main(api, service_provider_id: str, group_id: str):
    """
    This script returns the services assigned to Auto Attendants,
    Call Centres, and Hunt Groups. Only services are applied to these
    entities and there are scenarios one would need to focus services
    assigned to these entities.

    :param service_provider_id: Service Provider ID or Enterprise ID containing the Group ID.
    :param group_id: Group ID to generate the report for.

    :return JSON: A JSON formatted report of service packs assigned to AA, CC, and HG.
    """
    print("aa_cc_hg_audit start.")
    return_data = {"autoAttendants": [], "callCenters": [], "huntGroups": []}

    for entity_type, api_method in [
        ("autoAttendants", api.auto_attendant.get_auto_attendants),
        ("callCenters", api.call_centers.get_group_call_centers),
        ("huntGroups", api.hunt_groups.get_group_hunt_groups),
    ]:
        entities = api_method(service_provider_id, group_id)
        for entity in tqdm(entities, desc=f"Analysing {entity_type.capitalize()}"):
            services = api.services.get_user_services_assigned(entity["serviceUserId"])
            return_data[entity_type].append(
                {
                    "serviceUserId": entity["serviceUserId"],
                    "type": entity.get("type", "None"),
                    "services": services.get("userServices", []),
                }
            )

    return return_data
