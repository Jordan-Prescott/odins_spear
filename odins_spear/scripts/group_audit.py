import odins_spear.logger as logger
import json
from tqdm import tqdm


def main(api, service_provider_id: str, group_id: str):
    """ Audits a group for chargeable services this will return all feature packs 
    assigned and count for all broadwork entities such as users, call centers, hunt groups etc.
    Additionaly this will return all DID/DDI's and their active status.

    :param service_provider_id: Service provider or Enterprise ID that contains group being audited.
    :param group_id: Group that is to be audited.

    :return r:
    """

    RETRY_QUEUE = []
    MAX_RETRIES = 2

    # all Services
    service_report = api.get.group_services(group_id, service_provider_id)

    assigned_user_services = []
    assigned_group_services = []
    assigned_service_pack_services = []

    for us in tqdm(service_report["userServices"], desc="Analysing User Services..."):
        if us["usage"] > 0:
            del us["authorized"]
            del us["assigned"]
            del us["limited"]
            del us["quantity"]
            del us["licensed"]
            del us["allowed"]
            del us["userAssignable"]
            del us["groupServiceAssignable"]
            del us["tags"]
            del us["alias"]

            users = api.get.group_services_assigned(
                group_id, service_provider_id, us["serviceName"], "serviceName")
            userIDs = [u["userId"] for u in users["users"]]
            us["users"] = userIDs

            assigned_user_services.append(us)

    for gs in tqdm(service_report["groupServices"], desc="Analysing Group Services..."):
        if gs["usage"] > 0:
            del gs["authorized"]
            del gs["assigned"]
            del gs["limited"]
            del gs["quantity"]
            del gs["licensed"]
            del gs["allowed"]
            del gs["instanceCount"]
            del gs["alias"]
            assigned_group_services.append(gs)

    for sps in tqdm(service_report["servicePackServices"], desc="Analysing Service Packs..."):
        if sps["usage"] > 0:
            del sps["authorized"]
            del sps["assigned"]
            del sps["limited"]
            del sps["allowed"]
            del sps["serviceName"]
            del sps["quantity"]
            del sps["alias"]

            users = api.get.group_services_assigned(
                group_id, service_provider_id, sps["servicePackName"], "servicePackName")
            userIDs = [u["userId"] for u in users["users"]]
            sps["users"] = userIDs

            assigned_service_pack_services.append(sps)

    return json.dumps({
        "user_services": assigned_user_services,
        "group_services": assigned_group_services,
        "service_pack_services": assigned_service_pack_services
    })
