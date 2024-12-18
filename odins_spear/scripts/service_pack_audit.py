from tqdm import tqdm


def main(api, service_provider_id: str, group_id: str) -> dict:
    """
    A stripped down version of group audit focussing only on the service packs assigned within
    the group. This only shows the service packs assigned and total count of unlike group audit
    which details the users this is assigned to.
    """

    service_report = api.services.get_group_services(group_id, service_provider_id)

    assigned_service_pack_services = []

    for sps in tqdm(
        service_report["servicePackServices"], desc="Analysing Service Packs..."
    ):
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
