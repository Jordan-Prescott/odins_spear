from tqdm import tqdm

from ..exceptions import OSServiceNotAssigned


def main(api: object, service_provider_id: str) -> dict:
    """Returns a breakdown of the Trunking Call Capacity of a Service Provider/ Enterprise (SP/ENT).
    This will show the totals at each level from SP/ ENT to Group to Trunk Groups located in Groups.
    At each level Max Active Calls and Bursting Max Active calls are detailed and then differences at
    calculated.
    """

    return_data = {}

    print(f"Fetching {service_provider_id} call capacity.")

    # OSServiceNotAssigned is returned if the Trunk Group service is not assigend to SP/ ENT
    try:
        service_provider_capacity = (
            api.trunk_groups.get_service_provider_trunk_group_call_capacity(
                service_provider_id
            )
        )
    except Exception:
        raise OSServiceNotAssigned

    return_data["serviceProviderId"] = service_provider_capacity["serviceProviderId"]
    return_data["maxActiveCalls"] = service_provider_capacity["maxActiveCalls"]
    return_data["burstingMaxActiveCalls"] = service_provider_capacity[
        "burstingMaxActiveCalls"
    ]
    return_data["groupsCallCapacityTotal"] = 0
    return_data["groupsBurstingCallCapacityTotal"] = 0
    return_data["groups"] = []

    print(f"Fetching complete list of groups in {service_provider_id}.")
    groups_in_service_provider = api.groups.get_groups(service_provider_id)

    # getting groups and group call capacities
    for group in tqdm(
        groups_in_service_provider, desc="Fetching groups call capacities."
    ):
        formatted_group = {}
        formatted_group["groupId"] = group["groupId"]
        formatted_group["groupName"] = group["groupName"]

        try:
            group_capacity = api.trunk_groups.get_group_trunk_groups_call_capacity(
                service_provider_id, group["groupId"]
            )
            formatted_group["maxActiveCalls"] = group_capacity["maxActiveCalls"]
            formatted_group["burstingMaxAvailableActiveCalls"] = group_capacity[
                "burstingMaxAvailableActiveCalls"
            ]
            formatted_group["burstingMaxActiveCalls"] = group_capacity[
                "burstingMaxActiveCalls"
            ]
            formatted_group["burstingMaxAvailableActiveCalls"] = group_capacity[
                "burstingMaxAvailableActiveCalls"
            ]

            return_data["groupsCallCapacityTotal"] += group_capacity["maxActiveCalls"]
            return_data["groupsBurstingCallCapacityTotal"] += group_capacity[
                "burstingMaxAvailableActiveCalls"
            ]

        # group has no trunks and therefore fails
        except Exception:
            formatted_group["maxActiveCalls"] = 0
            formatted_group["burstingMaxAvailableActiveCalls"] = 0
            formatted_group["burstingMaxActiveCalls"] = 0
            formatted_group["burstingMaxAvailableActiveCalls"] = 0

            return_data["groupsCallCapacityTotal"] += 0
            return_data["groupsBurstingCallCapacityTotal"] += 0

        formatted_group["trunkGroups"] = []
        return_data["groups"].append(formatted_group)

    # getting trunk group capacities
    for group in tqdm(
        return_data["groups"], desc="Fetching trunk groups call capacities."
    ):
        group["trunkGroupsCallCapacityTotal"] = 0
        group["trunkGroupsBurstingCallCapacityTotal"] = 0

        try:
            group_trunk_groups = api.trunk_groups.get_group_trunk_groups(
                service_provider_id, group["groupId"]
            )
            for trunk_group in group_trunk_groups:
                trunk_group_detailed = api.trunk_groups.get_group_trunk_group(
                    service_provider_id, group["groupId"], trunk_group["name"]
                )

                group["trunkGroupsCallCapacityTotal"] += trunk_group_detailed[
                    "maxActiveCalls"
                ]

                group["trunkGroups"].append(
                    {
                        "name": trunk_group_detailed["name"],
                        "maxActiveCalls": trunk_group_detailed["maxActiveCalls"],
                        "burstingMaxActiveCalls": trunk_group_detailed[
                            "burstingMaxActiveCalls"
                        ]
                        if "burstingMaxActiveCalls" in trunk_group_detailed
                        else 0,
                    }
                )

            group["callCapacityDifference"] = (
                group["maxActiveCalls"] - group["trunkGroupsCallCapacityTotal"]
            )
            group["burstingCallCapacityDifference"] = (
                group["trunkGroupsBurstingCallCapacityTotal"]
                - group["trunkGroupsBurstingCallCapacityTotal"]
            )

        # if no trunks exist in group api call fails
        except Exception:
            group["trunkGroupsCallCapacityTotal"] = 0
            group["trunkGroupsBurstingCallCapacityTotal"] = 0
            group["callCapacityDifference"] = 0
            group["burstingCallCapacityDifference"] = 0

    # working out totals difference
    return_data["callCapacityDifference"] = (
        return_data["maxActiveCalls"] - return_data["groupsCallCapacityTotal"]
    )
    return_data["burstingCallCapacityDifference"] = (
        return_data["burstingMaxActiveCalls"]
        - return_data["groupsBurstingCallCapacityTotal"]
    )

    return return_data
