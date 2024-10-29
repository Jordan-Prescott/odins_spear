import json
from tqdm import tqdm

def main(api, service_provider_id, group_id):
    """
        A stripped down version of group audit focussing only on the service packs assigned within
        the group. This only shows the service packs assigned and total count of unlike group audit 
        which details the users this is assigned to.

        :param service_provider_id (str): Service Provider ID or Enterprise ID containing the Group ID.
        :param group_id (str): Group ID to generate the report for.

        :return str: A JSON formatted report of service packs assigned in the group.
    """    
    
    service_report = api.get.group_services(group_id, service_provider_id)

    assigned_service_pack_services = []

    for sps in tqdm(service_report["servicePackServices"], desc="Analysing Service Packs..."):
            if sps["usage"] > 0:
                del sps["authorized"]
                del sps["assigned"]
                del sps["limited"]
                del sps["allowed"]
                del sps["serviceName"]
                del sps["quantity"]
                del sps["alias"]

                assigned_service_pack_services.append(sps)
                
    return {"servicePackServices": assigned_service_pack_services}
