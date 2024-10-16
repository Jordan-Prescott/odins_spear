

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

    def group_admin(self, service_provider_id: str, group_id: str, user_id: str, password: str, payload: dict = {}):
        """Builds a group-level administrator.

        Args:
            service_provider_id (str): Service provider ID where the admin should be built.
            group_id (str): Group ID where the admin should be built
            user_id (str): User ID of the admin. 
            password (str): Password for the administrator profile. Note get.password_generate() can be used to get this.
            payload (dict, optional): Admin configuration data. 
        
        Returns:
            Dict: Returns the admin profile. 
        """

        endpoint = "/groups/admins"

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["userId"] = user_id
        payload["password"] = password

        return self.requester.post(endpoint, data=payload)


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

    def group_device(self, service_provider_id: str, group_id: str, device_name: str, device_type: str, payload: dict ={}):
        """Adds a new device to a group. 

        Args:
            service_provider_id (str): Service provider ID where the device should be built.
            group_id (str): Group ID where the device should be built
            device_name (str): Name of the new device
            device_type (str): Type of device. 
            payload (dict, optional): Device configuration data. 
        
        Returns:
            Dict: Returns the device profile. 
        """
        
        endpoint = "/groups/devices"

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["deviceName"] = device_name
        payload["deviceType"] = device_type

        return self.requester.post(endpoint, data=payload)

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
        
        endpoint = "/groups/dns"
        
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
        
        endpoint = "/groups/dns/assign/bulk"
        
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
        
        endpoint = "/groups/dns/unassign/bulk"
        
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
        
        endpoint = "/groups/dns"
        
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

    def group_emergency_zones(self, service_provider_id: str, group_id: str, ip_addresses: list):
        """Updates the IP address(es) for the Emergency Zone configured in the group. 
       
        Args:
            service_provider_id (str): Service provider ID where the Emergency Zone to be updated exists.
            group_id (str): Group ID where the Emergency Zone to be updated exists.
            ip_addresses (list): A list of IP address ranges (dicts) to be added to the Emergency Zone. If the IP address to be applied is not a range, the min and max values should be the same.
            
        Returns:
            Dict: Emergency Zone profile with updated IP addresses.
        """

        endpoint = "/groups/emergency-zones"

        data = {
            "serviceProviderId": service_provider_id, 
            "groupId": group_id, 
            "ipAddresses": ip_addresses
        }

        return self.requester.post(endpoint, data=data)


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

    def group_hunt_group(self, service_provider_id: str, group_id: str, service_user_id: str, 
                         clid_first_name: str, clid_last_name:str, extension: str,  payload: dict={}, agents: list=[],
                         policy: str ="Regular", no_answer_number_of_rings: int=5, forward_timeout_seconds: int=0):
        """
        Builds a hunt group (HG) in the specified group. 

        Args:
            service_provider_id (str): The service provider ID in which the target group is built.
            group_id (str): The group ID where the HG should be built.
            service_user_id (str): The service user ID for the new HG. This must include the domain of the user.
            clid_first_name (str): The Calling Line ID first name.
            clid_last_name (str): The Calling Line ID last name. 
            extension (str): The extension number for the HG. This must be entered as a string. 
            payload (dict, optional): HG configuration data. 
            agents (list, optional): List of user IDs (str) that should be assigned to the new HG. The user(s) must already exist in the group. 
            policy (str, optional): Regular, Circular, Simultaneous, Uniform, Weighted. Defaults to Regular.
            no_answer_number_of_rings (int, optional): Defaults to 5.
            forward_timeout_seconds (int, optional): Defaults to 0.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/hunt-groups"

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id 
        payload["serviceUserId"] = service_user_id
        payload["policy"] = policy
        payload["noAnswerNumberOfRings"] = no_answer_number_of_rings
        payload["forwardTimeoutSeconds"] = forward_timeout_seconds
        
        if agents:
            payload["agents"] = [{"userId": agent} for agent in agents]

        if 'serviceInstanceProfile' not in payload:     
            payload.setdefault('serviceInstanceProfile', {})            

        payload["serviceInstanceProfile"]["callingLineIdFirstName"] = clid_first_name
        payload["serviceInstanceProfile"]["callingLineIdLastName"] = clid_last_name
        payload["serviceInstanceProfile"]["name"] = f"{clid_first_name} {clid_last_name}"
        payload["serviceInstanceProfile"]["extension"] = extension

        return self.requester.post(endpoint, data=payload)
    

    def group_hunt_groups_remove_user(self, service_provider_id: str, group_id: str, user_id: str):

        """Removes the specified user from all hunt groups in which it currently exists. 

        Args:
            service_provider_id (str): The service provider ID in which the target user exists.
            group_id (str): The group ID where the user exists.
            user_id (str): The User ID of the user that is to be removed from the hunt group(s).

        Returns:
            List: Service user ID's (str) of the hunt groups from which the specified user has been removed. 
        """

        endpoint = "/groups/hunt-groups/removeUser"

        data = {
            "serviceProviderId": service_provider_id, 
            "groupId": group_id,
            "userId": user_id
        }

        return self.requester.post(endpoint, data=data)

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

    def user_shared_call_appearance_endpoint(self, user_id: str, line_port: str, device_name):
        """Creates a new Shared Call Apprance (SCA) on a single user.

        Args:
            user_id (str): Target user id of user to create SCA on.
            line_port (str): Line port to be assigned to the new SCA.
            device_name (_type_): Device to add for SCA from available devices.

        Returns:
            dict: New SCA details applied to user. 
        """
        
        endpoint = "/users/shared-call-appearance/endpoints"
        
        data = {
            "userId":user_id,
            "linePort":line_port,
            "isActive":True,
            "allowOrigination":True,
            "allowTermination":True,
            "deviceName":device_name,
            "deviceLevel":"Group"
        }
        
        return self.requester.post(endpoint, data=data)

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

    def group_trunk_group(self, service_provider_id: str, group_id: str, trunk_name: str, max_active_calls: int, payload: dict={}, 
                          sip_authentication_username: str="", sip_authentication_password: str=""):
        """
        Builds a Trunk Group (TG) in the specified group. 

        Args:
            service_provider_id (str): The service provider ID in which the target group is built.
            group_id (str): The group ID where the HG should be built.
            trunk_name (str): The name of the new TG.
            max_active_calls (str): The maximum active calls to be set on the TG.
            payload (dict, optional): Configuration for the TG.
            sip_authentication_username (str, optional): The SIP authentication username for the TG. This field is required if "requireAuthentication" is set to "true". 
            sip_authentication_password (str, optional): The SIP authentication password for the TG. You can generate a password for this using get.sip_password_generator. This field is required if "requireAuthentication" is set to "true". 

        Note:
            Several fields are set to have default values. Please refer to the online documentation. 

        Returns:
            Dict: Returns the Trunk Group profile. 
        """

        endpoint = "/groups/trunk-groups"

        payload["name"] = trunk_name
        payload["maxActiveCalls"] = max_active_calls
        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id

        default_payload_values = {
            "capacityExceededTrapInitialCalls": 0, 
            "capacityExceededTrapOffsetCalls": 0,
            "clidSourceForScreenedCallsPolicy": "Profile Name Profile Number",
            "continuousOptionsSendingIntervalSeconds": 30,
            "failureOptionsSendingIntervalSeconds": 10,
            "failureThresholdCounter": 1,
            "invitationTimeout": 6,
            "inviteFailureThresholdCounter": 1,
            "inviteFailureThresholdWindowSeconds": 30,
            "pilotUserCallOptimizationPolicy": "Optimize For User Services",
            "pilotUserCallingLineAssertedIdentityPolicy": "Unscreened Originating Calls",
            "pilotUserCallingLineIdentityForEmergencyCallsPolicy": "No Calls",
            "pilotUserCallingLineIdentityForExternalCallsPolicy": "No Calls",
            "pilotUserChargeNumberPolicy": "No Calls",
            "successThresholdCounter": 1,
            "useSystemUserLookupPolicy": "true",
            "userLookupPolicy": "Basic",
            "requireAuthentication": "false"
            }
        for key, default_value in default_payload_values.items():
            payload.setdefault(key, default_value)

        if payload["requireAuthentication"] == "true":
            payload["sipAuthenticationUserName"] = sip_authentication_username
            payload["sipAuthenticationPassword"] = sip_authentication_password

        return self.requester.post(endpoint, data=payload)

#TWO STAGE DIALING
#USERS
        
    def user(self, service_provider_id: str, group_id: str, user_id: str, first_name: str, last_name: str, 
             extension: str, web_auth_password: str, payload: dict={}):
        """
            Creates a new user in the specified group with the configuration defined in the payload.

        Args:
            service_provider_id (str): Service provider ID where Group is loctaed.
            group_id (str): Group ID where new user will be built.
            user_id (str): Complete User ID including group domain of new user.
            first_name (str): First name of new user.
            last_name (str): Last name of new user.
            extension (str): Extension number of new user.
            web_auth_password (str): Web authentication password. Note get.password_generate() can be used to get this.
            payload (dict, optional): User configuration.

        Returns:
            Dict: New user entity.
        """
        
        endpoint = "/users"
        
        payload["callingLineIdFirstName"] = first_name if not payload.get("callingLineIdFirstName") else payload["callingLineIdFirstName"]
        payload["callingLineIdLastName"] = last_name if not payload.get("callingLineIdLastName") else payload["callingLineIdLastName"]

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["userId"] = user_id
        payload["firstName"] = first_name
        payload["lastName"] = last_name
        payload["extension"] = extension
        payload["password"] = web_auth_password   
        
        return self.requester.post(endpoint, data=payload)
    
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
