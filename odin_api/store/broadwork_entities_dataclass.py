from dataclasses import dataclas, field, InitVar
from typing import List

from odin_api.utils import generators as gen


@dataclass
class ServiceProvider:
    id: int
    name: str
    groups: List['Group'] = []

    is_enterprise: bool = False
    default_domain: str = None

    support_email: str = None
    contact_name: str = None
    contact_number: str = None
    contact_email: str = None

    address_line_1: str = None
    city: str = None
    state_or_province: str = None
    zip_or_postcode: str = None
    country: str = None

    use_service_provider_language: bool = False
    
    
    
@dataclass
class ServiceProvider:
    serviceId: int
    serviceName: str
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