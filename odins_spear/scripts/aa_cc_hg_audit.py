import json
from tqdm import tqdm

def remove_excess_details(aa_cc_hg: dict):
        del aa_cc_hg["name"]
        del aa_cc_hg["phoneNumber"]
        del aa_cc_hg["extension"]
        del aa_cc_hg["department"]
        del aa_cc_hg["isActive"]
        
        if aa_cc_hg["typeTag"] == "AA":
            del aa_cc_hg["video"]
        elif aa_cc_hg["typeTag"] == "CC":
            del aa_cc_hg["video"]
            del aa_cc_hg["policy"]
        elif aa_cc_hg["typeTag"] == "HG":
            del aa_cc_hg["serviceProviderId"]
            del aa_cc_hg["groupId"]
            del aa_cc_hg["policy"]
        
def main(api, service_provider_id: str, group_id: str):
    """
    This script returns the services assigned to Auto Attendants, 
    Call Centres, and Hunt Groups. Only services are applied to these 
    entities and there are scenarios one would need to focus services 
    assigned to these entities.
    

    :param service_provider_id: Service Provider ID or Enterprise ID containing the Group ID.
    :param group_id: Group ID to generate the report for.

    :return JSON: A JSON formatted report of service packs assigned to AA, CC, and HG. 
    """  

    print("aa_cc_hg_audit start.")
    return_data = {
        "autoAttendants": [],
        "callCenters": [],
        "huntGroups": []
    }
    auto_attendants = api.get.auto_attendants(service_provider_id, group_id)
    call_centers = api.get.group_call_centers(service_provider_id, group_id)
    hunt_groups = api.get.group_hunt_groups(service_provider_id, group_id)
    
    for aa in tqdm(auto_attendants, desc="Analysing Auto Attendants"):
        aa["typeTag"] = "AA"
        remove_excess_details(aa)

    for cc in tqdm(call_centers, desc="Analysing Call Centers"):
        cc["typeTag"] = "CC"
        remove_excess_details(cc)
        
    for hg in tqdm(hunt_groups, desc="Analysing Hunt Groups"):
        hg["typeTag"] = "HG"
        remove_excess_details(hg)
        
    aa_cc_hgs = auto_attendants + call_centers + hunt_groups
    
    for aa_cc_hg in tqdm(aa_cc_hgs, desc="Fetching User Services"):
        response = api.get.user_services_assigned(aa_cc_hg["serviceUserId"])
        aa_cc_hg["services"] = response["userServices"]
        
        if aa_cc_hg["typeTag"] == "AA":
            del aa_cc_hg["typeTag"]
            return_data["autoAttendants"].append(aa_cc_hg)
        elif aa_cc_hg["typeTag"] == "CC":
            del aa_cc_hg["typeTag"]
            return_data["callCenters"].append(aa_cc_hg)
        elif aa_cc_hg["typeTag"] == "HG":
            del aa_cc_hg["typeTag"]
            return_data["huntGroups"].append(aa_cc_hg)
        
    return return_data
        
    