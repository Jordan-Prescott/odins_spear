from typing import List

from odin_api.utils import generators as gen

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
        """_summary_

        Args:
            id (_type_): _description_
            name (_type_): _description_
            default_domain (_type_, optional): _description_. Defaults to None.
            support_email (_type_, optional): _description_. Defaults to None.
            contact_name (_type_, optional): _description_. Defaults to None.
            contact_number (_type_, optional): _description_. Defaults to None.
            contact_email (_type_, optional): _description_. Defaults to None.
            address_line_1 (_type_, optional): _description_. Defaults to None.
            city (_type_, optional): _description_. Defaults to None.
            state_or_province (_type_, optional): _description_. Defaults to None.
            zip_or_postcode (_type_, optional): _description_. Defaults to None.
            country (_type_, optional): _description_. Defaults to None.
            use_service_provider_language (bool, optional): _description_. Defaults to False.
        """
        
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


class Enterprise(ServiceProvider):
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
        """_summary_

        Args:
            id (_type_): _description_
            name (_type_): _description_
            default_domain (_type_, optional): _description_. Defaults to None.
            support_email (_type_, optional): _description_. Defaults to None.
            contact_name (_type_, optional): _description_. Defaults to None.
            contact_number (_type_, optional): _description_. Defaults to None.
            contact_email (_type_, optional): _description_. Defaults to None.
            address_line_1 (_type_, optional): _description_. Defaults to None.
            city (_type_, optional): _description_. Defaults to None.
            state_or_province (_type_, optional): _description_. Defaults to None.
            zip_or_postcode (_type_, optional): _description_. Defaults to None.
            country (_type_, optional): _description_. Defaults to None.
            use_service_provider_language (bool, optional): _description_. Defaults to False.
        """
        
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
                 default_domain, 
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
        """_summary_

        Args:
            sp_or_ent (_type_): _description_
            id (_type_): _description_
            name (_type_): _description_
            default_domain (_type_, optional): _description_. Defaults to None.
            user_limit (_type_, optional): _description_. Defaults to None.
            user_count (_type_, optional): _description_. Defaults to None.
            calling_line_id_name (_type_, optional): _description_. Defaults to None.
            calling_line_id_phone_number (_type_, optional): _description_. Defaults to None.
            calling_line_id_display_phone_number (_type_, optional): _description_. Defaults to None.
            time_zone (_type_, optional): _description_. Defaults to None.
            time_zone_display_name (_type_, optional): _description_. Defaults to None.
            location_dialing_code (_type_, optional): _description_. Defaults to None.
            contact_name (_type_, optional): _description_. Defaults to None.
            contact_number (_type_, optional): _description_. Defaults to None.
            contact_email (_type_, optional): _description_. Defaults to None.
            address_line_1 (_type_, optional): _description_. Defaults to None.
            address_line_2 (_type_, optional): _description_. Defaults to None.
            city (_type_, optional): _description_. Defaults to None.
            state_or_province (_type_, optional): _description_. Defaults to None.
            country (_type_, optional): _description_. Defaults to None.
        """
        
        self.sp_or_ent = sp_or_ent
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
        
        self.sp_or_ent.groups.append(self)


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
        """_summary_

        Args:
            name (_type_): _description_
            group (_type_): _description_
            access_device (_type_): _description_
            users (list[object]): _description_
            allow_termination_to_dtg_identity (bool, optional): _description_. Defaults to False.
            allow_termination_to_trunk_group_identity (bool, optional): _description_. Defaults to False.
            allow_unscreened_calls (bool, optional): _description_. Defaults to False.
            allow_unscreened_emergency_calls (bool, optional): _description_. Defaults to False.
            capacity_exceeded_trap_initial_calls (_type_, optional): _description_. Defaults to None.
            capacity_exceeded_trap_offset_calls (_type_, optional): _description_. Defaults to None.
            clid_source_for_screened_calls_policy (_type_, optional): _description_. Defaults to None.
            continuous_options_sending_interval_seconds (_type_, optional): _description_. Defaults to None.
            enable_bursting (bool, optional): _description_. Defaults to False.
            enable_network_address_identity (bool, optional): _description_. Defaults to False.
            failure_options_sending_interval_seconds (_type_, optional): _description_. Defaults to None.
            failure_threshold_counter (_type_, optional): _description_. Defaults to None.
            include_dtg_identity (bool, optional): _description_. Defaults to False.
            include_otg_identity_for_network_calls (bool, optional): _description_. Defaults to False.
            include_trunk_group_identity (bool, optional): _description_. Defaults to False.
            include_trunk_group_identity_for_network_calls (bool, optional): _description_. Defaults to False.
            invitation_timeout (_type_, optional): _description_. Defaults to None.
            invite_failure_threshold_counter (_type_, optional): _description_. Defaults to None.
            invite_failure_threshold_window_seconds (_type_, optional): _description_. Defaults to None.
            pilot_user_call_optimization_policy (_type_, optional): _description_. Defaults to None.
            pilot_user_calling_line_asserted_identity_policy (_type_, optional): _description_. Defaults to None.
            pilot_user_calling_line_identity_for_emergency_calls_policy (_type_, optional): _description_. Defaults to None.
            pilot_user_calling_line_identity_for_external_calls_policy (_type_, optional): _description_. Defaults to None.
            pilot_user_charge_number_policy (_type_, optional): _description_. Defaults to None.
            prefix_enabled (bool, optional): _description_. Defaults to False.
            require_authentication (bool, optional): _description_. Defaults to False.
            route_to_peering_domain (bool, optional): _description_. Defaults to False.
            send_continuous_options_message (bool, optional): _description_. Defaults to False.
            stateful_rerouting_enabled (bool, optional): _description_. Defaults to False.
            success_threshold_counter (_type_, optional): _description_. Defaults to None.
            use_system_clid_source_for_screened_calls_policy (bool, optional): _description_. Defaults to False.
            use_system_calling_line_asserted_identity_policy (bool, optional): _description_. Defaults to False.
            use_system_user_lookup_policy (bool, optional): _description_. Defaults to False.
            user_lookup_policy (_type_, optional): _description_. Defaults to None.
            max_active_calls (_type_, optional): _description_. Defaults to None.
            max_incoming_calls (_type_, optional): _description_. Defaults to None.
            max_outgoing_calls (_type_, optional): _description_. Defaults to None.
        """
         
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
        """_summary_

        Args:
            key_number (_type_, optional): _description_. Defaults to None.
            action (_type_, optional): _description_. Defaults to None.
            description (_type_, optional): _description_. Defaults to None.
            phone_number (_type_, optional): _description_. Defaults to None.
            submenu_id (_type_, optional): _description_. Defaults to None.
        """
        
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
        """_summary_

        Args:
            announcement_selection (_type_, optional): _description_. Defaults to None.
            enable_first_menu_level_extension_dialing (bool, optional): _description_. Defaults to False.
            keys (List[AAKey], optional): _description_. Defaults to None.
        """
        
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
        """_summary_

        Args:
            name (_type_, optional): _description_. Defaults to None.
            calling_line_id_last_name (_type_, optional): _description_. Defaults to None.
            calling_line_id_first_name (_type_, optional): _description_. Defaults to None.
            hiragana_last_name (_type_, optional): _description_. Defaults to None.
            hiragana_first_name (_type_, optional): _description_. Defaults to None.
            language (_type_, optional): _description_. Defaults to None.
            time_zone (_type_, optional): _description_. Defaults to None.
            time_zone_display_name (_type_, optional): _description_. Defaults to None.
            aliases (List[object], optional): _description_. Defaults to None.
            type (_type_, optional): _description_. Defaults to None.
            enable_video (bool, optional): _description_. Defaults to False.
            extension_dialing_scope (_type_, optional): _description_. Defaults to None.
            name_dialing_scope (_type_, optional): _description_. Defaults to None.
            name_dialing_entries (_type_, optional): _description_. Defaults to None.
            business_hours_menu (AAMenu, optional): _description_. Defaults to None.
            after_hours_menu (AAMenu, optional): _description_. Defaults to None.
            service_user_id (_type_, optional): _description_. Defaults to None.
            group (_type_, optional): _description_. Defaults to None.
        """
        
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
        """_summary_

        Args:
            name (_type_): _description_
            group (_type_): _description_
            agents (List[object], optional): _description_. Defaults to None.
            enable_video (bool, optional): _description_. Defaults to False.
            allow_caller_to_dial_escape_digit (bool, optional): _description_. Defaults to False.
            reset_call_statistics_upon_entry_in_queue (bool, optional): _description_. Defaults to True.
            allow_agent_logoff (bool, optional): _description_. Defaults to True.
            allow_call_waiting_for_agents (bool, optional): _description_. Defaults to True.
            play_ringing_when_offering_call (bool, optional): _description_. Defaults to True.
            external_preferred_audio_codec (_type_, optional): _description_. Defaults to None.
            internal_preferred_audio_codec (_type_, optional): _description_. Defaults to None.
            enable_reporting (bool, optional): _description_. Defaults to False.
            allow_calls_to_agents_in_wrap_up (bool, optional): _description_. Defaults to True.
            override_agent_wrap_up_time (bool, optional): _description_. Defaults to False.
            enable_automatic_state_change_for_agents (bool, optional): _description_. Defaults to False.
            force_delivery_of_calls (bool, optional): _description_. Defaults to False.
            type (_type_, optional): _description_. Defaults to None.
            service_user_id_prefix (_type_, optional): _description_. Defaults to None.
            calling_line_id_last_name (_type_, optional): _description_. Defaults to None.
            calling_line_id_first_name (_type_, optional): _description_. Defaults to None.
            password (_type_, optional): _description_. Defaults to None.
            policy (_type_, optional): _description_. Defaults to None.
            routing_type (_type_, optional): _description_. Defaults to None.
            queue_length (_type_, optional): _description_. Defaults to None.
            escape_digit (_type_, optional): _description_. Defaults to None.
            service_user_id (_type_, optional): _description_. Defaults to None.
        """
        
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
        """_summary_

        Args:
            name (_type_): _description_
            group (_type_): _description_
            agents (List[object], optional): _description_. Defaults to None.
            calling_line_id_last_name (_type_, optional): _description_. Defaults to None.
            calling_line_id_first_name (_type_, optional): _description_. Defaults to None.
            hiragana_last_name (_type_, optional): _description_. Defaults to None.
            hiragana_first_name (_type_, optional): _description_. Defaults to None.
            language (_type_, optional): _description_. Defaults to None.
            time_zone (_type_, optional): _description_. Defaults to None.
            aliases (_type_, optional): _description_. Defaults to None.
            policy (_type_, optional): _description_. Defaults to None.
            hunt_after_no_answer (_type_, optional): _description_. Defaults to None.
            no_answer_number_of_rings (_type_, optional): _description_. Defaults to None.
            forward_after_timeout (_type_, optional): _description_. Defaults to None.
            forward_timeout_seconds (_type_, optional): _description_. Defaults to None.
            allow_call_waiting_for_agents (_type_, optional): _description_. Defaults to None.
            use_system_hunt_group_clid_setting (_type_, optional): _description_. Defaults to None.
            include_hunt_group_name_in_clid (_type_, optional): _description_. Defaults to None.
            enable_not_reachable_forwarding (_type_, optional): _description_. Defaults to None.
            make_busy_when_not_reachable (_type_, optional): _description_. Defaults to None.
            service_user_id (_type_, optional): _description_. Defaults to None.
        """
        
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
                 group, 
                 user_id, 
                 last_name, 
                 first_name, 
                 extension, 
                 calling_line_id_last_name=None, 
                 calling_line_id_first_name=None, 
                 hiragana_last_name=None, 
                 hiragana_first_name=None, 
                 phone_number=None, 
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
        """_summary_

        Args:
            service_provider_id (_type_, optional): _description_. Defaults to None.
            group (_type_, optional): _description_. Defaults to None.
            user_id (_type_, optional): _description_. Defaults to None.
            last_name (_type_, optional): _description_. Defaults to None.
            first_name (_type_, optional): _description_. Defaults to None.
            calling_line_id_last_name (_type_, optional): _description_. Defaults to None.
            calling_line_id_first_name (_type_, optional): _description_. Defaults to None.
            hiragana_last_name (_type_, optional): _description_. Defaults to None.
            hiragana_first_name (_type_, optional): _description_. Defaults to None.
            phone_number (_type_, optional): _description_. Defaults to None.
            extension (_type_, optional): _description_. Defaults to None.
            calling_line_id_phone_number (_type_, optional): _description_. Defaults to None.
            password (_type_, optional): _description_. Defaults to None.
            department (_type_, optional): _description_. Defaults to None.
            department_full_path (_type_, optional): _description_. Defaults to None.
            language (_type_, optional): _description_. Defaults to None.
            time_zone (_type_, optional): _description_. Defaults to None.
            time_zone_display_name (_type_, optional): _description_. Defaults to None.
            default_alias (_type_, optional): _description_. Defaults to None.
            access_device_endpoint (_type_, optional): _description_. Defaults to None.
            title (_type_, optional): _description_. Defaults to None.
            pager_phone_number (_type_, optional): _description_. Defaults to None.
            mobile_phone_number (_type_, optional): _description_. Defaults to None.
            email_address (_type_, optional): _description_. Defaults to None.
            yahoo_id (_type_, optional): _description_. Defaults to None.
            address_location (_type_, optional): _description_. Defaults to None.
            address (_type_, optional): _description_. Defaults to None.
            country_code (_type_, optional): _description_. Defaults to None.
            network_class_of_service (_type_, optional): _description_. Defaults to None.
            allow_video (bool, optional): _description_. Defaults to True.
            domain (_type_, optional): _description_. Defaults to None.
            endpoint_type (_type_, optional): _description_. Defaults to None.
            aliases (_type_, optional): _description_. Defaults to None.
            trunk_addressing (_type_, optional): _description_. Defaults to None.
            alternate_user_id (_type_, optional): _description_. Defaults to None.
        """
        
        self.group = group
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
        
        self.group.users.append(self)


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
        """_summary_

        Args:
            type (_type_): _description_
            name (_type_): _description_
            group (Group): _description_
            use_custom_user_name_password (bool, optional): _description_. Defaults to True.
            access_device_credential_name (_type_, optional): _description_. Defaults to None.
            access_device_credential_password (_type_, optional): _description_. Defaults to None.
            net_address (_type_, optional): _description_. Defaults to None.
            port (_type_, optional): _description_. Defaults to None.
            outbound_proxy_server_net_address (_type_, optional): _description_. Defaults to None.
            stun_server_net_address (_type_, optional): _description_. Defaults to None.
            mac_address (_type_, optional): _description_. Defaults to None.
            serial_number (_type_, optional): _description_. Defaults to None.
            description (_type_, optional): _description_. Defaults to None.
            physical_location (_type_, optional): _description_. Defaults to None.
            transport_protocol (_type_, optional): _description_. Defaults to None.
            profile (_type_, optional): _description_. Defaults to None.
            static_registration_capable (_type_, optional): _description_. Defaults to None.
            config_type (_type_, optional): _description_. Defaults to None.
            protocol_choice (List[str], optional): _description_. Defaults to None.
            is_ip_address_optional (bool, optional): _description_. Defaults to True.
            use_domain (bool, optional): _description_. Defaults to True.
            is_mobility_manager_device (bool, optional): _description_. Defaults to False.
            device_configuration_option (_type_, optional): _description_. Defaults to None.
            static_line_ordering (bool, optional): _description_. Defaults to False.
            device_type_level (_type_, optional): _description_. Defaults to None.
            tags (List[str], optional): _description_. Defaults to None.
            related_services (List[str], optional): _description_. Defaults to None.
            protocol (_type_, optional): _description_. Defaults to None.
            user_name (_type_, optional): _description_. Defaults to None.
        """
        
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
        """_summary_

        Args:
            number (_type_): _description_
            broadworks_entity (object): _description_
        """
        
        self.number = number
        self.broadworks_entity = broadworks_entity
        
        self.user_id = number + broadworks_entity.group.default_domain