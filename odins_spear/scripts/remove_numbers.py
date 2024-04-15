import odins_spear.utils.loggers as loggers

def main(api, current_service_provider_id: str, current_group_id: str,
         start_of_range_number: str, end_of_range_number: str = None) -> bool:
    """Removes a singular or a range of numbers from a Broadworks instance.
    """
    
    loggers.log_info(f"Removing numbers from {current_group_id}.")
    # delete number from group
    api.delete.group_dns(
        current_service_provider_id,
        current_group_id,
        start_of_range_number = start_of_range_number,
        end_of_range_number = end_of_range_number
    )

    loggers.log_info(f"Removing numbers from {current_service_provider_id}.")
    # remove from sp/ent
    api.delete.service_provider_dns(
        current_service_provider_id,
        start_of_range_number = start_of_range_number,
        end_of_range_number = end_of_range_number
    )

    return True