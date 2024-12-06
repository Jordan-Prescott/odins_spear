from tqdm import tqdm

from .report_utils.graphviz_module import GraphvizModule
from .report_utils.helpers import find_entity_with_number_type
from .report_utils.parsing import call_flow_module


from ..store import DataStore
from ..store import broadwork_entities as bre

def main(api, service_provider_id: str, group_id: str, number: str, number_type: str,
         broadworks_entity_type: str):
    
    # Creates data store for use later
    data_store = DataStore()
    
    print("Start.\n")
    print("Fetching Service Provider & Group details.")
    # Gather entities 
    service_provider = bre.ServiceProvider.from_dict(data=api.get.service_provider(service_provider_id))
    group = bre.Group.from_dict(service_provider=service_provider, data=api.get.group(service_provider_id, group_id))
    
    data_store.store_objects(service_provider, group)
    
    auto_attendants = api.get.auto_attendants(service_provider_id, group_id)
    for aa in tqdm(auto_attendants, desc="Fetching all Auto Attendants."):
        auto_attendant = bre.AutoAttendant.from_dict(group=group, data=api.get.auto_attendant(aa['serviceUserId']))
        data_store.auto_attendants.append(auto_attendant)
    
    print("Fetching all users this may take a couple of minutes, please wait.")
    users = api.get.users(service_provider_id, group_id, extended=True)
    
    # Captures users with the forward fucntionality
    call_forward_always_users = [
    item["user"]["userId"] for item in api.get.bulk_call_forwarding_always(service_provider_id, group_id) if item["service"]["assigned"] \
        and item["data"]["isActive"]
    ]

    call_forward_busy_users = [
    item["user"]["userId"] for item in api.get.bulk_call_forwarding_busy(service_provider_id, group_id) if item["service"]["assigned"] \
        and item["data"]["isActive"]
    ]
    
    call_forward_no_answer_users = [
    item["user"]["userId"] for item in api.get.bulk_call_forwarding_no_answer(service_provider_id, group_id) if item["service"]["assigned"] \
        and item["data"]["isActive"]
    ]
    
    call_forward_not_reachable = [
    item["user"]["userId"] for item in api.get.bulk_call_forwarding_not_reachable(service_provider_id, group_id) if item["service"]["assigned"] \
        and item["data"]["isActive"]
    ]

    for u in tqdm(users, desc="Parsing all Users."):
        user = bre.User.from_dict(group=group, data=u)
        
        if user.id in call_forward_always_users:
            user.call_forwarding_always = str(api.get.user_call_forwarding_always(user.id)["forwardToPhoneNumber"])
        if user.id in call_forward_busy_users:
            user.call_forwarding_busy = str(api.get.user_call_forwarding_busy(user.id)["forwardToPhoneNumber"])
        if user.id in call_forward_no_answer_users:
            user.call_forwarding_no_answer = str(api.get.user_call_forwarding_no_answer(user.id)["forwardToPhoneNumber"])
        if user.id in call_forward_not_reachable:
            user.call_forwarding_not_reachable = str(api.get.user_call_forwarding_not_reachable(user.id)["forwardToPhoneNumber"])
        
        data_store.users.append(user)


    call_centers = api.get.group_call_centers(service_provider_id, group_id)    
    for cc in tqdm(call_centers, desc="Fetching all Call Centers."):
        
        call_center = api.get.group_call_center(cc['serviceUserId'])
        call_center['agents'] = api.get.group_call_center_agents(cc['serviceUserId'])['agents']
        
        call_center = bre.CallCenter.from_dict(group= group, data= call_center)
        
        try:
            overflow_settings = api.get.group_call_center_overflow(call_center.service_user_id)
            call_center.overflow_calls_action = overflow_settings["action"]
            call_center.overflow_calls_transfer_to_phone_number = overflow_settings["transferPhoneNumber"] \
                if call_center.overflow_calls_action == "Transfer" else None
        except Exception:
            call_center.overflow_calls_action = None
            call_center.overflow_calls_transfer_to_phone_number = None
        
        try:
            stranded_calls_settings = api.get.group_call_center_stranded_calls(call_center.service_user_id)
            call_center.stranded_calls_action = stranded_calls_settings["action"]
            call_center.stranded_calls_transfer_to_phone_number = stranded_calls_settings["transferPhoneNumber"] \
                if call_center.stranded_calls_action == "Transfer" else None
        except Exception:
            call_center.stranded_calls_action = None
            call_center.stranded_calls_transfer_to_phone_number = None
            
        try:
            stranded_calls_unavailable_settings = api.get.group_call_center_stranded_calls_unavailable(call_center.service_user_id)
            action_value = stranded_calls_unavailable_settings["action"]
            call_center.stranded_call_unavailable_action = None if action_value == 'None' else action_value
            call_center.stranded_call_unavailable_transfer_to_phone_number = stranded_calls_unavailable_settings["transferPhoneNumber"] \
                if call_center.stranded_call_unavailable_action == "Transfer" else None
        except Exception:
            call_center.stranded_call_unavailable_action = None
            call_center.stranded_call_unavailable_transfer_to_phone_number = None
        
        try: 
            forced_forwarding_settings = api.get.group_call_center_forced_forwarding(call_center.service_user_id)
            call_center.forced_forwarding_enabled = forced_forwarding_settings["enabled"]
            call_center.forced_forwarding_forward_to_phone_number = forced_forwarding_settings["forwardToPhoneNumber"] \
                if call_center.forced_forwarding_enabled else None
        except Exception:
            call_center.forced_forwarding_enabled = False
            call_center.forced_forwarding_forward_to_phone_number = None
        
        data_store.call_centers.append(call_center)
    
    hunt_groups = api.get.group_hunt_groups(service_provider_id, group_id)
    for hg in tqdm(hunt_groups, desc="Fetching all Hunt Groups."):
        hunt_group = bre.HuntGroup.from_dict(group=group, data= api.get.group_hunt_group(hg['serviceUserId']))
        data_store.hunt_groups.append(hunt_group)
      
    # locate number using broadworks_entity_type to zone in on correct location
    call_flow_start_node = find_entity_with_number_type(
			number,
			number_type.lower(),
			getattr(data_store, broadworks_entity_type + "s")
		)
    call_flow_start_node._start_node = True
    
    # Nodes used in the graph
    print("Gathering nodes in flow.")
    bre_nodes = call_flow_module(call_flow_start_node, data_store)
    
    print("Generating report.")
    # build, generate, save graph
    graph = GraphvizModule(
        "./os_reports/"
    )
    graph.generate_call_flow_graph(
        bre_nodes,
        number
    )
    print("Saving report.")
    graph._save_graph(f"Calls To {number}")
    print("\nEnd.")