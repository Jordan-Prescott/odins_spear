from dataclasses import dataclass, field, InitVar
from typing import List, Type

from odin_api.utils import generators as gen
   
@dataclass
class ServiceProvider:
    id: str
    name: str
    groups: List['Group'] = field(default_factory=list)
    is_enterprise: bool = False
    default_domain: str = None
    support_email: str = None
    contact_name: str = None
    contact_number: str = None
    contact_email: str = None
    address_line1: str = None
    city: str = None
    state_or_province: str = None
    zip_or_postcode: str = None
    country: str = None
    use_service_provider_language: bool = False
   
    
@dataclass
class Group:
    service_provider: Type['ServiceProvider']
    group_id: int
    group_name: str
    default_domain: str
    user_limit: int = None
    user_count: int = None
    calling_line_id_name: str = None
    calling_line_id_phone_number: str = None
    calling_line_id_display_phone_number: str = None
    time_zone: str = None
    time_zone_display_name: str = None
    location_dialing_code: str = None
    contact_name: str = None
    contact_number: str = None
    contact_email: str = None
    address_line1: str = None
    address_line2: str = None
    city: str = None
    state_or_province: str = None
    country: str = None
    trunk_groups: List['TrunkGroup'] = field(default_factory=list)
    call_centers: List['CallCenter'] = field(default_factory=list)
    hunt_groups: List['HuntGroup'] = field(default_factory=list)
    users: List['User'] = field(default_factory=list)

    def __post_init__(self):

        self.service_provider.groups.append(self)
     
        
@dataclass
class TrunkGroup:
    name: str
    group: Type['Group']
    access_device: Type['Device']
    users: List['User'] = field(default_factory=list)
    allow_termination_to_dtg_identity: bool = False
    allow_termination_to_trunk_group_identity: bool = False
    allow_unscreened_calls: bool = False
    allow_unscreened_emergency_calls: bool = False
    capacity_exceeded_trap_initial_calls: int = None
    capacity_exceeded_trap_offset_calls: int = None
    clid_source_for_screened_calls_policy: str = None
    continuous_options_sending_interval_seconds: int = None
    enable_bursting: bool = False
    enable_network_address_identity: bool = False
    failure_options_sending_interval_seconds: int = None
    failure_threshold_counter: int = None
    include_dtg_identity: bool = False
    include_otg_identity_for_network_calls: bool = False
    include_trunk_group_identity: bool = False
    include_trunk_group_identity_for_network_calls: bool = False
    invitation_timeout: int = None
    invite_failure_threshold_counter: int = None
    invite_failure_threshold_window_seconds: int = None
    pilot_user_call_optimization_policy: str = None
    pilot_user_calling_line_asserted_identity_policy: str = None
    pilot_user_calling_line_identity_for_emergency_calls_policy: str = None
    pilot_user_calling_line_identity_for_external_calls_policy: str = None
    pilot_user_charge_number_policy: str = None
    prefix_enabled: bool = False
    require_authentication: bool = False
    route_to_peering_domain: bool = False
    send_continuous_options_message: bool = False
    stateful_rerouting_enabled: bool = False
    success_threshold_counter: int = None
    use_system_clid_source_for_screened_calls_policy: bool = False
    use_system_calling_line_asserted_identity_policy: bool = False
    use_system_user_lookup_policy: bool = False
    user_lookup_policy: str = None
    max_active_calls: int = None
    max_incoming_calls: int = None
    max_outgoing_calls: int = None

    def __post_init__(self):
        self.service_provider_id = self.group.service_provider_id.id


@dataclass
class AAKey:
    key_number: int
    action: str
    description: str = None
    phone_number: str = None
    submenu_id: int = None


@dataclass
class AAMenu:
    announcement_selection: str = None
    enable_first_menu_level_extension_dialing: bool = False
    keys: List[AAKey] = field(default_factory=list)


@dataclass
class AutoAttendant:
    name: str
    group: Type['Group']
    calling_line_id_last_name: str = None
    calling_line_id_first_name: str = None
    hiragana_last_name: str = None
    hiragana_first_name: str = None
    language: str = None
    time_zone: str = None
    time_zone_display_name: str = None
    aliases: List[str] = field(default_factory= [list])
    type: str = None
    enable_video: bool = False
    extension_dialing_scope: str = None
    name_dialing_scope: str = None
    name_dialing_entries: str = None
    business_hours_menu: Type['AAMenu'] = None
    after_hours_menu: Type['AAMenu'] = None
    service_user_id: str = None

    def __post_init__(self):
        self.serviceProviderId = self.group.ServiceProvider.id
        

@dataclass
class CallCenter:
    name: str
    group: Type['Group']
    agents: List['User'] = field(default_factory=list)
    enable_video: bool = False
    allow_caller_to_dial_escape_digit: bool = False
    reset_call_statistics_upon_entry_in_queue: bool = True
    allow_agent_logoff: bool = True
    allow_call_waiting_for_agents: bool = True
    play_ringing_when_offering_call: bool = True
    external_preferred_audio_codec: str = None
    internal_preferred_audio_codec: str = None
    enable_reporting: bool = False
    allow_calls_to_agents_in_wrap_up: bool = True
    override_agent_wrap_up_time: bool = False
    enable_automatic_state_change_for_agents: bool = False
    force_delivery_of_calls: bool = False
    type: str = None
    service_user_id_prefix: str = None
    calling_line_id_last_name: str = None
    calling_line_id_first_name: str = None
    password: str = field(default_factory=gen.generate_password)
    policy: str = None
    routing_type: str = None
    queue_length: int = None
    escape_digit: str = None
    service_user_id: str = None

    def __post_init__(self):
        self.service_provider_id = self.group.service_provider_id.id
        self.group.call_centers.append(self)


@dataclass
class HuntGroup:
    name: str
    group: Type['Group']
    agents: List['User'] = field(default_factory=list)
    calling_line_id_last_name: str = None
    calling_line_id_first_name: str = None
    hiragana_last_name: str = None
    hiragana_first_name: str = None
    language: str = None
    time_zone: str = None
    aliases: List[str] = field(default_factory=list)
    policy: str = None
    hunt_after_no_answer: bool = None
    no_answer_number_of_rings: int = None
    forward_after_timeout: bool = None
    forward_timeout_seconds: int = None
    allow_call_waiting_for_agents: bool = None
    use_system_hunt_group_clid_setting: bool = None
    include_hunt_group_name_in_clid: bool = None
    enable_not_reachable_forwarding: bool = None
    make_busy_when_not_reachable: bool = None
    service_user_id: str = None
    service_provider_id: str = None
    group_id: str = None
    
    def __post_init__(self):
        self.service_provider_id = self.group.service_provider_id.id
        self.group.hunt_groups.append(self)
    
        
@dataclass
class User:
    group: Type['Group']
    access_device_endpoint: Type['Device'] = None
    user_id: str = None
    last_name: str = None
    first_name: str = None
    calling_line_id_last_name: str = None
    calling_line_id_first_name: str = None
    hiragana_last_name: str = None
    hiragana_first_name: str = None
    phone_number: str = None
    extension: str = None
    calling_line_id_phone_number: str = None
    password: str = None
    department: str = None
    department_full_path: str = None
    language: str = None
    time_zone: str = None
    time_zone_display_name: str = None
    default_alias: str = None
    title: str = None
    pager_phone_number: str = None
    mobile_phone_number: str = None
    email_address: str = None
    yahoo_id: str = None
    address_location: str = None
    address: Type['Address'] = None
    country_code: str = None
    network_class_of_service: str = None
    allow_video: bool = True
    domain: str = None
    endpoint_type: str = None
    aliases: List[str] = field(default_factory=list)
    trunk_addressing: str = None
    alternate_user_id: str = None
    is_enterprise: bool = False
    password_expires_days: int = 2147483647
    service_provider_id: str = None

    def __post_init__(self):
        self.is_enterprise = self.group.service_provider.is_enterprise
        self.service_provider_id = self.group.service_provider.id
        self.group.users.append(self)
 
    
@dataclass
class Device:
    device_type: str
    device_name: str
    group: Type['Group']
    device_level: Type['Group']
    use_custom_user_name_password: bool = True
    access_device_credential_name: str = None
    access_device_credential_password: str = None
    net_address: str = None
    port: str = None
    outbound_proxy_server_net_address: str = None
    stun_server_net_address: str = None
    mac_address: str = None
    serial_number: str = None
    description: str = None
    physical_location: str = None
    transport_protocol: str = None
    profile: str = None
    static_registration_capable: str = None
    config_type: str = None
    protocol_choice: List[str] = field(default_factory=list)
    is_ip_address_optional: bool = True
    use_domain: bool = True
    is_mobility_manager_device: bool = False
    device_configuration_option: str = None
    static_line_ordering: bool = False
    device_type_level: str = None
    tags: List[str] = field(default_factory=list)
    related_services: List[str] = field(default_factory=list)
    protocol: str = None
    user_name: str = None
    group_id: int = field(init=False)
    service_provider_id: int = field(init=False)

    def __post_init__(self):
        self.group_id = self.group.id
        self.service_provider_id = self.group.service_provider.id
        
        
@dataclass
class Contact:
    contact_name: str = None
    contact_number: str = None
    contact_email: str = None
    
    
@dataclass
class Address:
    address_line1: str
    address_line2: str
    city: str
    state_or_province: str
    zip_or_postal_code: str
    country: str


@dataclass
class Department:
    group: Type['Group']
    name: str
    
    def __post_init__(self):
        self.service_provider_id = self.group.service_provider.id