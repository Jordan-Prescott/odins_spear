from odin_api.utils import format_filter

class Get():
    
    filters = [
    "macAddress", "lastName", "firstName", "dn",
    "emailAddress", "userId", "extension"
    ]
    
    def __init__(self, requester):
        self.requester = requester
        
#SESSION
#ACCOUNT AUTHORIZATION CODES
#ADMINISTRATORS
#ADVICE OF CHARGE
#ALTERNATE NUMBERS
#ANSWER CONFIRMATION
#ALTERNATE USER ID
#ANNOUNCEMENTS
#ANONYMOUS CALL REJECTION
#ATTENDANT CONSOLE
#AUTHENTICATION
#AUTO ATTENDANTS

    def auto_attendants(self, service_provider_id, group_id):

        endpoint = f"/groups/auto-attendants?serviceProviderId={service_provider_id}&groupId={group_id}"
        
        return self.requester.get(endpoint)
    
    def auto_attendant(self, service_user_id):

        endpoint = f"/groups/auto-attendants?serviceUserId={service_user_id}"
        
        return self.requester.get(endpoint)
    
#AUTOMATIC CALLBACK
#AUTOMATIC HOLD RETRIEVE
#BARGE IN EXEMPT
#BASIC CALL LOGS
#BROADWORKS ANYWHERE
#BROADWORKS MOBILITY
#BROADWORKS NAVIGATION
#BROADWORKS RECEPTIONIST ENTERPRISE
#BROADWORKS RECEPTIONIST OFFICE
#BROADWORKS RECEPTIONIST SMALL BUSINESS
#BUSY LAMP FIELD
#CALL CAPACITY
#CALL CENTER

    def group_call_centers(self, service_provider_id, group_id):

        endpoint = f"/groups/call-centers?serviceProviderId={service_provider_id}&groupId={group_id}"
        
        return self.requester.get(endpoint)

    def group_call_center(self, service_user_id):

        endpoint = f"/groups/call-centers?serviceUserId={service_user_id}"
        
        return self.requester.get(endpoint)
    
#CALL CONTROL
#CALL FORWARDING ALWAYS
#CALL FORWARDING ALWAYS SECONDARY
#CALL FORWARDING BUSY
#CALL FORWARDING NO ANSWER
#CALL FORWARDING NOT REACHABLE
#CALL FORWARDING SELECTIVE
#CALL FORWARDING SETTINGS
#CALL NOTIFY
#CALL PARK
#CALL PICKUP
#CALL POLICIES
#CALL PROCESSING POLICIES
#CALL RECORDING
#CALL RECORDS
#CALL TRANSFER
#CALL WAITING
#CALLING LINE ID BLOCKING OVERRIDE
#CALLING LINE ID DELIVERY BLOCKING
#CALLING NAME DELIVERY
#CALLING NAME RETRIEVAL
#CALLING NUMBER DELIVERY
#CALLING PARTY CATEGORY
#CALLING PLANS
#CALLBACKS
#CHARGENUMBER
#CLASSMARK
#CLONE
#COLLABORATE
#COMM PILOT CALL MANAGER
#COMM PILOT EXPRESS
#COMMON PHONE LIST
#COMMUNICATION BARRING
#COMMUNICATION BARRING USER
#CONNECTED LINE IDENTIFICATION
#CUSTOM CONTACT DIRECTORY
#DEPARTMENTS
#DEVICE POLICIES
#DEVICES
#DIAL PLAN POLICY
#DIRECTED CALL PICKUP WITH BARGE IN
#DIRECTROUTE
#DN
#DO NOT DISTURB
#DOMAINS
#EMERGENCY NOTIFICATIONS
#EMERGENCY ZONES
#ENTERPRISE TRUNKS
#EXECUTIVE
#EXECUTIVE ASSISTANT
#EXTENSIONS
#EXTERNAL CALLING LINE ID DELIVERY
#EXTERNAL CUSTOM RINGBACK
#FAX MESSAGING
#FEATURE ACCESS CODES
#FLEXIBLE SEATING
#GROUP PAGING
#GROUPS
#GROUP NAVIGATION
#HOTELING GUEST
#HOTELING HOST
#HUNT GROUPS

    def group_hunt_groups(self, service_provider_id, group_id):
    
        endpoint = f"/groups/hunt-groups?serviceProviderId={service_provider_id}&groupId={group_id}"
            
        return self.requester.get(endpoint)


    def group_hunt_group(self, service_user_id):
    
        endpoint = f"/groups/hunt-groups?serviceUserId={service_user_id}"
            
        return self.requester.get(endpoint)

#IN CALL SERVICE ACTIVATION
#INSTANT GROUP CALL
#INTEGRATED IMP
#INTERCEPT
#INTERNAL CALLING LINE ID DELIVERY
#LANGUAGES
#LEGACY AUTOMATIC CALLBACK
#MALICIOUS CALL TRACE
#MEDIA
#MEET-ME CONFERENCING
#MUSIC ON HOLD
#MWI DELIVERY TO MOBILE ENDPOINT
#NETWORK CLASS OF SERVICE
#NIGHT FORWARDING
#NUMBER PORTABILITY ANNOUNCEMENT
#NUMBER PORTABILITY QUERY
#NUMBERS
#OUTLOOK INTEGRATION
#PASSCODE RULES
#PASSWORD GENERATE
#PASSWORD RULES
#PERSONAL PHONE LIST
#PHONE DIRECTORY
#PHYSICAL LOCATION
#POLYCOM PHONE SERVICES
#PRE ALERTING
#PREFERRED CARRIER
#PREPAID
#PRIMARY ENDPOINT ADVANCED SETTING
#PRIORITY ALERT
#PRIVACY
#PUSH REGISTRATION
#PUSH TO TALK
#REGISTRATION
#REMOTE OFFICE
#REPORTS

    def user_report(self, user_id):
        """ Detailed report of user including services and service packs assigned.

        Args:
            user_id (str): Target user id of user.

        Returns:
            dict: Detailed report of user including services and service packs.
        """
        
        endpoint = f"/users/reports/users?userId={user_id}"
        
        return self.requester.get(endpoint)

#RESELLERS
#ROUTE LIST
#ROUTING PROFILE
#SCHEDULES
#SECURITY CLASSIFICATION
#SELECTIVE CALL ACCEPTANCE
#SELECTIVE CALL REJECTION
#SEQUENTIAL RING
#SERIES COMPLETION
#SERVICE PACKS
#SERVICE PROVIDERS
#SERVICES
#SHARED CALL APPEARANCE
#SILENT ALERTING
#SIMULTANEOUS RING PERSONAL
#SMARTY ADDRESS
#SPEED DIAL 100
#SPEED DIAL 8
#STATES AND PROVINCES
#SYSTEM
#TERMINATING ALTERNATE TRUNK IDENTITY
#THIRD PARTY VOICE MAIL SUPPORT
#THIRD PARTY EMERGENCY CALLING
#TIME ZONES
#TRUNK GROUPS
#TWO STAGE DIALING
#USERS
    
    def users(self, servive_provider_id: str =None, group_id: str =None, 
                  filter: str =None, filter_type: str =None, filter_value: str =None,
                  limit: int =None, extended =False):
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
            
        #### Supported Filters
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

        if servive_provider_id:
            endpoint += f"serviceProviderId={servive_provider_id}"
            if group_id:
                endpoint += f"&groupId={group_id}"
        if filter:       
            if servive_provider_id:
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

#USER CUSTOM RINGBACK
#VIDEO ADD ON
#VIRTUAL ON-NET ENTERPRISE EXTENSIONS
#VOICE MESSAGING
#VOICE PORTAL CALLING
#ZONE CALLING RESTRICTIONS
#ODIN BRANDING
#ODIN CALLBACKS
#ODIN CONNECTORS
#ODIN EMAIL
#ODIN EVENTS
#ODIN INVENTORY
#ODIN REPORTS
#ODIN SETTINGS
#ODIN STATUS
#ODIN SSO
#ODIN SSO ALTERNATE USER IDS
#ODIN TASKS
#ODIN UI
#ODIN VIEWABLE PACKS
#ODIN WEBHOOKS
#ODIN AUDIT
#ODIN IMPORTS
#ODIN EXPORTS
#XSI
#SIP AUTHENTICATION
#POLICY
#PASSWORD RESET
#PARTNERS
#USER UTILITIES
#ODIN TASKS COPY
#ODIN CONNECTORS
#LOCALES