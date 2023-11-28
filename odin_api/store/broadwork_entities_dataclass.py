from dataclasses import dataclass, field, InitVar
from typing import List

from odin_api.utils import generators as gen

   
@dataclass
class ServiceProvider:
    id: int
    name: str
    groups: List['Group'] = field(default_factory=list)

    isEnterprise: bool = False
    defaultDomain: str = None
    supportEmail: str = None
    contactName: str = None
    contactNumber: str = None
    contactEmail: str = None
    addressLine1: str = None
    city: str = None
    stateOrProvince: str = None
    zipOrPostcode: str = None
    country: str = None
    useServiceProviderLanguage: bool = False
   
    
@dataclass
class Group:
    ServiceProvider: 'ServiceProvider'
    groupId: int
    groupName: str
    defaultDomain: str
    userLimit: int = None
    userCount: int = None
    callingLineIdName: str = None
    callingLineIdPhoneNumber: str = None
    callingLineIdDisplayPhoneNumber: str = None
    timeZone: str = None
    timeZoneDisplayName: str = None
    locationDialingCode: str = None
    contactName: str = None
    contactNumber: str = None
    contactEmail: str = None
    addressLine1: str = None
    addressLine2: str = None
    city: str = None
    stateOrProvince: str = None
    country: str = None

    def __post_init__(self):
        self.trunk_groups: List['TrunkGroup'] = field(default_factory=list)
        self.call_centers: List['CallCenter'] = field(default_factory=list)
        self.hunt_groups: List['HuntGroup'] = field(default_factory=list)
        self.users: List['User'] = field(default_factory=list)

        self.ServiceProvider.groups.append(self)
     
        
@dataclass
class TrunkGroup:
    name: str
    group: 'Group'
    accessDevice: 'Device'
    users: List['User'] = field(default_factory=list)

    allowTerminationToDtgIdentity: bool = False
    allowTerminationToTrunkGroupIdentity: bool = False
    allowUnscreenedCalls: bool = False
    allowUnscreenedEmergencyCalls: bool = False
    capacityExceededTrapInitialCalls: int = None
    capacityExceededTrapOffsetCalls: int = None
    clidSourceForScreenedCallsPolicy: str = None
    continuousOptionsSendingIntervalSeconds: int = None
    enableBursting: bool = False
    enableNetworkAddressIdentity: bool = False
    failureOptionsSendingIntervalSeconds: int = None
    failureThresholdCounter: int = None
    includeDtgIdentity: bool = False
    includeOtgIdentityForNetworkCalls: bool = False
    includeTrunkGroupIdentity: bool = False
    includeTrunkGroupIdentityForNetworkCalls: bool = False
    invitationTimeout: int = None
    inviteFailureThresholdCounter: int = None
    inviteFailureThresholdWindowSeconds: int = None
    pilotUserCallOptimizationPolicy: str = None
    pilotUserCallingLineAssertedIdentityPolicy: str = None
    pilotUserCallingLineIdentityForEmergencyCallsPolicy: str = None
    pilotUserCallingLineIdentityForExternalCallsPolicy: str = None
    pilotUserChargeNumberPolicy: str = None
    prefixEnabled: bool = False
    requireAuthentication: bool = False
    routeToPeeringDomain: bool = False
    sendContinuousOptionsMessage: bool = False
    statefulReroutingEnabled: bool = False
    successThresholdCounter: int = None
    useSystemClidSourceForScreenedCallsPolicy: bool = False
    useSystemCallingLineAssertedIdentityPolicy: bool = False
    useSystemUserLookupPolicy: bool = False
    userLookupPolicy: str = None
    maxActiveCalls: int = None
    maxIncomingCalls: int = None
    maxOutgoingCalls: int = None

    def __post_init__(self):
        self.service_provider_id = self.group.service_provider_id.id



@dataclass
class AAKey:
    keyNumber: int
    action: str 
    description: str = None
    phoneNumber: str = None
    submenuId: int = None


@dataclass
class AAMenu:
    announcementSelection: str = None
    enableFirstMenuLevelExtensionDialing: bool = False
    keys: List[AAKey] = None

@dataclass
class AutoAttendant:
    name: str 
    group: 'Group' 
    callingLineIdLastName: str = None
    callingLineIdFirstName: str = None
    hiraganaLastName: str = None
    hiraganaFirstName: str = None
    language: str = None
    timeZone: str = None
    timeZoneDisplayName: str = None
    aliases: List[object] = None
    type: str = None
    enableVideo: bool = False
    extensionDialingScope: str = None
    nameDialingScope: str = None
    nameDialingEntries: str = None
    businessHoursMenu: 'AAMenu' = None
    afterHoursMenu: 'AAMenu' = None
    serviceUserId: str = None
    

    def __post_init__(self):
        self.serviceProviderId = self.group.ServiceProvider.id
        

@dataclass
class CallCenter:
    name: str
    group: 'Group'
    agents: List['User'] = field(default_factory=list)

    enableVideo: bool = False
    allowCallerToDialEscapeDigit: bool = False
    resetCallStatisticsUponEntryInQueue: bool = True
    allowAgentLogoff: bool = True
    allowCallWaitingForAgents: bool = True
    playRingingWhenOfferingCall: bool = True
    externalPreferredAudioCodec: str = None
    internalPreferredAudioCodec: str = None
    enableReporting: bool = False
    allowCallsToAgentsInWrapUp: bool = True
    overrideAgentWrapUpTime: bool = False
    enableAutomaticStateChangeForAgents: bool = False
    forceDeliveryOfCalls: bool = False
    type: str = None
    serviceUserIdPrefix: str = None
    callingLineIdLastName: str = None
    callingLineIdFirstName: str = None
    password: str = None
    policy: str = None
    routingType: str = None
    queueLength: int = None
    escapeDigit: str = None
    serviceUserId: str = None

    def __post_init__(self):
        self.service_provider_id = self.group.service_provider_id.id
        self.password = self.password if self.password is not None else gen.generate_password()
        
        self.group.call_centers.append(self)

#TODO: Change to camelcase
@dataclass
class HuntGroup:
    name: str
    group: 'Group'
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
    
    agents: List['User'] = field(default_factory=list)
    
    def __post_init__(self):
        self.service_provider_id = self.group.service_provider_id.id
        self.group.hunt_groups.append(self)
        
        
@dataclass
class HuntGroup:
    id: str
    group = 'Group'
    first_name = str
    last_name = str
    