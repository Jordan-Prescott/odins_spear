from exceptions import OSExtensionNotFound

def retrieve_extensions( api, service_provider_id: str, group_id: str ) -> list:
    
    extensions = []

    dataset = (
       api.get.users( service_provider_id, group_id )              +
       api.get.group_hunt_groups( service_provider_id, group_id )  +
       api.get.group_call_centers( service_provider_id, group_id ) +
       api.get.auto_attendants( service_provider_id, group_id )
    )

    for data in dataset:
        if not data['extension']:
            continue

        extensions.append(int(data['extension']))

    return extensions if extensions else None

def main( api, service_provider_id: str, group_id: str, range_start: int, range_end: int ):
    '''Retrieves The Lowest Free Extension Available In The Designated Group Passed.
    '''

    if range_start > range_end:
        initial_range = range_end

        range_end = range_start
        range_start = initial_range

    # Retrieve List Of Occupied Extensions Within The Group
    extensions = retrieve_extensions(
        api,
        service_provider_id,
        group_id,
    )

    for extension in range(range_start, range_end + 1):
        if extension not in extensions:
            return {'extension': extension}

    raise OSExtensionNotFound
    

    

