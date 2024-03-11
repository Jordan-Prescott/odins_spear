import json

from tqdm import tqdm

import odins_spear.logger as logger

def main(api: object, service_provider_id: str):
    
    """
    
    service_provider_trunk_group_call_capacity
    
    
    {{url}}/api/v2/groups?serviceProviderId=ent.odin
    group_trunk_group_call_capacity
    group_trunk_groups
    group_trunk_group
    
    """
    
    return_data = {}
    
    logger.log_info(f"Fetching {service_provider_id} call capacity.")
    service_provider_capacity = api.get.service_provider_trunk_group_call_capacity(service_provider_id)
    return_data["serviceProviderId"] = service_provider_capacity["serviceProviderId"]
    return_data["maxActiveCalls"] = service_provider_capacity["maxActiveCalls"]
    return_data["burstingMaxActiveCalls"] = service_provider_capacity["burstingMaxActiveCalls"]
    return_data["GroupsCallCapacityTotal"] = 0
    return_data["GroupsBurstingCallCapacityTotal"] = 0
    return_data["groups"] = []
    
    logger.log_info(f"Fetching complete list of groups in {service_provider_id}.")
    groups_in_service_provider = api.get.groups(service_provider_id)
    
    # getting groups and group call capacities
    for group in tqdm(groups_in_service_provider, desc="Fetching groups call capacities."):
        formatted_group = {}
        formatted_group["groupId"] =  group["groupId"]
        formatted_group["groupName"] =  group["groupName"]
        
        group_capacity = api.get.group_trunk_groups_call_capacity(service_provider_id, group["groupId"])
        formatted_group["maxActiveCalls"] =  group_capacity["maxActiveCalls"]
        formatted_group["burstingMaxAvailableActiveCalls"] =  group_capacity["burstingMaxAvailableActiveCalls"]
        formatted_group["burstingMaxActiveCalls"] =  group_capacity["burstingMaxActiveCalls"]
        formatted_group["burstingMaxAvailableActiveCalls"] =  group_capacity["burstingMaxAvailableActiveCalls"]
        
        return_data["GroupsCallCapacityTotal"] += group_capacity["maxActiveCalls"]
        return_data["GroupsBurstingCallCapacityTotal"] += group_capacity["burstingMaxAvailableActiveCalls"]
        
        formatted_group["trunkGroups"] = []
        
        return_data["groups"].append(formatted_group)
    
    # getting trunk group capacities
    for group in tqdm(return_data["groups"], desc="Fetching trunk groups call capacities."):
        group["trunkGroupsCallCapacityTotal"] = 0
        group["trunkGroupsBurstingCallCapacityTotal"] = 0
        
        group_trunk_groups = api.get.group_trunk_groups(service_provider_id, group["groupId"])
        
        for trunk_group in group_trunk_groups:
            
            trunk_group_detailed = api.get.group_trunk_group(service_provider_id, group, trunk_group["name"])
            
            group["trunkGroupsCallCapacityTotal"] += trunk_group_detailed["maxActiveCalls"]
            group["trunkGroupsBurstingCallCapacityTotal"] += trunk_group_detailed["burstingMaxActiveCalls"]
            
            group["trunkGroups"].append(
                {
                    "maxActiveCalls": trunk_group_detailed["maxActiveCalls"],
                    "burstingMaxActiveCalls": trunk_group_detailed["burstingMaxActiveCalls"] if "burstingMaxActiveCalls" in trunk_group_detailed else 0
                }
            )
        
        group["callCapacityDifference"] = group["maxActiveCalls"] - group["trunkGroupsCallCapacityTotal"]
        group["BurstingCallCapacityDifference"] = group["trunkGroupsBurstingCallCapacityTotal"] - group["trunkGroupsBurstingCallCapacityTotal"]
          
    # working out totals difference 
    return_data["callCapacityDifference"] = return_data["maxActiveCalls"] - return_data["GroupsCallCapacityTotal"]
    return_data["BurstingCallCapacityDifference"] = return_data["burstingMaxActiveCalls"] - return_data["GroupsBurstingCallCapacityTotal"]
        
    return json.dumps(return_data)
    