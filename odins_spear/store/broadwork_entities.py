from dataclasses import dataclass, field
from typing import List, Type


@dataclass(kw_only=True)
class ServiceProvider:
    id: str
    name: str
    groups: List["Group"] = field(default_factory=list)
    is_enterprise: bool = False

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("serviceProviderId"),
            name=data.get("serviceProviderId"),
            is_enterprise=data.get("isEnterprise"),
        )


@dataclass(kw_only=True)
class Group:
    service_provider: Type["ServiceProvider"]
    id: str
    name: str
    default_domain: str
    calling_line_id_phone_number: str = None
    auto_attendants: List["AutoAttendant"] = field(default_factory=list)
    trunk_groups: List["TrunkGroup"] = field(default_factory=list)
    call_centers: List["CallCenter"] = field(default_factory=list)
    hunt_groups: List["HuntGroup"] = field(default_factory=list)
    users: List["User"] = field(default_factory=list)

    def __post_init__(self):
        self.service_provider.groups.append(self)
        self.default_domain = "@" + self.default_domain

    @classmethod
    def from_dict(cls, service_provider: ServiceProvider, data):
        return cls(
            service_provider=service_provider,
            id=data.get("groupId"),
            name=data.get("groupName"),
            default_domain=data.get("defaultDomain"),
            calling_line_id_phone_number=data.get("callingLineIdPhoneNumber"),
        )


@dataclass(kw_only=True)
class TrunkGroup:
    service_user_id: str
    group: Type["Group"]
    users: List["User"] = field(default_factory=list)
    max_active_calls: int = None
    bursting_enabled: bool = False
    bursting_max_active_calls: bool = False
    pilot_user_id: str = None

    def __post_init__(self):
        self.group.trunk_groups.append(self)

    @classmethod
    def from_dict(cls, group: Group, data):
        # gather user IDs to gather user object
        user_ids = [agent["userId"] for agent in data["agents"]]
        users = _get_user_object_from_id(group, user_ids)

        return cls(
            service_user_id=data.get(""),
            group=group,
            users=users,
            max_active_calls=data.get("maxActiveCalls"),
            bursting_enabled=data.get("enableBursting"),
            bursting_max_active_calls=data.get("burstingMaxActiveCalls"),
            pilot_user_id=data.get("pilotUserId"),
        )


@dataclass(kw_only=True)
class AAKey:
    number: int
    action: str
    description: str = None
    phone_number: str = None
    submenu_id: int = None

    @classmethod
    def from_dict(cls, data):
        return cls(
            number=data.get("key"),
            action=data.get("action"),
            description=data.get("description"),
            phone_number=data.get("phoneNumber"),
            submenu_id=data.get("submenuId"),
        )


@dataclass(kw_only=True)
class AAMenu:
    enable_first_menu_level_extension_dialing: bool = False
    keys: List[AAKey] = field(default_factory=list)


@dataclass(kw_only=True)
class AutoAttendant:
    service_user_id: str
    name: str
    group: Type["Group"]
    extension: str = None
    phone_number: str = None
    aliases: List[str] = field(default_factory=[list])
    type: str = None
    business_hours_menu: Type["AAMenu"] = None
    after_hours_menu: Type["AAMenu"] = None

    def __post_init__(self):
        self.group.auto_attendants.append(self)

    @classmethod
    def from_dict(cls, group: Group, data):
        return cls(
            service_user_id=data.get("serviceUserId"),
            name=data.get("serviceInstanceProfile").get("name"),
            group=group,
            extension=data.get("serviceInstanceProfile").get("extension"),
            phone_number=data.get("serviceInstanceProfile").get("phoneNumber"),
            aliases=data.get("serviceInstanceProfile").get("aliases"),
            type=data.get("type"),
            business_hours_menu=AAMenu(
                enable_first_menu_level_extension_dialing=data.get(
                    "businessHoursMenu"
                ).get("enableFirstMenuLevelExtensionDialing"),
                keys=[
                    AAKey.from_dict(key)
                    for key in data.get("businessHoursMenu").get("keys")
                ],
            ),
            after_hours_menu=AAMenu(
                enable_first_menu_level_extension_dialing=data.get(
                    "afterHoursMenu"
                ).get("enableFirstMenuLevelExtensionDialing"),
                keys=[
                    AAKey.from_dict(key)
                    for key in data.get("afterHoursMenu").get("keys")
                ],
            ),
        )


@dataclass(kw_only=True)
class CallCenter:
    service_user_id: str
    group: Type["Group"]
    agents: List["User"] = field(default_factory=list)
    extension: str = None
    phone_number: str = None
    aliases: List[str] = field(default_factory=list)
    name: str = None
    type: str = None
    policy: str = None

    bounced_calls_enabled: bool = False
    overflow_calls_action: str = None
    overflow_calls_transfer_to_phone_number: bool = False
    stranded_calls_action: str = None
    stranded_calls_transfer_to_phone_number: bool = False
    stranded_call_unavailable_action: str = None
    stranded_call_unavailable_transfer_to_phone_number: bool = False

    # NOTE: Not sure which forwarding this is.
    forced_forwarding_enabled: bool = False
    forced_forwarding_forward_to_phone_number: str = None

    night_service: str = None
    holiday_service: str = None

    def __post_init__(self):
        self.group.call_centers.append(self)

    @classmethod
    def from_dict(cls, group: Group, data):
        # gather user IDs to gather user object
        try:
            agent_ids = [agent["userId"] for agent in data["agents"]]
            agents = _get_user_object_from_id(group, agent_ids)
        except KeyError:
            agents = []

        return cls(
            service_user_id=data.get("serviceUserId"),
            group=group,
            agents=agents,
            extension=data.get("serviceInstanceProfile").get("extension"),
            phone_number=data.get("serviceInstanceProfile").get("phoneNumber"),
            name=data.get("serviceInstanceProfile").get("name"),
            aliases=data.get("serviceInstanceProfile").get("aliases"),
            type=data.get("type"),
            policy=data.get("policy"),
            bounced_calls_enabled=data.get("bouncedCallsEnabled"),
            overflow_calls_action=data.get("overFlowCallsAction"),
            overflow_calls_transfer_to_phone_number=data.get(
                "overflowCallsTransferToPhoneNumber"
            ),
            stranded_calls_action=data.get("strandedCallsAction"),
            stranded_calls_transfer_to_phone_number=data.get(
                "strandedCallsTransferToPhoneNumber"
            ),
            stranded_call_unavailable_action=data.get("strandedCallUnavailableAction"),
            stranded_call_unavailable_transfer_to_phone_number=data.get(
                "strandedCallUnavailableTransferToPhoneNumber"
            ),
            # NOTE: Not sure which forwarding this is.
            forced_forwarding_enabled=data.get("forcedForwardingEnabled"),
            forced_forwarding_forward_to_phone_number=data.get(
                "forcedForwardingEnabled"
            ),
            night_service=data.get("nightService"),
            holiday_service=data.get("holidayService"),
        )


@dataclass(kw_only=True)
class HuntGroup:
    service_user_id: str
    name: str
    group: Type["Group"]
    agents: List["User"] = field(default_factory=list)
    aliases: List[str] = field(default_factory=list)
    extension: str = None
    phone_number: str = None
    policy: str = None

    forward_after_timeout_enabled: bool = False
    forward_timeout_seconds: int = None
    no_answer_number_of_rings: int = None
    no_answer_forward_to_phone_number: str = None

    call_forward_not_reachable_enabled: bool = False
    call_forward_not_reachable_transfer_to_phone_number: str = None

    def __post_init__(self):
        self.group.hunt_groups.append(self)

    @classmethod
    def from_dict(cls, group: Group, data):
        # gather user IDs to gather user object
        agent_ids = [agent["userId"] for agent in data["agents"]]
        agents = _get_user_object_from_id(group, agent_ids)

        return cls(
            service_user_id=data.get("serviceUserId"),
            name=data.get("serviceInstanceProfile").get("name"),
            group=group,
            agents=agents,
            aliases=data.get("serviceInstanceProfile").get("aliases"),
            extension=data.get("serviceInstanceProfile").get("extension"),
            phone_number=data.get("serviceInstanceProfile").get("phoneNumber"),
            policy=data.get("policy"),
            forward_after_timeout_enabled=data.get("forwardAfterTimeout"),
            forward_timeout_seconds=data.get("forwardTimeoutSeconds"),
            no_answer_number_of_rings=data.get("noAnswerNumberOfRings"),
            no_answer_forward_to_phone_number=data.get("forwardToPhoneNumber"),
            call_forward_not_reachable_enabled=data.get("enableNotReachableForwarding"),
            call_forward_not_reachable_transfer_to_phone_number=data.get(
                "notReachableForwardToPhoneNumber"
            ),
        )


@dataclass(kw_only=True)
class User:
    group: Type["Group"]
    id: str
    first_name: str = None
    last_name: str = None
    extension: str = None
    phone_number: str = None
    aliases: List[str] = field(default_factory=list)

    call_forwarding_always: str = None
    call_forwarding_busy: str = None
    call_forwarding_no_answer: str = None
    call_forwarding_not_reachable: str = None

    def __post_init__(self):
        self.group.users.append(self)

    @classmethod
    def from_dict(cls, group: Group, data):
        return cls(
            group=group,
            id=data.get("userId"),
            first_name=data.get("firstName"),
            last_name=data.get("lastName"),
            extension=data.get("extension"),
            phone_number=data.get("phoneNumber"),
            aliases=data.get("aliases"),
        )


@dataclass(kw_only=True)
class Contact:
    name: str = None
    number: str = None
    email: str = None

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            number=data.get("number"),
            email=data.get("email"),
        )


@dataclass(kw_only=True)
class Address:
    address_line1: str
    address_line2: str
    city: str
    state_or_province: str
    zip_or_postal_code: str
    country: str

    @classmethod
    def from_dict(cls, data):
        return cls(
            address_line1=data.get("addressLine1"),
            address_line2=data.get("addressLine2"),
            city=data.get("city"),
            state_or_province=data.get("stateOrProvince"),
            zip_or_postal_code=data.get("zipOrPostalCode"),
            country=data.get("country"),
        )


@dataclass(kw_only=True)
class Department:
    service_provider_id: str
    group_id: str
    name: str

    @classmethod
    def from_dict(cls, data):
        return cls(
            service_provider_id=data.get("serviceProviderId"),
            group_id=data.get("groupId"),
            name=data.get("name"),
        )


def _get_user_object_from_id(group, user_ids: list):
    return list(
        filter(
            lambda user: any(user_id in user.id for user_id in user_ids), group.users
        )
    )
