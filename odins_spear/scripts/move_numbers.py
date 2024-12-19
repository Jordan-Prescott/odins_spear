def main(
    api,
    current_service_provider_id: str,
    current_group_id: str,
    target_service_provider_id: str,
    target_group_id: str,
    start_of_range_number: str,
    end_of_range_number: str = None,
) -> bool:
    """Moves singular or a range of numbers from one group to another located on the same Broadwork instance."""

    print(f"Removing numbers from {current_group_id}.")
    # delete number from group
    api.dns.delete_group_dns(
        current_service_provider_id,
        current_group_id,
        start_of_range_number=start_of_range_number,
        end_of_range_number=end_of_range_number,
    )

    # check if sp/ent are the same if not number needs to be removed to sys level
    if not current_service_provider_id == target_service_provider_id:
        print(f"Removing numbers from {current_service_provider_id}.")
        # remove from sp/ent
        api.dns.delete_service_provider_dns(
            current_service_provider_id,
            start_of_range_number=start_of_range_number,
            end_of_range_number=end_of_range_number,
        )

        print(
            f"Adding number to SP/ Ent: {target_service_provider_id} Group: {target_group_id}."
        )
        # assign to new group
        api.dns.post_group_dns_assign_bulk(
            target_service_provider_id,
            target_group_id,
            start_of_range_number=start_of_range_number,
            end_of_range_number=end_of_range_number,
        )
    else:
        # only when group is in the same sp/ent

        print(f"Adding number to {target_group_id}.")
        # assign to new group
        api.dns.post_group_dns(
            target_service_provider_id,
            target_group_id,
            start_of_range_number=start_of_range_number,
            end_of_range_number=end_of_range_number,
        )

    return True
