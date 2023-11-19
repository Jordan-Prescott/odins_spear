from typing import List

from odin_api.utils import generator as gen

class ServiceProvider:
    """_summary_
    """
    
    def __init__():
        pass
    
    def __init__(self, 
                 id, 
                 name, 
                 default_domain=None, 
                 support_email=None, 
                 contact_name=None, 
                 contact_number=None, 
                 contact_email=None,
                 address_line_1=None, 
                 city=None, 
                 state_or_province=None, 
                 zip_or_postcode=None, 
                 country=None, 
                 use_service_provider_language=False
                 ):
        
        self.id = id
        self.name = name
        self.groups: List[Group] = []

        self.is_enterprise = False
        self.default_domain = default_domain

        self.support_email = support_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_email = contact_email

        self.address_line_1 = address_line_1
        self.city = city
        self.state_or_province = state_or_province
        self.zip_or_postcode = zip_or_postcode
        self.country = country

        self.use_service_provider_language = use_service_provider_language


class Enteprise(ServiceProvider):
    """_summary_

    Args:
        ServiceProvider (_type_): _description_
    """
    def __init__(self, 
                 id, 
                 name, 
                 default_domain=None, 
                 support_email=None, 
                 contact_name=None, 
                 contact_number=None, 
                 contact_email=None,
                 address_line_1=None, 
                 city=None, 
                 state_or_province=None, 
                 zip_or_postcode=None, 
                 country=None, 
                 use_service_provider_language=False
                 ):
        
        super().__init__(default_domain, support_email, contact_name, contact_number, 
                         contact_email, address_line_1, city, state_or_province, 
                         zip_or_postcode, country, use_service_provider_language)

        self.id = id 
        self.name = name

        self.is_enterprise = True


class Group:
    """_summary_
    """
    
    def __init__(self, 
                 sp_or_ent, 
                 id, 
                 name, 
                 default_domain=None, 
                 user_limit=None, 
                 user_count=None, 
                 calling_line_id_name=None, 
                 calling_line_id_phone_number=None, 
                 calling_line_id_display_phone_number=None, 
                 time_zone=None, 
                 time_zone_display_name=None, 
                 location_dialing_code=None, 
                 contact_name=None, 
                 contact_number=None, 
                 contact_email=None, 
                 address_line_1=None, 
                 address_line_2=None, 
                 city=None, 
                 state_or_province=None, 
                 country=None,
                 ):
        
        self.sp_or_ent = sp_or_ent.groups.append(self) #TODO: This may fail
        self.id = id
        self.default_domain = default_domain
        self.name = name
        self.users: List[User] = []
        self.hunt_groups: List[HuntGroup] = []
        self.trunk_groups: List[TrunkGroup] = []

        self.calling_line_id_name = calling_line_id_name
        self.calling_line_id_phone_number = calling_line_id_phone_number
        self.calling_line_id_display_phone_number = calling_line_id_display_phone_number
        self.location_dialing_code = location_dialing_code
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.time_zone = time_zone
        self.time_zone_display_name = time_zone_display_name

        self.user_limit = user_limit
        self.user_count = user_count
        
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state_or_province = state_or_province
        self.country = country


class TrunkGroup:
    """_summary_
    """
    
    def __init__(self,
                 name,
                 group,
                 access_device,
                 users: list[object],
                 allow_termination_to_dtg_identity: bool=False,
                 allow_termination_to_trunk_group_identity: bool=False,
                 allow_unscreened_calls: bool=False,
                 allow_unscreened_emergency_calls: bool=False,
                 capacity_exceeded_trap_initial_calls=None,
                 capacity_exceeded_trap_offset_calls=None,
                 clid_source_for_screened_calls_policy=None,
                 continuous_options_sending_interval_seconds=None,
                 enable_bursting: bool=False,
                 enable_network_address_identity: bool=False,
                 failure_options_sending_interval_seconds=None,
                 failure_threshold_counter=None,
                 include_dtg_identity: bool=False,
                 include_otg_identity_for_network_calls: bool=False,
                 include_trunk_group_identity: bool=False,
                 include_trunk_group_identity_for_network_calls: bool=False,
                 invitation_timeout=None,
                 invite_failure_threshold_counter=None,
                 invite_failure_threshold_window_seconds=None,
                 pilot_user_call_optimization_policy=None,
                 pilot_user_calling_line_asserted_identity_policy=None,
                 pilot_user_calling_line_identity_for_emergency_calls_policy=None,
                 pilot_user_calling_line_identity_for_external_calls_policy=None,
                 pilot_user_charge_number_policy=None,
                 prefix_enabled: bool=False,
                 require_authentication: bool=False,
                 route_to_peering_domain: bool=False,
                 send_continuous_options_message: bool=False,
                 stateful_rerouting_enabled: bool=False,
                 success_threshold_counter=None,
                 use_system_clid_source_for_screened_calls_policy: bool=False,
                 use_system_calling_line_asserted_identity_policy: bool=False,
                 use_system_user_lookup_policy: bool=False,
                 user_lookup_policy=None,
                 max_active_calls=None,
                 max_incoming_calls=None,
                 max_outgoing_calls=None,
                 ):
         
        self.name = name
        self.group = group
        self.access_device = access_device
        self.users: List[User] = users if users else []

        self.allow_termination_to_dtg_identity = allow_termination_to_dtg_identity
        self.allow_termination_to_trunk_group_identity = allow_termination_to_trunk_group_identity
        self.allow_unscreened_calls = allow_unscreened_calls
        self.allow_unscreened_emergency_calls = allow_unscreened_emergency_calls
        self.capacity_exceeded_trap_initial_calls = capacity_exceeded_trap_initial_calls
        self.capacity_exceeded_trap_offset_calls = capacity_exceeded_trap_offset_calls
        self.clid_source_for_screened_calls_policy = clid_source_for_screened_calls_policy
        self.continuous_options_sending_interval_seconds = continuous_options_sending_interval_seconds
        self.enable_bursting = enable_bursting
        self.enable_network_address_identity = enable_network_address_identity
        self.failure_options_sending_interval_seconds = failure_options_sending_interval_seconds
        self.failure_threshold_counter = failure_threshold_counter
        self.include_dtg_identity = include_dtg_identity
        self.include_otg_identity_for_network_calls = include_otg_identity_for_network_calls
        self.include_trunk_group_identity = include_trunk_group_identity
        self.include_trunk_group_identity_for_network_calls = include_trunk_group_identity_for_network_calls
        self.invitation_timeout = invitation_timeout
        self.invite_failure_threshold_counter = invite_failure_threshold_counter
        self.invite_failure_threshold_window_seconds = invite_failure_threshold_window_seconds
        self.pilot_user_call_optimization_policy = pilot_user_call_optimization_policy
        self.pilot_user_calling_line_asserted_identity_policy = pilot_user_calling_line_asserted_identity_policy
        self.pilot_user_calling_line_identity_for_emergency_calls_policy = pilot_user_calling_line_identity_for_emergency_calls_policy 
        self.pilot_user_calling_line_identity_for_external_calls_policy = pilot_user_calling_line_identity_for_external_calls_policy
        self.pilot_user_charge_number_policy = pilot_user_charge_number_policy
        self.prefix_enabled = prefix_enabled
        self.require_authentication = require_authentication
        self.route_to_peering_domain = route_to_peering_domain
        self.send_continuous_options_message = send_continuous_options_message
        self.stateful_rerouting_enabled = stateful_rerouting_enabled
        self.success_threshold_counter = success_threshold_counter
        self.use_system_clid_source_for_screened_calls_policy = use_system_clid_source_for_screened_calls_policy
        self.use_system_calling_line_asserted_identity_policy = use_system_calling_line_asserted_identity_policy
        self.use_system_user_lookup_policy = use_system_user_lookup_policy
        self.user_lookup_policy = user_lookup_policy
        self.max_active_calls = max_active_calls
        self.max_incoming_calls = max_incoming_calls
        self.max_outgoing_calls = max_outgoing_calls

        self.service_provider_id = group.sp_or_ent


class AAKey():
    """_summary_
    """
    
    def __init__(self,
                 key_number=None, 
                 action=None, 
                 description=None, 
                 phone_number=None, 
                 submenu_id=None
                 ) -> None:
        
        self.key = key_number
        self.action = action
        self.description = description
        self.phone_number = phone_number
        self.submenu_id = submenu_id

class AAMenu():
    """_summary_
    """
    
    def __init__(self, 
                 announcement_selection=None, 
                 enable_first_menu_level_extension_dialing: bool=False,
                 keys: List[AAKey]=None
                 ) -> None:
        
        self.announcement_selection = announcement_selection
        self.enable_first_menu_level_extension_dialing = enable_first_menu_level_extension_dialing
        self.keys = keys
        

class AutoAttendant:
    """_summary_
    """
    
    def __int__(self, 
                name=None, 
                calling_line_id_last_name=None, 
                calling_line_id_first_name=None, 
                hiragana_last_name=None, 
                hiragana_first_name=None, 
                language=None, 
                time_zone=None, 
                time_zone_display_name=None, 
                aliases: List[object]=None,
                type=None, 
                enable_video: bool=False, 
                extension_dialing_scope=None, 
                name_dialing_scope=None, 
                name_dialing_entries=None,
                business_hours_menu: AAMenu=None,
                after_hours_menu: AAMenu=None,
                service_user_id=None, 
                group=None, 
                ):
        
        self.name = name
        self.group = group

        self.calling_line_id_last_name = calling_line_id_last_name
        self.calling_line_id_first_name = calling_line_id_first_name
        self.hiragana_last_name = hiragana_last_name
        self.hiragana_first_name = hiragana_first_name
        self.language = language
        self.time_zone = time_zone
        self.time_zone_display_name = time_zone_display_name
        self.aliases = aliases
        self.type = type
        self.enable_video = enable_video
        self.extension_dialing_scope = extension_dialing_scope
        self.name_dialing_scope = name_dialing_scope
        self.name_dialing_entries = name_dialing_entries
        self.business_hours_menu = business_hours_menu
        self.after_hours_menu = after_hours_menu
        self.service_user_id = service_user_id

        self.service_provider_id = group.sp_or_ent.id
        self.is_enterprise = group.sp_or_ent.is_enterprise
        

class CallCenter:
    """_summary_
    """
    
    def __init__(self,
                name,         
                group,
                agents: List[object]=None,
                        
                enable_video=False, 
                allow_caller_to_dial_escape_digit=False, 
                reset_call_statistics_upon_entry_in_queue=True, 
                allow_agent_logoff=True, 
                allow_call_waiting_for_agents=True, 
                play_ringing_when_offering_call=True, 
                external_preferred_audio_codec=None, 
                internal_preferred_audio_codec=None,
                enable_reporting=False, 
                allow_calls_to_agents_in_wrap_up=True,
                override_agent_wrap_up_time=False, 
                enable_automatic_state_change_for_agents=False,
                force_delivery_of_calls=False, 
                type=None,
                service_user_id_prefix=None, 
                calling_line_id_last_name=None, 
                calling_line_id_first_name=None, 
                password=None, 
                policy=None, 
                routing_type=None,
                queue_length=None, 
                escape_digit=None, 
                service_user_id=None
                ):
        
        self.name = name
        self.group = group
        self.agents: List[User] = []
        
        self.enable_video = enable_video
        self.allow_caller_to_dial_escape_digit = allow_caller_to_dial_escape_digit
        self.reset_call_statistics_upon_entry_in_queue = reset_call_statistics_upon_entry_in_queue
        self.allow_agent_logoff = allow_agent_logoff
        self.allow_call_waiting_for_agents = allow_call_waiting_for_agents
        self.play_ringing_when_offering_call = play_ringing_when_offering_call
        self.external_preferred_audio_codec = external_preferred_audio_codec
        self.internal_preferred_audio_codec = internal_preferred_audio_codec
        self.enable_reporting = enable_reporting
        self.allow_calls_to_agents_in_wrap_up = allow_calls_to_agents_in_wrap_up
        self.override_agent_wrap_up_time = override_agent_wrap_up_time
        self.enable_automatic_state_change_for_agents = enable_automatic_state_change_for_agents
        self.force_delivery_of_calls = force_delivery_of_calls
        self.type = type
        self.service_user_id_prefix = service_user_id_prefix
        self.calling_line_id_last_name = calling_line_id_last_name
        self.calling_line_id_first_name = calling_line_id_first_name
        self.password = password if password is not None else gen.generate_password() 
        self.policy = policy
        self.routing_type = routing_type
        self.queue_length = queue_length
        self.escape_digit = escape_digit
        self.service_user_id = service_user_id
        
        self.service_provider_id = group.sp_or_ent.id 
        
        
class HuntGroup:
    """_summary_
    """
    
    def __init__(self,
                name,
                group,
                agents: List[object]=None,
                calling_line_id_last_name=None,
                calling_line_id_first_name=None,
                hiragana_last_name=None,
                hiragana_first_name=None,
                language=None,
                time_zone=None,
                aliases=None,
                policy=None,
                hunt_after_no_answer=None,
                no_answer_number_of_rings=None,
                forward_after_timeout=None,
                forward_timeout_seconds=None,
                allow_call_waiting_for_agents=None,
                use_system_hunt_group_clid_setting=None,
                include_hunt_group_name_in_clid=None,
                enable_not_reachable_forwarding=None,
                make_busy_when_not_reachable=None,
                service_user_id=None,
                ):
        
        self.name = name
        self.group = group.hunt_groups.append(self) #this may fail
        self.agents: List[User] = []
        
        self.service_provider_id = group.so_or_ent.id
        
        self.calling_line_id_last_name = calling_line_id_last_name
        self.calling_line_id_first_name = calling_line_id_first_name
        self.hiragana_last_name = hiragana_last_name
        self.hiragana_first_name = hiragana_first_name
        self.language = language
        self.time_zone = time_zone
        self.aliases = aliases
        self.policy = policy
        self.hunt_after_no_answer = hunt_after_no_answer
        self.no_answer_number_of_rings = no_answer_number_of_rings
        self.forward_after_timeout = forward_after_timeout
        self.forward_timeout_seconds = forward_timeout_seconds
        self.allow_call_waiting_for_agents = allow_call_waiting_for_agents
        self.use_system_hunt_group_clid_setting = use_system_hunt_group_clid_setting
        self.include_hunt_group_name_in_clid = include_hunt_group_name_in_clid
        self.enable_not_reachable_forwarding = enable_not_reachable_forwarding
        self.make_busy_when_not_reachable = make_busy_when_not_reachable
        self.service_user_id = service_user_id
     
     
class User:
    """_summary_
    """
    
    def __init__(self, 
                 service_provider_id=None, 
                 group=None, 
                 user_id=None, 
                 last_name=None, 
                 first_name=None, 
                 calling_line_id_last_name=None, 
                 calling_line_id_first_name=None, 
                 hiragana_last_name=None, 
                 hiragana_first_name=None, 
                 phone_number=None, 
                 extension=None, 
                 calling_line_id_phone_number=None, 
                 password=None, 
                 department=None, 
                 department_full_path=None, 
                 language=None, 
                 time_zone=None, 
                 time_zone_display_name=None, 
                 default_alias=None, 
                 access_device_endpoint=None, 
                 title=None, 
                 pager_phone_number=None, 
                 mobile_phone_number=None, 
                 email_address=None, 
                 yahoo_id=None, 
                 address_location=None, 
                 address=None, 
                 country_code=None, 
                 network_class_of_service=None, 
                 allow_video: bool=True, 
                 domain=None, 
                 endpoint_type=None, 
                 aliases=None, 
                 trunk_addressing=None,
                 alternate_user_id=None):
        
        self.group = group.user.append(self) #this may fail
        self.user_id = user_id + group.default_domain
        self.last_name = last_name
        self.first_name = first_name
        
        self.calling_line_id_last_name = self.last_name
        self.calling_line_id_first_name = self.first_name
        self.hiragana_last_name = self.last_name
        self.hiragana_first_name = self.first_name
        self.phone_number = phone_number
        self.extension = extension
        self.calling_line_id_phone_number = calling_line_id_phone_number
        self.password = password if password is not None else gen.generate_password()
        self.department = department
        self.department_full_path = department_full_path
        self.language = language
        self.time_zone = time_zone
        self.time_zone_display_name = time_zone_display_name
        self.default_alias = default_alias
        self.access_device_endpoint = access_device_endpoint #Device object
        self.title = title
        self.pager_phone_number = pager_phone_number
        self.mobile_phone_number = mobile_phone_number
        self.email_address = email_address
        self.yahoo_id = yahoo_id
        self.address_location = address_location
        self.address = address #address object
        self.country_code = country_code
        self.network_class_of_service = network_class_of_service
        self.allow_video = allow_video
        self.domain = domain
        self.endpoint_type = endpoint_type
        self.aliases = aliases
        self.trunk_addressing = trunk_addressing
        self.alternate_user_id = alternate_user_id
        
        self.is_enterprise = group.sp_or_ent.is_enterprise
        self.password_expires_days = 2147483647
        self.service_provider_id = group.sp_or_ent.id


class Device:
    """_summary_
    """
    
    def __init__(self, 
                 type,
                 name,
                 group: Group,
                 
                 use_custom_user_name_password: bool=True, 
                 access_device_credential_name=None,
                 access_device_credential_password=None,
                 net_address=None, 
                 port=None, 
                 outbound_proxy_server_net_address=None,
                 stun_server_net_address=None,
                 mac_address=None, 
                 serial_number=None,
                 description=None, 
                 physical_location=None, 
                 transport_protocol=None,
                 profile=None,
                 static_registration_capable=None, 
                 config_type=None, 
                 protocol_choice: List[str]=None,
                 is_ip_address_optional: bool=True, 
                 use_domain: bool=True,
                 is_mobility_manager_device: bool=False, 
                 device_configuration_option=None,
                 static_line_ordering: bool=False,
                 device_type_level=None, 
                 tags: List[str]=None,
                 related_services: List[str]=None, 
                 protocol=None,
                 user_name=None):
        
        self.device_type = type
        self.device_name = name
        self.group = group
        
        self.use_custom_user_name_password = use_custom_user_name_password
        self.access_device_credential_name = access_device_credential_name
        self.access_device_credential_password = access_device_credential_password if access_device_credential_password is not None else gen.generate_password()
        self.net_address = net_address
        self.port = port
        self.outbound_proxy_server_net_address = outbound_proxy_server_net_address
        self.stun_server_net_address = stun_server_net_address
        self.mac_address = mac_address
        self.serial_number = serial_number
        self.description = description
        self.physical_location = physical_location
        self.transport_protocol = transport_protocol
        self.profile = profile
        self.static_registration_capable = static_registration_capable
        self.config_type = config_type
        self.protocol_choice = protocol_choice
        self.is_ip_address_optional = is_ip_address_optional
        self.use_domain = use_domain
        self.is_mobility_manager_device = is_mobility_manager_device
        self.device_configuration_option = device_configuration_option
        self.static_line_ordering = static_line_ordering
        self.device_type_level = device_type_level
        self.tags = tags
        self.related_services = related_services
        self.protocol = protocol
        self.user_name = user_name
        
        self.device_level = "Group"
        self.group_id = group.id
        self.service_provider_id = group.sp_or_ent.id

class Alias:
    """_summary_
    """
    
    def __init__(self, 
                 number, 
                 broadworks_entity: object):
        
        self.number = number
        self.broadworks_entity = broadworks_entity
        
        self.user_id = number + broadworks_entity.group.default_domain