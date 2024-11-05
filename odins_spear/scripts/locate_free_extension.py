
def retrieve_extensions(
    api,
    service_provider_id: str,
    group_id: str
) -> list:
    
    extensions = []

    dataset = api.get.users(
        service_provider_id,
        group_id
    )

    for data in dataset:
        if not data['extension']:
            continue
    ###

        extensions.append(data['extension'])

    dataset = api.get.group_hunt_groups(
        service_provider_id,
        group_id
    )

    for data in dataset:
        if not data['extension']:
            continue
    ###

        extensions.append(data['extension'])

    dataset = api.get.group_call_centers(
        service_provider_id,
        group_id
    )

    for data in dataset:
        if not data['extension']:
            continue
    ###

        extensions.append(data['extension'])

    dataset = api.get.auto_attendants(
        service_provider_id,
        group_id
    )

    for data in dataset:
        if not data['extension']:
            continue

        extensions.append(data['extension'])
    ###

    if not extensions:
        return
    
    return extensions
###

def main(
    api,
    service_provider_id,
    group_id,
    field: list
):
    '''
    Retrieves The Lowest Free Extension Available In The Designated Group Passed.

    field is passed as such [100, 1000]
    '''
    ### Retrieve List Of Occupied Extensions Within The Group
    extensions = retrieve_extensions(
        api,
        service_provider_id,
        group_id,
    )

    ### Cull Out Of Range Extensions
    for extension in extensions:

        if field[0] < extension and field[1] > extension:
            continue

        extensions.remove(extension)
    ###

    ### Locate Initial Free Extension
    extension_set = set(extensions)

    for extension in range(field[0] + 1, field[1]):
        if extension not in extension_set:
            return extension
    ####

    print("Unable To Locate A Free Extension Within The Range")
    return    
    

    

