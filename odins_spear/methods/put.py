import requests.exceptions

from odins_spear.exceptions import *

class Put():
    def __init__(self, requester):
        self.requester = requester
        
#SESSION

    def session(self):
        
        endpoint = "/auth/token"
        
        return self.requester.put(endpoint)
        
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

    def auto_attendants_status(self, auto_attendant_user_ids: list, 
                               status: bool =True):
        """Updates a list of auto attendants (AA) status to either active or inactive.

        Args:
            auto_attendant_user_ids (list): List of service user IDs (AA IDs), the status given 
            will be applied to these.
            status (bool, optional): Boolean value of True (Activate) or False (Deactivate) 
            which will be applied to list of AAs. Defaults to True.
            
        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/auto-attendants/status"
        
        data = {     
            "instances": [{'serviceUserId': auto_attendant_user_id, 'isActive': status} 
                          for auto_attendant_user_id in auto_attendant_user_ids]
        }
        
        return self.requester.put(endpoint, data=data)

        
        
    def auto_attendant(self, service_provider_id: str, group_id, 
                       auto_attendant_user_id: str, updates: dict):
        """Updates a specific Auto Attendant.
        
        Note: Needs the service instance profile to use this method.

        Args:
            service_provider_id (str): _description_
            group_id (_type_): _description_
            auto_attendant_user_id (str): _description_
            updates (dict): _description_

        Returns:
            Dict: AA updated.  
        """
        
        endpoint = f"/groups/auto-attendants"
        
        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["serviceUserId"] = auto_attendant_user_id
    
        return self.requester.put(endpoint, data=updates)
    
    
    def auto_attendant_submenu(self, auto_attendant_user_id: str, 
                               submenu_id: str, updates: dict):
        """This method allows you to update the configuration of the submenus for your AAs
        
        Args:
            auto_attendant_user_id (str): Service user ID of your auto attendant.
            submenu_id (str): Service user ID of your submenu
            updates (dict): Updates your applying to your submenu.
            
        Returns:
            None: This method does not return any specific value.
        """
        
        
        endpoint = f"/groups/auto-attendants/submenus"
        
        updates["serviceUserId"] = auto_attendant_user_id,
        updates["submenuId"] = submenu_id
        
        return self.request.put(endpoint, data=updates)
        

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

    def group_call_centers_status(self, call_center_user_ids: list, 
                                  status: bool =True):
        """Updates a list of call centers (CC) status to either active or inactive.

        Args:
            call_center_user_ids(list): List of service user IDs (CC IDs), the status given will be applied to these.
            status (bool): Boolean value of True (Activate) or False (Deactivate) which will be applied to list of AAs.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = f"/groups/call-centers/status"
        
        data = {     
            "instances": [{'serviceUserId': call_center_user_id, 'isActive': status} 
                          for call_center_user_id in call_center_user_ids]
        }
        
        return self.requester.put(endpoint, data=data)
        
        
    def group_call_center(self, call_center_user_id: str, updates: dict):
        """Allows you to update a specific call center.

        Args:
            call_center_user_id (str): Service user id of the target call center. 
            updates (dict): Updates to apply in in a dictionary format.

        Returns:
            Dict: The call center with the new applied updates.
        """
        
        endpoint = f"/groups/call-centers"
        
        updates["serviceUserId"] = call_center_user_id

        return self.requester.put(endpoint, data=updates)
    
    
    def group_call_center_agents(self, call_center_user_id: str, 
                                 agent_user_ids: list):
        """Add or remove agents to a call center. 
        
        Note: Leave the agent_user_ids blank to remove all users and to remove some only include
        the users you would like to include in this call center.
        
        Args:
            call_center_user_id (str): Service user ID of the target call center.
            agent_user_ids (list): List of user IDs to be added to call center.

        Returns:
            Dict: Dictionary of the new state of the CC.
        """
        
        endpoint = f"/groups/call-centers/agents"
        
        data = {
            "serviceUserId": call_center_user_id,
            "agents": [{"userId": agent_id} for agent_id in agent_user_ids]
        }

        return self.requester.put(endpoint, data=data)
        
    
    def group_call_center_agents_levels(self, call_center_user_id: str, 
                                        agent_user_ids: list, 
                                        skill_level: int):
        """Update a list of agents skill level in a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the call center users belong to. 
            agent_user_ids (list): List of the target users.
            skill_level (int): Skill level that will be applied to the list of users in the target call center.

        Returns:
            Dict: CC ID and list of the agent and their updated skill level.
        """
        
        endpoint = f"/groups/call-centers/agents"
        
        data = {
            "serviceUserId": call_center_user_id,
            "agents": [{"userId": agent_id, "skillLevel": skill_level} for agent_id in agent_user_ids]
        }

        return self.requester.put(endpoint, data=data) 
    
    
    def group_call_center_bounced_calls(self, call_center_user_id: str, 
                                        updates: dict):
        """Update the bounced call settings of a single Call Center (CC)

        Args:
            call_center_user_id (str): Service user ID of the target CC.   
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/call-centers/bounced-calls"
        
        updates["serviceUserId"] = call_center_user_id
        
        return self.requester.put(endpoint, data=updates) 
    
    
    def group_call_center_dnis_instance(self, call_center_user_id: str, 
                                        updates: dict):
        """Update a DNIS instance of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC. 
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/call-centers/dnis/instances"
        
        updates["serviceUserID"] = call_center_user_id

        return self.requester.put(endpoint, data=updates) 
    
    
    def group_call_center_forced_forwarding(self, call_center_user_id: str, 
                                            updates: dict):
        """Update the forced forwarding settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC. 
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/call-centers/forced-forwarding"
        
        updates["serviceUserID"] = call_center_user_id

        return self.requester.put(endpoint, data=updates) 
    

    def group_call_center_overflow(self, call_center_user_id: str, 
                                   updates: dict):
        """Update the overflow settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC. 
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/call-centers/overflow"
        
        updates["serviceUserID"] = call_center_user_id

        return self.requester.put(endpoint, data=updates) 
    

    def group_call_center_stranded_calls(self, call_center_user_id: str, 
                                         updates: dict):
        """Update the stranded calls settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC. 
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/call-centers/stranded-calls"
        
        updates["serviceUserID"] = call_center_user_id

        return self.requester.put(endpoint, data=updates) 
    

    def group_call_center_stranded_calls_unavailable(self, call_center_user_id: str, 
                                                     updates: dict):
        """Update the stranded calls unavailable settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC. 
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/call-centers/stranded-calls-unavailable"
        
        updates["serviceUserID"] = call_center_user_id

        return self.requester.put(endpoint, data=updates) 
    
    
    def user_call_center_supervised_agents(self, call_center_user_id: str, 
                                           supervisor_user_id: str, agent_ids: list):
        """Update the list of agents a supervisor has in a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC. 
            supervisor_user_id (str): User ID of the supervisor.
            agent_ids (list): List of user IDs of agents to apply to supervisor.

        Returns:
            Dict: Superivor ID and list of agents they supervise.
        """
        
        endpoint = f"/groups/call-centers/supervisors"
        
        data = {
            "serviceUserId": call_center_user_id,
            "supervisorUserId": supervisor_user_id,
            "supervisors": [{"userId": agent_id} for agent_id in agent_ids]
        }

        return self.requester.put(endpoint, data=data) 
    
    
    def user_call_center(self, user_id: str, updates: dict):
        """Update an agents status in a Call Center (CC).

        Args:
            user_id (str): User ID of the target user.
            updates (dict): Updates to be applied to the user.

        Returns:
            Dict: Agents ACD status and status in each CC they are assigned to.
        """
        
        endpoint = f"/users/call-center"
        
        updates["userId"] = user_id
           
        return self.requester.put(endpoint, data=updates)


    def user_call_center_agents_update(self, user_id: str, 
                                       call_center_service_ids: list):
        """Update the Call Centers (CC) a user is assigned to. 

        Args:
            user_id (str): User ID of the target user.
            call_center_service_ids (list): List of CC service user IDs to update the user with.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/user/call-centers/agents"
        
        data = {
            "agentUserId": user_id,
            "callCenters": [{"userId": call_center_id} for call_center_id in call_center_service_ids]
        }

        return self.requester.put(endpoint, data=data)   


    def user_call_center_agent_sign_out(self, user_id: str):
        """Sign the user out of their assigned Call Centers (CC).

        Args:
            user_id (str): User ID of the target user.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/user/call-centers/agents/sign-out"
        
        data = {
            "agentUserId": user_id,
        }

        return self.requester.put(endpoint, data=data)  
          
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


    def group_devices(self, service_provider_id: str, group_id: str, 
                      device_name: str, updates: dict):
        """Update a single device in a group. 

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """
        
        endpoint = f"/groups/devices"
        
        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["deviceName"] = device_name
        
        return self.requester.put(endpoint, data=updates)  
    
    
    def service_provider_device(self, service_provider_id: str, device_name: str, 
                                updates: dict):
        """Update a single device in a Service Provider or Enterprise.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where device is located.
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """
        
        endpoint = "/service-providers/devices"
        
        updates["serviceProviderId"] = service_provider_id
        updates["deviceName"] = device_name
        
        return self.requester.put(endpoint, data=updates)
        
    
    def system_devices(self, device_name: str, updates: dict):
        """Update a single device in the Broadworks system.

        Args:
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """
    
        endpoint = "/service-providers/devices"
        
        updates["deviceName"] = device_name
        
        return self.requester.put(endpoint, data=updates)
        
    
    def system_device_file(self, device_name: str, updates: dict):
        """Update a config file for a single device at the system level.

        Args:
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = "/system/devices/files"
        
        updates["deviceName"] = device_name
        
        return self.requester.put(endpoint, data=updates)
    
    
    def service_provider_device_file(self, device_name: str, updates: dict):
        """Update a config file for a single device at Service Provider or
        Enterprise level.

        Args:
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = "/service_provider/devices/files"

        updates["deviceName"] = device_name
        
        return self.requester.put(endpoint, data=updates)
    

    def group_device_file(self, device_name: str, updates: dict):
        """Update a config file for a single device at Group level.

        Args:
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = "/groups/devices/files"
        
        updates["deviceName"] = device_name
        
        return self.requester.put(endpoint, data=updates)
    
    
    def group_device_tags_profile(self, service_provider_id: str, group_id: str, 
                                  device_name: str, tags: list):
        """Update tags assigned to single device at group level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_name (str): Device name of the target device.
            tags (dict): List of dictionaries tag name and value entries.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """
        
        endpoint = "/groups/devices/profile"
        
        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name,
            "tags": [
                {
                    "elements": tags
                }
            ]
        }
        
        return self.requester.put(endpoint, data=data)
    
    
    def group_device_tag(self, service_provider_id: str, group_id: str, device_name: str, 
                         tag_name: str, tag_value: str):
        """Update a single tag assigned to a device at group level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_name (str): Device name of the target device.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            _type_: _description_
        """
        
        endpoint = "/groups/devices/tags"
        
        data = {
            "tagName": f"%{tag_name}%",
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name
        }     
        
        return self.requester.put(endpoint, data=data)
    
    
    def service_provider_device_tag(self, service_provider_id: str, device_name: str, 
                                    tag_name: str, tag_value: str):
        
        endpoint = "/service-providers/devices/tags"
        
        data = {
            "tagName": f"%{tag_name}%",
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "deviceName": device_name
        }     
        
        return self.requester.put(endpoint, data=data)
        
        
    def system_device_tag(self, device_name: str, tag_name: str, tag_value: str):
        
        endpoint = "/system/devices/tags"
        
        data = {
            "tagName": f"%{tag_name}%",
            "tagValue": tag_value,
            "deviceName": device_name
        }     
        
        return self.requester.put(endpoint, data=data)
    
    
    def group_device_type_file(self, service_provider_id: str, group_id: str, device_type: str, updates: dict):
    
        endpoint = "/groups/device-types/files"
        
        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["deviceType"] = device_type
        
        return self.requester.put(endpoint, data=updates)
        
    
    def group_device_type_tag(self, service_provider_id: str, group_id: str, device_type: str, tag_name: str, tag_value: str):
        
        endpoint = "/groups/system/device-types/tags"
        
        data = {
            "tagName": tag_name,
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceType": device_type
        }     
        
        return self.requester.put(endpoint, data=data)
    
    
    def service_provider_device_type_tag(self, service_provider_id: str, device_type: str, tag_name: str, tag_value: str):
        
        endpoint = "/service-providers/device-types/tags"
        
        data = {
            "tagName": tag_name,
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "deviceType": device_type
        }     
        
        return self.requester.put(endpoint, data=data)

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
    
    def group_hunt_groups_status(self, hunt_group_user_ids: list, status: bool =True):
        """Updates a list of Hunt Groups (HG) status to either active or inactive.

        Args:
            service_user_ids (list): List of service user IDs of target HGs.
            status (bool, optional): Status to apply to target HGs. Defaults to True.

        Returns:
            None: This method does not return any specific value.
        """
    
        endpoint = f"/groups/hunt-groups/status"
        
        data = {     
            "instances": [{'serviceUserId': hunt_group_user_id, 'isActive': status} 
                          for hunt_group_user_id in hunt_group_user_ids]
        }
        
        return self.requester.put(endpoint, data=data)
        
    
    def group_hunt_group(self, service_provider_id: str, group_id: str, hunt_group_user_id: str, updates: dict):
        """Update a Hunt Groups (HG) settings.

        Args:
            hunt_group_user_id (str): Service provider ID of where the group that hosts the HG is located.
            group_id (_type_): Group ID of where the HG is located.
            service_user_id (str): Target service user ID of the HG.
            updates (dict): Updates to be applied to HG.

        Returns:
            None: This method does not return any specific value.
        """
    
        endpoint = f"/groups/hunt-groups"
        
        updates["serviceProviderId"] = [service_provider_id]
        updates["groupId"] = [group_id]
        updates["serviceUserId"] = [hunt_group_user_id]
        
        return self.requester.put(endpoint, data=updates)
            
        
    def group_hunt_group_weighted_call_distribution(self, service_provider_id: str, group_id, hunt_group_user_id: str, 
                                                    agents: list):
        """Update the Weighted Call Distribution (WCD) between users in a Hunt Group (HG).

        Args:
            service_provider_id (str): Service provider ID where the group is located. 
            group_id (_type_): Group ID where the HG is located.
            hunt_group_user_id (str): Service user ID of the target HG.
            agents (list): Updates of WCD to be applied to HG.

        Raises:
            AOInvalidWeighting: The WCD must equal 100 if it does not this error will be returned.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = f"/groups/hunt-groups/weighted-call-distribution"
        
        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "serviceUserId": hunt_group_user_id,
            "agents": agents
        }
        
        max_weights = 100
        assigned_weight = 0
        
        for agent in agents:
            assigned_weight += agent["weight"]                
        if not assigned_weight == max_weights:
            raise AOInvalidWeighting
      
        return self.requester.put(endpoint, data=data)
        
        
        
        

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

    def user_services(self, user_id: str, services: list =None, service_packs: list =None, assigned: bool =True):
        """Update the services assigend to a user. NOT service/ feature packs.

        Args:
            user_id (str): User ID of the target user.
            services (list): List of services to be applied to user.
            service_packs (list): List of service packs to be applied to user.
            assigned (bool, optional): Assign (True) or unassign(False). Defaults to True.

        Returns:
            Dict: User services assigned to the user. 
        """
        
        endpoint = f"/users/services"
        
        data = {
            "userId": user_id
        }
        
        if services:
            data["userServices"] = [{'serviceName': service, 'assigned': assigned} for service in services]
        if service_packs:
            data["servicePackServices"] = [{'serviceName': service_pack, 'assigned': assigned} for service_pack in service_packs]
        
        return self.requester.put(endpoint, data=data)
    

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

    def users_bulk(self, users: list, updates: dict):
        
        endpoint = "/users/bulk"
        
        target_users = [{"userId": user} for user in users]
        
        data = {
            "users": target_users,
            "data": updates 
        }
        
        return self.requester.put(endpoint, data=data)


    def user(self, service_provider_id: str, group_id, user_id: str, updates: dict):
        
        endpoint = "/users"
        
        updates["serviceProviderId"] = [service_provider_id]
        updates["groupId"] = [group_id]
        updates["userId"] = [user_id]
        
        return self.requester.put(endpoint, data=updates)
        
    
    def user_portal_passcode(self, user_id: str, new_passcode: int):
        
        if new_passcode < 4 or new_passcode > 6:
            raise AOInvalidCode
        
        endpoint = "/users/portal-passcode"
        
        data = {
            "userId": user_id,
            "newPasscode": new_passcode
        }
        
        return self.requester.put(endpoint, data=data)
   
    
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