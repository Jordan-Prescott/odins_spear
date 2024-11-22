class Delete():
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

    def auto_attendant(self, service_user_id: str):
        """Removes an Auto Attendant (AA) from a group. 

        Args:
            service_user_id(str): The service user ID of the AA.

        Returns:
            Dict: Returns the profile of the deleted AA.
        """

        endpoint = "/groups/auto-attendants"

        params = {
            "serviceUserId": service_user_id
        }

        return self.requester.delete(endpoint, params=params)


    def auto_attendant_submenu(self, service_user_id: str, submenu_id: str):
        """Removes an Auto Attendant (AA) Submenu from the AA configuration. Submenus are only a feature of the 'Auto Attendant - Standard' service. These are not available on Basic AAs.

        Args:
            service_user_id(str): The service user ID of the AA.
            submenu_id (str): The ID of the Submenu to be removed from the AA. 

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/auto-attendants/submenus"

        params = {
            "serviceUserId": service_user_id, 
            "submenuId": submenu_id
        }

        return self.requester.delete(endpoint, params=params)

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

    def group_dns(self, service_provider_id: str, group_id: str, 
                  start_of_range_number: str, end_of_range_number: str):
        """Removes range of numbers from a Group. 

        Args:
            service_provider_id (str): Service provider ID where the group is located. 
            group_id (str): Group ID where numbers are hosted.
            start_of_range_number (str): Starting number in range to remove from group. 
            end_of_range_number (str): Ending number in range to remove from group.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = "/groups/dns"
        
        data = {
			"serviceProviderId": service_provider_id,
			"groupId": group_id,
			"dns": [
                {
                    "min": start_of_range_number,
                    "max": end_of_range_number,
                }
            ]
		}
        
        return self.requester.delete(endpoint, data=data)
    
    
    def service_provider_dns(self, service_provider_id: str, start_of_range_number: str, end_of_range_number: str):
        """Removes range of numbers from a Service Proiver or Enterprise. 

        Args:
            service_provider_id (str): Service provider ID where target numbers are located. 
            start_of_range_number (str): Starting number in range to remove from service provider. 
            end_of_range_number (str): Ending number in range to remove from service provider.

        Returns:
            None: This method does not return any specific value.
        """
        endpoint = "/service-providers/dns"
        
        data = {
			"serviceProviderId": service_provider_id,
			"dns": [
                {
                    "min": start_of_range_number,
                    "max": end_of_range_number
                }
            ]
		}
        
        return self.requester.delete(endpoint, data=data)

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

    def group_hunt_group(self, service_user_id: str):

        """Deletes the specified hunt group.

        Args:
            service_user_id (str): The service user ID of the hunt group to be deleted.

        Returns:
            Dict: Profile of the deleted hunt group.

        """

        endpoint = "/groups/hunt-groups"

        params = {
            "serviceUserId": service_user_id
        }

        return self.requester.delete(endpoint, params=params)


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

    def user(self, user_id: str):

        """Deletes the specified User

        Args:
            user_id (str): The target user ID to be deleted.

        Returns:
            Nothing

        """

        endpoint = "/users"

        params = {
            "userId": user_id
        }

        return self.requester.delete(endpoint, params=params)
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

