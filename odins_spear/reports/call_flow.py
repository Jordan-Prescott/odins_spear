import json

import odins_spear.logger as logger

from .report_utils.graphviz_module import GraphvizModule

def main(api, service_provider_id: str, group_id: str, number: str, number_type: str,
         broadworks_entity_type: str):
    
    """ 
    methods needed:
    - get.auto_attendants - X
    - get.auto_attendant - X
    
    - get.group_call_centers - X
    - get.group_call_center - X 
    - get.group_call_center_bounced_calls - X
    - get.group_call_center_forced_forwarding - X
    - get.group_call_center_overflow - X
    - get.group_call_center_stranded_calls - X
    - get.group_call_center_stranded_unavailable - X
    
    - get.group_hunt_groups - X
    - get.group_hunt_group - X
    
    - get.users - X
    - get.user_by_id - X
    
    - get.user_call_forwarding_always - X
    - get.user_call_forwarding_busy - X
    - get.user_call_forwarding_no_answer - X
    - get.user_call_forwarding_not_reachable - X
    
    - get.group_schedules - X
    - get.group_events  - X
    - get.user_alternate_numbers  - X
    """
    
    # Gather entities 
    
    # locate number using broadworks_entity_type to zone in on correct location
    
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