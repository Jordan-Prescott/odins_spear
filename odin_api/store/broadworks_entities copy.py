from typing import List

class ServiceProvider:
    """_summary_
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
                 users: list[User],
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
    def __init__(self, 
                 announcement_selection=None, 
                 enable_first_menu_level_extension_dialing: bool=False,
                 keys: List[AAKey]=None
                 ) -> None:
        
        self.announcement_selection = announcement_selection
        self.enable_first_menu_level_extension_dialing = enable_first_menu_level_extension_dialing
        self.keys = keys
        

class AutoAttendant:
    def __int__(self, 
                name=None, 
                calling_line_id_last_name=None, 
                calling_line_id_first_name=None, 
                hiragana_last_name=None, 
                hiragana_first_name=None, 
                language=None, 
                time_zone=None, 
                time_zone_display_name=None, 
                aliases: List[Alias]=None,
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
        


