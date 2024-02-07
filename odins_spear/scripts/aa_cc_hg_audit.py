import json
from tqdm import tqdm

def remove_excess_details(aa_cc_hg: dict):
        del aa_cc_hg["name"]
        del aa_cc_hg["phoneNumber"]
        del aa_cc_hg["extension"]
        del aa_cc_hg["department"]
        del aa_cc_hg["isActive"]
        
        if aa_cc_hg["type_tag"] == "AA":
            del aa_cc_hg["type"]
            del aa_cc_hg["video"]
        elif aa_cc_hg["type_tag"] == "CC":
            del aa_cc_hg["video"]
            del aa_cc_hg["policy"]
        elif aa_cc_hg["type_tag"] == "HG":
            del aa_cc_hg["serviceProviderId"]
            del aa_cc_hg["groupId"]
            del aa_cc_hg["policy"]
        
def main(api, service_provider_id: str, group_id: str):

    print("aa_cc_hg_audit start.")
    return_data = {
        "Auto Attendants": [],
        "Call Centres": [],
        "Hunt Groups": []
    }
    auto_attendants = api.get.auto_attendants(service_provider_id, group_id)
    call_centers = api.get.group_call_centers(service_provider_id, group_id)
    hunt_groups = api.get.group_hunt_groups(service_provider_id, group_id)
    
    for aa in tqdm(auto_attendants, desc="Analysing Auto Attendants"):
        aa["type_tag"] = "AA"
        remove_excess_details(aa)

    for cc in tqdm(call_centers, desc="Analysing Call Centers"):
        cc["type_tag"] = "CC"
        remove_excess_details(cc)
        
    for hg in tqdm(hunt_groups, desc="Analysing Hunt Groups"):
        hg["type_tag"] = "HG"
        remove_excess_details(hg)
        
    aa_cc_hgs = auto_attendants + call_centers + hunt_groups
    
    for aa_cc_hg in tqdm(aa_cc_hgs, desc="Fetching User Services"):
        response = api.get.user_services_assigned(aa_cc_hg["serviceUserId"])
        aa_cc_hg["services"] = response["userServices"]
        
        if aa_cc_hg["type_tag"] == "AA":
            del aa_cc_hg["type_tag"]
            return_data["Auto Attendants"].append(aa_cc_hg)
        elif aa_cc_hg["type_tag"] == "CC":
            del aa_cc_hg["type_tag"]
            return_data["Call Centres"].append(aa_cc_hg)
        elif aa_cc_hg["type_tag"] == "HG":
            del aa_cc_hg["type_tag"]
            return_data["Hunt Groups"].append(aa_cc_hg)
        
    return json.dumps(return_data)
        
    