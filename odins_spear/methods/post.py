

class Post():
    
    def __init__(self, requester):
        self.requester = requester
            
#SESSION
        
    def session(self, username, password):
        
        endpoint = "/auth/token"
        
        data={
            "username": username,
            "password": password
        }
        
        return self.requester.post(endpoint, data=data)
        
    def session_switch(self, username: str):
        
        endpoint = "/auth/switch-user"
        
        data = {
            "username": username
        }
        
        return self.requester.post(endpoint, data=data)
        

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

    def group_device(self, service_provider_id: str, group_id: str, device_name: str, device_type: str):

        """Adds a new device to a group. 

        Args:
            service_provider_id (str): Service provider ID where the device should be built.
            group_id (str): Group ID where the device should be built
            device_name (str): Name of the new device
            device_type (str): Type of device. 
        
        Returns:
            JSON data with the details of the newly created device. 
        """
        
        
        endpoint = "/groups/devices"

        data = {
            "serviceProviderId": service_provider_id, 
            "groupId": group_id, 
            "deviceName": device_name, 
            "deviceType": device_type
        }

        return self.requester.post(endpoint, data=data)

#DIAL PLAN POLICY
#DIRECTED CALL PICKUP WITH BARGE IN
#DIRECTROUTE
#DN

    def group_dns(self, service_provider_id: str, group_id: str, 
                  start_of_range_number: str, end_of_range_number: str):
        """Adds a range of numbers to a Group. Range of numbers must be complete and 
        format of number must follow: +{country code}-{number}.
        
        Adding a singular number - Set both the start and end of range parameters as the same number.
       
        Args:
            service_provider_id (str): Service provider ID where the target group is located. 
            group_id (str): Group ID where numbers should be added to.
            start_of_range_number (str): Starting number in range to add to group. 
            end_of_range_number (str): Ending number in range to add to group. 
            
        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/dns"
        
        data = {
			"serviceProviderId": service_provider_id,
            "groupId": group_id,
			"dns": [
                {
                    "min": start_of_range_number,
                    "max": end_of_range_number
                }
            ]
		}
        
        return self.requester.post(endpoint, data=data)
    
    
    def group_dns_assign_bulk(self, service_provider_id: str, group_id: str, 
                              start_of_range_number: int, end_of_range_number: int):
        """Adds a range of numbers to a Group. Range of numbers must be complete and 
        format of number must follow: +{country code}-{number}.
        
        Adding a singular number - Set both the start and end of range parameters as the same number.
       
        Args:
            service_provider_id (str): Service provider ID where the target group is located. 
            group_id (str): Group ID where numbers should be added to.
            start_of_range_number (str): Starting number in range to add to group. 
            end_of_range_number (str): Ending number in range to add to group. 
            
        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/dns/assign/bulk"
        
        data = {
			"serviceProviderId": service_provider_id,
            "groupId": group_id,
			"dns": [
                {
                    "min": start_of_range_number,
                    "max": end_of_range_number
                }
            ]
		}
        
        return self.requester.post(endpoint, data=data)
    
    
    def group_dns_unassign_bulk(self, service_provider_id: str, group_id: str, 
                                start_of_range_number: int, end_of_range_number: int):
        """Unassign a range of numbers from a Group. Range of numbers must be complete and 
        format of number must follow: +{country code}-{number}.
        
        Unassigning a singular number - Set both the start and end of range parameters as the same number.
       
        Args:
            service_provider_id (str): Service provider ID where the target group is located. 
            group_id (str): Group ID where numbers where numbers are located.
            start_of_range_number (str): Starting number in range to unassign in group. 
            end_of_range_number (str): Ending number in range to unassign in group.
            
        Returns:
            None: This method does not return any specific value. 
        """
        
        endpoint = f"/groups/dns/unassign/bulk"
        
        data = {
			"serviceProviderId": service_provider_id,
            "groupId": group_id,
			"dns": [
                {
                    "min": start_of_range_number,
                    "max": end_of_range_number
                }
            ]
		}
        
        return self.requester.post(endpoint, data=data)
    
    
    def service_provider_dns(self, service_provider_id: str, start_of_range_number: int, 
                             end_of_range_number: int):
        """Adds a range of numbers to a Service Provider/ Enterprise. Range of numbers must be complete and 
        format of number must follow: +{country code}-{number}.
        
        Adding a singular number - Set both the start and end of range parameters as the same number.
       
        Args:
            service_provider_id (str): Service provider ID where the target group is located. 
            start_of_range_number (str): Starting number in range to add to group. 
            end_of_range_number (str): Ending number in range to add to group. 
            
        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/dns"
        
        data = {
			"serviceProviderId": service_provider_id,
			"dns": [
                {
                    "min": start_of_range_number,
                    "max": end_of_range_number
                }
            ]
		}
        
        return self.requester.post(endpoint, data=data)


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
        
    def user(self, user):
        """_summary_

        Args:
            user (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        endpoint = "users"
        
        return self.requester.post(endpoint, data=user)
    
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