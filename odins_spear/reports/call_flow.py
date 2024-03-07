import graphviz

import odins_spear.logger as logger

from .report_utils.graphviz_formatting import GraphvizFormatter

def main(api, service_provider_id: str, group_id: str, number: int, number_type: str,
         broadworks_entity_type: str):
    
    """ 
    methods needed:
    - get.auto_attendants
    - get.auto_attendant
    
    - get.group_call_centers
    - get.group_call_center
    - get.group_call_center_bounced_calls
    - get.group_call_center_forced_forwarding
    - get.group_call_center_overflow
    - get.group_call_center_stranded_calls
    - get.group_call_center_stranded_unavailable
    
    - get.group_hunt_groups
    - get.group_hunt_group
    
    - get.users
    - get.user_by_id
    
    - get.user_call_forwarding_always
    - get.user_call_forwarding_busy
    - get.user_call_forwarding_no_answer
    - get.user_call_forwarding_not_reachable
    """
    
    # locate number using broadworks_entity_type to zone in on correct location
    
    # follow and map how the routing options. each routing instance will need to be followed.
    
    # create a graphviz chart  
    
    # save the chart to local machine as svg. 
    
    pass