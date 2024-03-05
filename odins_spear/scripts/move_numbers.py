from tqdm import tqdm

import odins_spear.logger as logger

def main(api, current_service_provider_id: str, current_group_id: str, target_service_provider_id: str, 
         target_group_id: str, start_of_range_number: str, end_of_range_number: str = None) -> bool:
    
    # delete number from group
    api.delete.group_dns(
        current_service_provider_id,
        current_group_id,
        start_of_range_number = start_of_range_number,
        end_of_range_number = end_of_range_number
    )
    
    # check if sp/ent are the same if not number needs to be removed to sys level
    if not current_service_provider_id == target_service_provider_id:
        
        # remove from sp/ent
        api.delete.service_provider_dns(
            current_service_provider_id,
            start_of_range_number = start_of_range_number,
            end_of_range_number = end_of_range_number
        )
        
        # assign to new sp/ent
        api.post.service_provider_dns(
            target_service_provider_id,
            start_of_range_number = start_of_range_number,
            end_of_range_number = end_of_range_number
        )
        
        # assign to new group
        api.post.group_dns(
            target_service_provider_id,
            target_group_id,
            start_of_range_number = start_of_range_number,
            end_of_range_number = end_of_range_number
        )
    else:
    # only when group is in the same sp/ent    
        
        # assign to new group
        api.post.group_dns(
            target_service_provider_id,
            target_group_id,
            start_of_range_number = start_of_range_number,
            end_of_range_number = end_of_range_number
        )
    
    return True