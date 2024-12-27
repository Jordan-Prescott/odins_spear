def main(
    api,
    current_service_provider_id: str,
    current_group_id: str,
    start_of_range_number: str,
    end_of_range_number: str = None,
) -> bool:
    """Removes a singular or a range of numbers from a Broadworks instance."""

    print(f"Removing numbers from {current_group_id}.")
    # delete number from group
    api.dns.delete_group_dns(
        current_service_provider_id,
        current_group_id,
        start_of_range_number=start_of_range_number,
        end_of_range_number=end_of_range_number,
    )

    print(f"Removing numbers from {current_service_provider_id}.")
    # remove from sp/ent
    api.dns.delete_service_provider_dns(
        current_service_provider_id,
        start_of_range_number=start_of_range_number,
        end_of_range_number=end_of_range_number,
    )

    return True
