from tqdm import tqdm


def main(api, service_provider_id: str, group_id: str, user_id: str):
    """identify a user's associations with Call Centers (CC), Hunt Groups (HG),
    and Pick Up Groups.

    Args:
        service_provider_id (str): Service Provider where the group is hosted.
        group_id (str): Group where the User is located.
        user_id (str): Target user ID.

    Returns:
        str: Formatted output of the user showing all CC, HG, and Pick Up user is assigned to.
    """

    USER_DATA = {
        "userId": user_id,
        "firstName": None,
        "lastName": None,
        "extension": None,
        "phoneNumber": None,
        "aliases": None,
        "services": None,
        "featurePacks": None,
        "huntGroups": [],
        "callCenters": [],
        "pickUpGroup": None,
    }

    try:
        user = api.reports.get_user_report(user_id)
    except Exception:
        return f"User {user_id} not found."

    USER_DATA["firstName"] = user["firstName"]
    USER_DATA["lastName"] = user["lastName"]
    USER_DATA["extension"] = user["extension"]
    USER_DATA["phoneNumber"] = user["phoneNumber"]
    USER_DATA["services"] = user["userServices"]
    USER_DATA["featurePacks"] = user["servicePacks"]
    USER_DATA["aliases"] = user["aliases"]

    pick_up_group = api.call_pickup.get_call_pickup_group_user(
        service_provider_id, group_id, user_id
    )
    try:
        USER_DATA["pickUpGroup"] = pick_up_group[0]["name"]
    except IndexError:
        USER_DATA["pickUpGroup"] = None

    hunt_groups = api.hunt_groups.get_group_hunt_group_user(
        service_provider_id, group_id, user_id
    )
    for hg in tqdm(hunt_groups, desc="Fetching Hunt Groups"):
        USER_DATA["huntGroups"].append(hg["serviceUserId"])

    # if the user does not have a license for CC this call errors
    try:
        call_centers = api.call_centers.get_user_call_center(user_id)
        for cc in tqdm(call_centers["callCenters"], desc="Fetching Call Centers"):
            USER_DATA["callCenters"].append(cc["serviceUserId"])
    except Exception:
        USER_DATA["callCenters"] = None

    return USER_DATA
