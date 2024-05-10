import json

from .report_utils.graphviz_module import GraphvizModule
from .report_utils.helpers import find_number

from odins_spear.store import DataStore
from odins_spear.store import broadwork_entities as bre

def main(api, service_provider_id: str, group_id: str, number: str, number_type: str,
         broadworks_entity_type: str):
    
    """ 
    methods needed:
    - get.auto_attendants - X
    - get.auto_attendant - X
    
    - get.group_call_centers - X
    - get.group_call_center - X 
    - get.group_call_center_bounced_calls - 
    - get.group_call_center_forced_forwarding - 
    - get.group_call_center_overflow - 
    - get.group_call_center_stranded_calls - 
    - get.group_call_center_stranded_unavailable - 
    
    - get.group_hunt_groups - X
    - get.group_hunt_group - X
    
    - get.users - X
    - get.user_by_id - X
    
    - get.user_call_forwarding_always - 
    - get.user_call_forwarding_busy - 
    - get.user_call_forwarding_no_answer - 
    - get.user_call_forwarding_not_reachable - 
    
    - get.group_schedules - X
    - get.group_events  - X
    - get.user_alternate_numbers  - X
    """
    
    data_store = DataStore()
    
    # Gather entities 
    service_provider = bre.ServiceProvider.from_dict(data=api.get.service_provider(service_provider_id))
    group = bre.Group.from_dict(service_provider=service_provider, data=api.get.group(service_provider_id, group_id))
    
    data_store.store_objects(service_provider, group)
    
    # auto_attendants = api.get.auto_attendants(service_provider_id, group_id)
    # for aa in auto_attendants:
    #     auto_attendant = bre.AutoAttendant.from_dict(group=group, data=api.get.auto_attendant(aa['serviceUserId']))
    #     data_store.auto_attendants.append(auto_attendant)
    
    users = api.get.users(service_provider_id, group_id, extended=True)
    for u in users:
        user = bre.User.from_dict(group=group, data=u)
        data_store.users.append(user)
    
    # call_centers = api.get.group_call_centers(service_provider_id, group_id)
    # for cc in call_centers:
    #     call_center = bre.CallCenter.from_dict(group=group, data= api.get.group_call_center(cc['serviceUserId']))
    #     data_store.call_centers.append(call_center)
    
    # hunt_groups = api.get.group_hunt_groups(service_provider_id, group_id)
    # for hg in hunt_groups:
    #     hunt_group = bre.HuntGroup.from_dict(group=group, data= api.get.group_hunt_group(hg['serviceUserId']))
    #     data_store.hunt_groups.append(hunt_group)
      
    
    
    # locate number using broadworks_entity_type to zone in on correct location
    call_flow_start = find_number(
			number,
			number_type,
			getattr(data_store, broadworks_entity_type + "s")
		)
    if broadworks_entity_type == "auto attendant":
        call_flow_start = find_number(
			number,
			number_type,
			data_store.auto_attendants
		)
    if broadworks_entity_type == "hunt group":
        call_flow_start = find_number(
			number,
			number_type,
			data_store.hunt_groups
		)
    if broadworks_entity_type == "call center":
        call_flow_start = find_number(
			number,
			number_type,
			data_store.call_centers
		)
  
    
    # follow and map how the routing options. each routing instance will need to be followed.
    
    # create a graphviz chart  
    
    # save the chart to local machine as svg. 
    
    
    graph = GraphvizModule(
         "./os_reports/"
    )
    graph.generate_call_flow_graph(
         "flow",
         "0"
    )
    pass