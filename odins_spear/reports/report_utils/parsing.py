from odins_spear.store import broadwork_entities as bre

# nodes needed for graph generation
NODES = [] 
MAX_LEVEL = 30

def call_flow_module(node: object, data_store: object):
    
    # create mapping for easier searchability when gathering nodes
    data_store.build_number_mapping()
    
    _traverse_connecting_entities(node, data_store)
    
    return NODES
    

#TODO: run over the entities and depening on what it is use the call forwards to pull the other entities
def _traverse_connecting_entities(entity: object, data_store: object):
    try:
        if isinstance(entity, bre.User):
            entity.call_forwarding_always = data_store.number_mapping.get(entity.call_forwarding_always)
            if entity.call_forwarding_always: 
                _traverse_connecting_entities(entity.call_forwarding_always, data_store)
            
            entity.call_forwarding_busy = data_store.number_mapping.get(entity.call_forwarding_busy)
            if entity.call_forwarding_busy:
                _traverse_connecting_entities(entity.call_forwarding_busy, data_store)
            
            entity.call_forwarding_no_answer = data_store.number_mapping.get(entity.call_forwarding_no_answer)
            if entity.call_forwarding_no_answer:
                _traverse_connecting_entities(entity.call_forwarding_no_answer, data_store)
            
            entity.call_forwarding_not_reachable = data_store.number_mapping.get(entity.call_forwarding_not_reachable)
            if entity.call_forwarding_not_reachable:
                _traverse_connecting_entities(entity.call_forwarding_not_reachable, data_store)
        
        if isinstance(entity, bre.CallCenter):
            if entity.bounced_calls_enabled:
                entity.bounced_calls_transfer_to_phone_number = data_store.number_mapping.get(entity.bounced_calls_transfer_to_phone_number)
                if entity.bounced_calls_transfer_to_phone_number:
                    _traverse_connecting_entities(entity.bounced_calls_transfer_to_phone_number, data_store)
            
            if entity.overflow_calls_action:
                entity.overflow_calls_transfer_to_phone_number = data_store.number_mapping.get(entity.overflow_calls_transfer_to_phone_number)
                if entity.overflow_calls_transfer_to_phone_number:
                    _traverse_connecting_entities(entity.overflow_calls_transfer_to_phone_number, data_store)

            if entity.stranded_calls_action:
                entity.stranded_calls_transfer_to_phone_number = data_store.number_mapping.get(entity.stranded_calls_transfer_to_phone_number)
                if entity.stranded_calls_transfer_to_phone_number:
                    _traverse_connecting_entities(entity.stranded_calls_transfer_to_phone_number, data_store)
        
            if entity.stranded_call_unavailable_action:
                entity.stranded_call_unavailable_transfer_to_phone_number = data_store.number_mapping.get(entity.stranded_call_unavailable_transfer_to_phone_number)
                if entity.stranded_call_unavailable_transfer_to_phone_number:
                    _traverse_connecting_entities(entity.stranded_call_unavailable_transfer_to_phone_number, data_store)
    except TypeError:
        pass                           
    NODES.append(entity)  # Append outside of the if condition
