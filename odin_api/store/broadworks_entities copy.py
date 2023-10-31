from typing import List

class ServiceProvider:
    def __init__(self, id, name, default_domain=None, support_email=None, 
                 contact_name=None, contact_number=None, contact_email=None,
                 address_line_1=None, city=None, state_or_province=None, 
                 zip_or_postcode=None, country=None, use_service_provider_language=False):
        
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
    def __init__(self, id, name, default_domain=None, support_email=None, 
                 contact_name=None, contact_number=None, contact_email=None,
                 address_line_1=None, city=None, state_or_province=None, 
                 zip_or_postcode=None, country=None, use_service_provider_language=False):
        
        super().__init__(default_domain=None, support_email=None, 
                 contact_name=None, contact_number=None, contact_email=None,
                 address_line_1=None, city=None, state_or_province=None, 
                 zip_or_postcode=None, country=None, use_service_provider_language=False)

        self.id = id 
        self.name = name

        self.is_enterprise = True


class Group():
    def __init__(self, sp_or_ent, id, name, default_domain=None, ):
        
        self.sp_or_ent = sp_or_ent.groups.append(self) #TODO: This may fail
        self.id = id
        self.name = name

        self.default_domain = default_domain






        