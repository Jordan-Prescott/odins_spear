from .base_config import BaseConfig


class AutoAttendantConfig(BaseConfig):
    def __init__(self):
        """Configuration class for Auto Attendant."""

        default_config = {
            "serviceInstanceProfile": {
                "name": "mock-aa-test-1",
                "callingLineIdLastName": "mock-aa-test-1",
                "callingLineIdFirstName": "mock-aa-test-1",
                "hiraganaLastName": "mock-aa-test-1",
                "hiraganaFirstName": "Auto Attendant",
                "language": "English",
                "timeZone": "America/Denver",
                "timeZoneDisplayName": "(GMT-06:00) (US) Mountain Time",
                "aliases": [],
            },
            "type": "Basic",
            "enableVideo": False,
            "extensionDialingScope": "Group",
            "nameDialingScope": "Group",
            "nameDialingEntries": "LastName + FirstName",
            "businessHoursMenu": {
                "announcementSelection": "Default",
                "enableFirstMenuLevelExtensionDialing": False,
                "keys": [
                    {
                        "key": "0",
                        "action": "Transfer To Operator",
                        "description": None,
                        "phoneNumber": None,
                        "submenuId": None,
                    },
                    {
                        "key": "1",
                        "action": "Extension Dialing",
                        "description": None,
                        "phoneNumber": None,
                        "submenuId": None,
                    },
                    {
                        "key": "2",
                        "action": "Name Dialing",
                        "description": None,
                        "phoneNumber": None,
                        "submenuId": None,
                    },
                ],
            },
            "afterHoursMenu": {
                "announcementSelection": "Default",
                "enableFirstMenuLevelExtensionDialing": False,
                "keys": [
                    {
                        "key": "0",
                        "action": "Transfer To Operator",
                        "description": None,
                        "phoneNumber": None,
                        "submenuId": None,
                    },
                    {
                        "key": "1",
                        "action": "Extension Dialing",
                        "description": None,
                        "phoneNumber": None,
                        "submenuId": None,
                    },
                    {
                        "key": "2",
                        "action": "Name Dialing",
                        "description": None,
                        "phoneNumber": None,
                        "submenuId": None,
                    },
                ],
            },
            "serviceUserId": "mock-aa-test-1",
            "serviceProviderId": "odin.mock.ent1",
            "groupId": "odin.mock.grp1",
            "isEnterprise": True,
        }
        super().__init__(default_config)


class CallCenterConfig(BaseConfig):
    def __init__(self):
        """Configuration class for Call Center."""

        default_config = {
            "enableVideo": False,
            "allowCallerToDialEscapeDigit": False,
            "resetCallStatisticsUponEntryInQueue": True,
            "allowAgentLogoff": True,
            "allowCallWaitingForAgents": True,
            "playRingingWhenOfferingCall": True,
            "externalPreferredAudioCodec": "None",
            "internalPreferredAudioCodec": "None",
            "enableReporting": False,
            "allowCallsToAgentsInWrapUp": True,
            "overrideAgentWrapUpTime": False,
            "enableAutomaticStateChangeForAgents": False,
            "forceDeliveryOfCalls": False,
            "type": "Premium",
            "serviceUserIdPrefix": "mock.cc.1",
            "serviceInstanceProfile": {
                "name": "mock.cc.1",
                "callingLineIdLastName": "mock.cc.1",
                "callingLineIdFirstName": "mock.cc.1",
                "password": "l@q3zC",
            },
            "policy": "Circular",
            "routingType": "Priority Based",
            "queueLength": 3,
            "escapeDigit": "3",
            "serviceProviderId": "odin.mock.ent1",
            "groupId": "odin.mock.grp1",
            "serviceUserId": "mock.cc.1@microv-works.com",
        }
        super().__init__(default_config)


class DeviceConfig(BaseConfig):
    def __init__(self):
        """Configuration class for Devices."""

        default_config = {
            "deviceType": "Polycom Soundpoint IP 4000",
            "deviceName": "my-new-device-name",
            "deviceLevel": "Group",
            "useCustomUserNamePassword": True,
            "accessDeviceCredentials": {
                "userName": "9871515000",
                "password": "ym7#zIuA",
            },
            "netAddress": "111.111.111.111",
            "port": "2222",
            "outboundProxyServerNetAddress": "222.222.222.222",
            "stunServerNetAddress": "333.333.333.333",
            "macAddress": "CBFB0EBBF325",
            "serialNumber": "123456789",
            "description": "description",
            "physicalLocation": "usa",
            "transportProtocol": "UDP",
            "groupId": "grp.odin",
            "serviceProviderId": "ent.odin",
            "profile": "Intelligent Proxy Addressing",
            "staticRegistrationCapable": "false",
            "configType": "3 File Configuration",
            "protocolChoice": ["SIP 2.0"],
            "isIpAddressOptional": "true",
            "useDomain": "true",
            "isMobilityManagerDevice": "false",
            "deviceConfigurationOption": "Device Management",
            "staticLineOrdering": "false",
            "deviceTypeLevel": "System",
            "tags": [],
            "relatedServices": [],
            "protocol": "SIP 2.0",
            "userName": "9871515000",
        }
        super().__init__(default_config)


class GroupConfig(BaseConfig):
    def __init__(self):
        """Configuration class for Groups."""

        default_config = {
            "defaultDomain": "lab.tekvoice.net",
            "userLimit": 50,
            "userCount": 13,
            "groupName": "grp.odin",
            "callingLineIdName": "grp.odin",
            "callingLineIdPhoneNumber": "+15132337655",
            "callingLineIdDisplayPhoneNumber": 5132337655,
            "timeZone": "America/Denver",
            "timeZoneDisplayName": "(GMT-06:00) (US) Mountain Time",
            "locationDialingCode": "5131",
            "contact": {
                "contactName": "Mark Reverman",
                "contactNumber": "100-454-4545",
                "contactEmail": "zmayfield@parkbenchsolutions.com",
            },
            "address": {
                "addressLine1": "4545 Main Street",
                "addressLine2": "Bldg 2",
                "city": "Cincinnati",
                "stateOrProvince": "Ohio",
                "zipOrPostalCode": "45212",
                "country": "United States",
            },
            "serviceProviderId": "ent.odin",
            "groupId": "grp.odin",
        }
        super().__init__(default_config)


class HuntGroupConfig(BaseConfig):
    def __init__(self):
        """Configuration class for Hunt Groups."""

        default_config = {
            "serviceInstanceProfile": {
                "name": "odin.mock.hg.2",
                "callingLineIdLastName": "odin.mock.hg.2",
                "callingLineIdFirstName": "odin.mock.hg.2",
                "hiraganaLastName": "odin.mock.hg.2",
                "hiraganaFirstName": "Hunt Group",
                "language": "English",
                "timeZone": "America/Denver",
                "aliases": [],
            },
            "policy": "Regular",
            "huntAfterNoAnswer": True,
            "noAnswerNumberOfRings": 5,
            "forwardAfterTimeout": False,
            "forwardTimeoutSeconds": 10,
            "allowCallWaitingForAgents": True,
            "useSystemHuntGroupCLIDSetting": True,
            "includeHuntGroupNameInCLID": True,
            "enableNotReachableForwarding": False,
            "makeBusyWhenNotReachable": False,
            "serviceUserId": "odin.mock.hg.2@microv-works.com",
            "serviceProviderId": "odin.mock.ent1",
            "groupId": "odin.mock.grp1",
            "agents": [
                {"userId": "9709580001"},
                {"userId": "9709580002"},
            ],
        }
        super().__init__(default_config)


class ServiceProviderConfig(BaseConfig):
    def __init__(self):
        """Configuration class for Service Providers."""

        default_config = {
            "serviceProviderId": "ent.odin.mock",
            "isEnterprise": True,
            "defaultDomain": "microv-works.com",
            "serviceProviderName": "Odin Mock Enterprise 2",
            "supportEmail": "support@parkbenchsolutions.com",
            "contact": {
                "contactName": "Support Team",
                "contactNumber": "111-111-1111",
                "contactEmail": "support@parkbenchsolutions.com",
            },
            "address": {
                "addressLine1": "111 This St",
                "city": "Somecity",
                "stateOrProvince": "Arizona",
                "zipOrPostalCode": "33333",
                "country": "US",
            },
            "useServiceProviderLanguages": False,
        }
        super().__init__(default_config)


class TrunkGroupConfig(BaseConfig):
    def __init__(self):
        """Configuration class for Trunk Groups."""

        default_config = {
            "allowTerminationToDtgIdentity": False,
            "allowTerminationToTrunkGroupIdentity": False,
            "allowUnscreenedCalls": False,
            "allowUnscreenedEmergencyCalls": False,
            "capacityExceededTrapInitialCalls": 0,
            "capacityExceededTrapOffsetCalls": 0,
            "clidSourceForScreenedCallsPolicy": "Profile Name Profile Number",
            "continuousOptionsSendingIntervalSeconds": 30,
            "enableBursting": False,
            "enableNetworkAddressIdentity": False,
            "failureOptionsSendingIntervalSeconds": 10,
            "failureThresholdCounter": 1,
            "includeDtgIdentity": False,
            "includeOtgIdentityForNetworkCalls": False,
            "includeTrunkGroupIdentity": False,
            "includeTrunkGroupIdentityForNetworkCalls": False,
            "invitationTimeout": 6,
            "inviteFailureThresholdCounter": 1,
            "inviteFailureThresholdWindowSeconds": 30,
            "pilotUserCallOptimizationPolicy": "Optimize For User Services",
            "pilotUserCallingLineAssertedIdentityPolicy": "Unscreened Originating Calls",
            "pilotUserCallingLineIdentityForEmergencyCallsPolicy": "No Calls",
            "pilotUserCallingLineIdentityForExternalCallsPolicy": "No Calls",
            "pilotUserChargeNumberPolicy": "No Calls",
            "prefixEnabled": False,
            "requireAuthentication": False,
            "routeToPeeringDomain": False,
            "sendContinuousOptionsMessage": False,
            "statefulReroutingEnabled": False,
            "successThresholdCounter": 1,
            "useSystemCLIDSourceForScreenedCallsPolicy": True,
            "useSystemCallingLineAssertedIdentityPolicy": True,
            "useSystemUserLookupPolicy": True,
            "userLookupPolicy": "Basic",
            "name": "odin.mock.trunk2",
            "maxActiveCalls": 2,
            "maxIncomingCalls": 2,
            "maxOutgoingCalls": 2,
            "accessDevice": {
                "serviceProviderId": "odin.mock.sp1",
                "groupId": "odin.mock.sp.grp1",
                "deviceName": "odin.mock.dev2",
                "deviceLevel": "Group",
            },
            "serviceProviderId": "odin.mock.sp1",
            "groupId": "odin.mock.sp.grp1",
        }
        super().__init__(default_config)


class UserConfig(BaseConfig):
    def __init__(self):
        """Configuration class for Users."""

        default_config = {
            "serviceProviderId": "ent.odin",
            "groupId": "grp.odin",
            "userId": "test1234-1234@odinapi.net",
            "lastName": "Reverman",
            "firstName": "Mark",
            "callingLineIdLastName": "Reverman",
            "callingLineIdFirstName": "Mark",
            "hiraganaLastName": "Reverman",
            "hiraganaFirstName": "Mark",
            "phoneNumber": "5136549858",
            "extension": "9858",
            "callingLineIdPhoneNumber": "5136549858",
            "password": "Test12341234@odinapi.net",
            "department": {
                "serviceProviderId": "ent.odin",
                "groupId": "grp.odin",
                "name": "department1",
            },
            "departmentFullPath": "department1 (grp.odin)",
            "language": "English",
            "timeZone": "America/New_York",
            "timeZoneDisplayName": "(GMT-05:00) (US) Eastern Time",
            "defaultAlias": "test1234-1234@odinapi.net",
            "accessDeviceEndpoint": {
                "accessDevice": {
                    "deviceType": "Generic SIP Phone",
                    "protocol": "SIP 2.0",
                    "numberOfPorts": {"unlimited": "true"},
                    "numberOfAssignedPorts": 1,
                    "status": "Online",
                    "transportProtocol": "Unspecified",
                    "useCustomUserNamePassword": False,
                    "version": "Kapanga Softphone Desktop Windows 1.00/2180b+1595505876_80E82C997FFA_A0510BEA6293_02004C4F4F50_005056C00001_005056C00008_0A002700000E_FABBC859EAB4_A0510BEA6290_A2510BEA628F",
                    "deviceName": "generic_sip",
                    "macAddress": "",
                    "deviceLevel": "Group",
                    "accessDeviceCredentials": {"userName": None},
                    "serviceProviderId": "ent.odin",
                    "groupId": "grp.odin",
                    "tags": [],
                    "relatedServices": [],
                },
                "linePort": "test1234-1234@odinapi.net",
                "staticRegistrationCapable": "true",
                "useDomain": "true",
                "supportVisualDeviceManagement": "false",
                "contacts": [],
            },
            "title": "mreverman@parkbenchsolutions.com",
            "pagerPhoneNumber": 9871515000,
            "mobilePhoneNumber": 9871515000,
            "emailAddress": "mreverman@parkbenchsolutions.com",
            "yahooId": "mreverman@gmail.com",
            "addressLocation": "1234 Main Street",
            "address": {
                "addressLine1": "Bldg 1",
                "addressLine2": "Suite 2",
                "city": "Cincinnat",
                "stateOrProvince": "Ohio",
                "zipOrPostalCode": "45204",
                "country": "US",
            },
            "countryCode": "1",
            "networkClassOfService": "testncosuu",
            "allowVideo": True,
            "domain": "odinapi.net",
            "endpointType": "accessDeviceEndpoint",
            "aliases": [],
            "trunkAddressing": {
                "trunkGroupDeviceEndpoint": {"contacts": []},
            },
            "isEnterprise": True,
            "passwordExpiresDays": 2147483647,
            "alternateUserId": [
                {
                    "description": "mreverman-2@parkbenchsolutions.com",
                    "alternateUserId": "mreverman-2@parkbenchsolutions.com",
                },
                {
                    "description": "mark.reverman-2@parkbenchsolutions.com",
                    "alternateUserId": "mark.reverman-2@parkbenchsolutions.com",
                },
                {
                    "description": "mreverman-2@odinweb.net",
                    "alternateUserId": "mreverman-2@odinweb.net",
                },
            ],
        }
        super().__init__(default_config)
