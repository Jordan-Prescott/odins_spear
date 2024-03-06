from odins_spear.utils.formatting import format_filter


class Get():

    filters = [
        "macAddress", "lastName", "firstName", "dn",
        "emailAddress", "userId", "extension"
    ]

    def __init__(self, requester):
        self.requester = requester

# SESSION

    def session(self):

        endpoint = f"/auth/session"

        return self.requester.get(endpoint)

# ACCOUNT AUTHORIZATION CODES
# ADMINISTRATORS
# ADVICE OF CHARGE
# ALTERNATE NUMBERS
# ANSWER CONFIRMATION
# ALTERNATE USER ID
# ANNOUNCEMENTS
# ANONYMOUS CALL REJECTION
# ATTENDANT CONSOLE
# AUTHENTICATION
# AUTO ATTENDANTS

    def auto_attendants(self, service_provider_id, group_id):

        endpoint = f"/groups/auto-attendants?serviceProviderId={service_provider_id}&groupId={group_id}"

        return self.requester.get(endpoint)

    def auto_attendant(self, service_user_id):

        endpoint = f"/groups/auto-attendants?serviceUserId={service_user_id}"

        return self.requester.get(endpoint)

# AUTOMATIC CALLBACK
# AUTOMATIC HOLD RETRIEVE
# BARGE IN EXEMPT
# BASIC CALL LOGS
# BROADWORKS ANYWHERE
# BROADWORKS MOBILITY
# BROADWORKS NAVIGATION
# BROADWORKS RECEPTIONIST ENTERPRISE
# BROADWORKS RECEPTIONIST OFFICE
# BROADWORKS RECEPTIONIST SMALL BUSINESS
# BUSY LAMP FIELD
# CALL CAPACITY
# CALL CENTER

    def group_call_centers(self, service_provider_id: str, group_id: str):

        endpoint = f"/groups/call-centers?serviceProviderId={service_provider_id}&groupId={group_id}"

        return self.requester.get(endpoint)

    def group_call_center(self, service_user_id: str):

        endpoint = f"/groups/call-centers?serviceUserId={service_user_id}"

        return self.requester.get(endpoint)

    def user_call_center(self, user_id: str):

        endpoint = f"/users/call-center?userId={user_id}"

        return self.requester.get(endpoint)

# CALL CONTROL
# CALL FORWARDING ALWAYS
# CALL FORWARDING ALWAYS SECONDARY
# CALL FORWARDING BUSY
# CALL FORWARDING NO ANSWER
# CALL FORWARDING NOT REACHABLE
# CALL FORWARDING SELECTIVE
# CALL FORWARDING SETTINGS
# CALL NOTIFY
# CALL PARK
# CALL PICKUP

    def call_pickup_group_user(self, service_provider_id, group_id, user_id):

        endpoint = f"/groups/call-pickup/user?serviceProviderId={service_provider_id}&groupId={group_id}&userId={user_id}"

        return self.requester.get(endpoint)

# CALL POLICIES
# CALL PROCESSING POLICIES
# CALL RECORDING
# CALL RECORDS
# CALL TRANSFER
# CALL WAITING
# CALLING LINE ID BLOCKING OVERRIDE
# CALLING LINE ID DELIVERY BLOCKING
# CALLING NAME DELIVERY
# CALLING NAME RETRIEVAL
# CALLING NUMBER DELIVERY
# CALLING PARTY CATEGORY
# CALLING PLANS
# CALLBACKS
# CHARGENUMBER
# CLASSMARK
# CLONE
# COLLABORATE
# COMM PILOT CALL MANAGER
# COMM PILOT EXPRESS
# COMMON PHONE LIST
# COMMUNICATION BARRING
# COMMUNICATION BARRING USER
# CONNECTED LINE IDENTIFICATION
# CUSTOM CONTACT DIRECTORY
# DEPARTMENTS
# DEVICE POLICIES
# DEVICES
# DIAL PLAN POLICY
# DIRECTED CALL PICKUP WITH BARGE IN
# DIRECTROUTE
# DN

    def group_dns(self, service_provider_id:str, group_id:str):
        """Gets all numbers assigned to group.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where group is hosted.
            group_id (str): Group ID of target group.

        Returns:
            Dict: Dictionary containing all DNs assigned to group. 
        """

        endpoint = f"/groups/dns?serviceProviderId={service_provider_id}&groupId={group_id}"

        return self.requester.get(endpoint)
    
    
    def group_dn_search(self, service_provider_id:str, group_id:str, dn: int,
                        filter_type: str = None, limit: int = None):
        """Searches for numbers assigned to group and allows search criteria and limiting result.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where group is hosted.
            group_id (str): Group ID of target group where numbers are located.
            dn (int): Number/ part of number to search for.
            filter_type (str, optional): Options: equal to, starts with, or contains. Defaults to None.
            limit (int, optional): Limits the amount of values API returns. Defaults to None.

        Returns:
            List: List of numbers matching search criteria
        """

        endpoint = f"/groups/dns/search?&serviceProviderId={service_provider_id}&groupId={group_id}"
        
        if filter_type:
            endpoint += f"&{format_filter('dn', filter_type, dn)}"
        if limit:
            # TODO: Limit is failing when needed, odin to resolve
            endpoint += f"&limit={limit}"

        return self.requester.get(endpoint)
    
    
    def group_dn_details(self, service_provider_id:str, group_id:str):
        """Gets all numbers assigned to Group in detail. This will show where the number is assigned
        in a group such as which user or hunt group. 

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where group is hosted.
            group_id (str): Group ID of target group where numbers are located.

        Returns:
            Dict: Dictionary of numbers with details of each number.
        """
        
        endpoint = f"/groups/dns/details?serviceProviderId={service_provider_id}&groupId={group_id}"
        
        return self.requester.get(endpoint)
    
    
    def system_dn_search(self, dn: int):
        """Searches for number from System level. This will return where the number is located on the system.
        It will show the Service Provider/ Enterprise, Group ID, and User ID the number is assigned to.

        Args:
            dn (int): Target number excluding country code e.g. 123456789

        Returns:
            List: List of dictionaries containing details of each number that fit the search criteria. 
        """
        
        endpoint = f"/system/dns/search?dn=%2b{dn}"
        
        return self.requester.get(endpoint)
    
    
    def system_dn(self, dn: int):
        """Searches for number from System level. This will return where the number is located on the system.
        It will show the Service Provider/ Enterprise, Group ID, and User ID the number is assigned to.

        Args:
            dn (int): Target number excluding country code e.g. 123456789

        Returns:
            List: List of dictionaries containing details of each number that fit the search criteria. 
        """
        
        endpoint = f"/system/dns?phoneNumber={dn}"
        
        return self.requester.get(endpoint)
    
    
    def system_dn_summary(self):
        """Returns all numbers assigned to system.

        Returns:
            List: List of all Service Providers/ Enterprises and numbers assigned in ranges.
        """
        
        endpoint = f"/system/dns/summary"
        
        return self.requester.get(endpoint)
    
    
    def system_dn_utilization(self):
        """Returns DN statistics for each Service Provider/ Enterprise such as total DNs assigned.

        Returns:
            List: List of all Service Provider/ Enterprises with statistics of DNs for each.
        """
        
        endpoint = f"/system/dns/utilization"   
       
        return self.requester.get(endpoint) 
    
    
    def service_provider_dn_search(self, service_provider_id:str, dn: int,
                        filter_type: str = None, limit: int = None):
        """Searches for numbers assigned to Service Provider/ Enterprise and allows search criteria and limiting result.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where group is hosted.
            dn (int): Number/ part of number to search for.
            filter_type (str, optional): Options: equal to, starts with, or contains. Defaults to None.
            limit (int, optional): Limits the amount of values API returns. Defaults to None.

        Returns:
            List: List of numbers matching search criteria
        """

        endpoint = f"/service-providers/dns/search?&serviceProviderId={service_provider_id}"
        
        if filter_type:
            endpoint += f"&{format_filter('dn', filter_type, dn)}"
        if limit:
            # TODO: Limit is failing when needed, odin to resolve
            endpoint += f"&limit={limit}"

        return self.requester.get(endpoint)
        
    
    def service_provider_dns(self, service_provider_id: str):
        """Returns all numbers assigned to Service Provider/ Enterprise with the group its assigned to
        and if the numbers can be deleted.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where target numbers are located.

        Returns:
            Dict: All numbers assigend to Service Provider/ Enterprise with group and delete status.
        """
        
        endpoint = f"/service-providers/dns?serviceProviderId={service_provider_id}"
        
        return self.requester.get(endpoint)
        
    
# DO NOT DISTURB
# DOMAINS
# EMERGENCY NOTIFICATIONS
# EMERGENCY ZONES
# ENTERPRISE TRUNKS
# EXECUTIVE
# EXECUTIVE ASSISTANT
# EXTENSIONS
# EXTERNAL CALLING LINE ID DELIVERY
# EXTERNAL CUSTOM RINGBACK
# FAX MESSAGING
# FEATURE ACCESS CODES
# FLEXIBLE SEATING
# GROUP PAGING
# GROUPS
    
    def group(self, service_provider_id, group_id):

        endpoint = f"/groups?serviceProviderId={service_provider_id}&groupId={group_id}"

        return self.requester.get(endpoint)

# GROUP NAVIGATION
# HOTELING GUEST
# HOTELING HOST
# HUNT GROUPS

    def group_hunt_groups(self, service_provider_id, group_id):

        endpoint = f"/groups/hunt-groups?serviceProviderId={service_provider_id}&groupId={group_id}"

        return self.requester.get(endpoint)

    def group_hunt_group(self, service_user_id):

        endpoint = f"/groups/hunt-groups?serviceUserId={service_user_id}"

        return self.requester.get(endpoint)

    def group_hunt_group_user(self, service_provider_id, group_id, user_id):

        endpoint = f"/groups/hunt-groups/user?serviceProviderId={service_provider_id}&groupId={group_id}&userId={user_id}"

        return self.requester.get(endpoint)


# IN CALL SERVICE ACTIVATION
# INSTANT GROUP CALL
# INTEGRATED IMP
# INTERCEPT
# INTERNAL CALLING LINE ID DELIVERY
# LANGUAGES
# LEGACY AUTOMATIC CALLBACK
# MALICIOUS CALL TRACE
# MEDIA
# MEET-ME CONFERENCING
# MUSIC ON HOLD
# MWI DELIVERY TO MOBILE ENDPOINT
# NETWORK CLASS OF SERVICE
# NIGHT FORWARDING
# NUMBER PORTABILITY ANNOUNCEMENT
# NUMBER PORTABILITY QUERY
# NUMBERS
# OUTLOOK INTEGRATION
# PASSCODE RULES
# PASSWORD GENERATE

    def password_generate(self, service_provider_id: str, group_id: str) -> dict:
        """Generates a single passwords following the groups rules.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate password for. 

        Returns:
            dict: Single password generated according to the groups rules.
        """
        
        endpoint = f"/password/generate?serviceProviderId={service_provider_id}&groupId={group_id}"
        
        return self.requester.get(endpoint)
    
    
    def passwords_generate(self, service_provider_id: str, group_id: str, limit: int =10) -> dict:
        """Generates a multiple passwords to the limit set in pararmeters.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate password for. 
            limit (int, optional): Number of passwords api will return. Defaults to 10.

        Returns:
            dict: Multiple passwords generated according to the groups rules.
        """
                
        endpoint = f"/password/generate?serviceProviderId={service_provider_id}&groupId={group_id}&limit={limit}"
        
        return self.requester.get(endpoint)
        
    
    def passcode_generate(self, service_provider_id: str, group_id: str) -> dict:
        """Generates a single passcode following group rules.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate passcode for. 

        Returns:
            dict: Single passcode generated according to the groups rules.
        """
        
        endpoint = f"/passcode/generate?serviceProviderId={service_provider_id}&groupId={group_id}"
    
        return self.requester.get(endpoint)
    
    
    def passcodes_generate(self, service_provider_id: str, group_id: str, limit: int =10) -> dict:
        """Generates a multiple passcodes to the limit set in pararmeters.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate passcodes for. 
            limit (int, optional): Number of passwords api will return. Defaults to 10.

        Returns:
            dict: Multiple passcodes generated according to the groups rules.
        """
        
        endpoint = f"/passcode/generate?serviceProviderId={service_provider_id}&groupId={group_id}&limit={limit}"
        
        return self.requester.get(endpoint)
    
    
    def sip_password_generate(self) -> dict:
        """Generates a single SIP password.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate SIP password for. 

        Returns:
            dict: Single SIP password generated according to the groups rules.
        """
        
        endpoint = f"/sip-password/generate"
        
        return self.requester.get(endpoint)
    
    
    def sip_passwords_generate(self, limit: int =10) -> dict:
        """Generates multiple SIP passwords to the limit set in parameters. Defaults to 10.

        Args:
            limit (int, optional): Number of passwords api will return. Defaults to 10.

        Returns:
            dict: Mutliple SIP passwords generated according to the groups rules.
        """

        endpoint = f"/password/generate?limit={limit}"
        
        return self.requester.get(endpoint)

# PASSWORD RULES
# PERSONAL PHONE LIST
# PHONE DIRECTORY
# PHYSICAL LOCATION
# POLYCOM PHONE SERVICES
# PRE ALERTING
# PREFERRED CARRIER
# PREPAID
# PRIMARY ENDPOINT ADVANCED SETTING
# PRIORITY ALERT
# PRIVACY
# PUSH REGISTRATION
# PUSH TO TALK
# REGISTRATION
# REMOTE OFFICE
# REPORTS

    def user_report(self, user_id: str):
        """ Detailed report of user including services and service packs assigned.

        Args:
            user_id (str): Target user id of user.

        Returns:
            dict: Detailed report of user including services and service packs.
        """

        endpoint = f"/users/reports/users?userId={user_id}"

        return self.requester.get(endpoint)

# RESELLERS
# ROUTE LIST
# ROUTING PROFILE
# SCHEDULES
# SECURITY CLASSIFICATION
# SELECTIVE CALL ACCEPTANCE
# SELECTIVE CALL REJECTION
# SEQUENTIAL RING
# SERIES COMPLETION
# SERVICE PACKS
# SERVICE PROVIDERS
# SERVICES

    def user_services_assigned(self, user_id: str):
        """

        Args:
            user_id (str): _description_
        """
        endpoint = f"/users/services/assigned?userId={user_id}"
        
        return self.requester.get(endpoint)

    def user_services(self, user_id: str):
        """Fetch all services assigned to a broadwrok entity, this can be 
        a user, AA, CC, or HG.

        Args:
            user_id (str): User ID of the target Broadworks entity.

        Returns:
            Dict: Broadwork entiy and a list of services assigned.
        """

        endpoint = f"/users/services?userId={user_id}"

        return self.requester.get(endpoint)

    def group_services(self, group_id: str, service_provider_id: str):
        """
        Fetch all userServices, groupServices and servicePackServices assigned to a group.

        Args:
            group_id (str): GroupID of the target 
            service_provider_id (str): Service Provider or Enterprise ID of the target.

        Returns:
            Dict: Authorised and assigned services within the group.
        """

        endpoint = f"/groups/services?groupId={group_id}&serviceProviderId={service_provider_id}"

        return self.requester.get(endpoint)

    def group_services_assigned(self, group_id: str, service_provider_id: str, service_name: str, service_type: str):
        """
        Get details of the user/service instances where a particular service is assigned.

        Args:
            group_id (str): GroupID being targeted
            service_provider_id (str): Service provider/Enterprise ID where the group is located.
            service_name (str): Name of the service querying
            service_type (str): Type of service. Either: serviceName or servicePackName

        Returns:
            Dict: Users/Service Instances where the service is assigned.
        """

        endpoint = f"/groups/services/assigned?serviceProviderId={service_provider_id}&groupId={group_id}&serviceType={service_type}&serviceName={service_name}"

        return self.requester.get(endpoint)

# SHARED CALL APPEARANCE
# SILENT ALERTING
# SIMULTANEOUS RING PERSONAL
# SMARTY ADDRESS
# SPEED DIAL 100
# SPEED DIAL 8
# STATES AND PROVINCES
# SYSTEM
# TERMINATING ALTERNATE TRUNK IDENTITY
# THIRD PARTY VOICE MAIL SUPPORT
# THIRD PARTY EMERGENCY CALLING
# TIME ZONES
# TRUNK GROUPS
    
    def group_trunk_groups_call_capacity(self, service_provider_id: str, group_id: str):
        
        endpoint = f"/groups/trunk-groups/call-capacity?serviceProviderId={service_provider_id}&groupId={group_id}"
        
        return self.requester.get(endpoint)
    
    
    def group_trunk_group(self, service_provider_id: str, group_id: str, trunk_group_name: str):
        
        endpoint = f"/groups/trunk-groups?serviceProviderId={service_provider_id}&groupId={group_id}&name={trunk_group_name}"
        
        return self.requester.get(endpoint)

# TWO STAGE DIALING
# USERS

    def users(self, service_provider_id: str = None, group_id: str = None,
              filter: str = None, filter_type: str = None, filter_value: str = None,
              limit: int = None, extended=False):
        """
        Returns list of users depending on filter criteria.

        Args:
            servive_provider_id (str, optional): Service or Enterprise ID,
            top level object. Defaults to None.
            group_id (str, optional): Group ID where user is hosted. Defaults to None.
            filter (str, optional): Filter criteria, supported filters below. Defaults to None.
            filter_type (str, optional): Options: equal to, starts with, or contains. Defaults to None.
            filter_value (str, optional): Value filtering on e.g. firstName. Defaults to None.
            limit (int, optional): Limits the amount of values API returns. Defaults to None.

        Returns:
            dict: List of users.

        # Supported Filters
        macAddress: search by device
        lastName: filter by lastName
        firstName: filter by firstName
        dn: filter by dn
        emailAddress: filter by emailAddress
        userId: filter by userId
        extension: filter by extension

        #### Examples
        Get all users in Enterprise ent1
        GET /api/v2/users?serviceProviderId=ent1

        Get all users in Group grp1
        GET /api/v2/users?serviceProviderId=ent1&groupId=grp1

        Get up to 10 users in the system with a last name that contains smith
        GET /api/v2/users?lastName=*smith*&limit=10

        Get the users in grp1 that have a phone number that starts with 513333
        GET /api/v2/users?serviceProviderId=ent1&groupId=grp1&dn=513333*
        """

        endpoint = f"/users?"

        if service_provider_id:
            endpoint += f"serviceProviderId={service_provider_id}"
            if group_id:
                endpoint += f"&groupId={group_id}"
        if filter:
            if service_provider_id:
                endpoint += "&"
            endpoint += f"{format_filter(filter, filter_type, filter_value)}"
        if limit:
            # TODO: Limit is failing when needed, odin to resolve
            endpoint += f"&limit={limit}"
        if extended:
            endpoint += f"&extended=True"

        return self.requester.get(endpoint)

    def user_by_id(self, user_id: str):
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            _type_: _description_
        """

        endpoint = f"/users?userId={user_id}"

        return self.requester.get(endpoint)

# USER CUSTOM RINGBACK
# VIDEO ADD ON
# VIRTUAL ON-NET ENTERPRISE EXTENSIONS
# VOICE MESSAGING
# VOICE PORTAL CALLING
# ZONE CALLING RESTRICTIONS
# ODIN BRANDING
# ODIN CALLBACKS
# ODIN CONNECTORS
# ODIN EMAIL
# ODIN EVENTS
# ODIN INVENTORY
# ODIN REPORTS
# ODIN SETTINGS
# ODIN STATUS
# ODIN SSO
# ODIN SSO ALTERNATE USER IDS
# ODIN TASKS
# ODIN UI
# ODIN VIEWABLE PACKS
# ODIN WEBHOOKS
# ODIN AUDIT
# ODIN IMPORTS
# ODIN EXPORTS
# XSI
# SIP AUTHENTICATION
# POLICY
# PASSWORD RESET
# PARTNERS
# USER UTILITIES
# ODIN TASKS COPY
# ODIN CONNECTORS
# LOCALES
