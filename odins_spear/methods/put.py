from ..exceptions import *


class Put():
    def __init__(self, requester):
        self.requester = requester
        
#SESSION

    def session(self):
        """ this updates session
        """
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

    def user_authentication_service(self, user_id: str, new_password: str):
        """Set new SIP Authentication password for a single user.

        Args:
            user_id (str): Target user ID to reset the SIP authentication password.
            new_password (str): New SIP authentication password to apply to new user.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = "/users/authentication"
        
        data = {
            "userId": user_id,
            "newPassword": new_password
        }
        
        return self.requester.put(endpoint, data=data)
    
    
    def user_web_authentication_password(self, user_id: str, new_password: str):
        """Set new Web Authentication password for a single user.

        Args:
            user_id (str): Target user ID to reset the web authentication password.
            new_password (str): New web authentication password to apply to new user.

        Returns:
            None: This method does not return any specific value.
        """
        
        endpoint = "/users/passwords"
        
        data = {
            "userId": user_id,
            "newPassword": new_password
        }
        
        return self.requester.put(endpoint, data=data)

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
        
        endpoint = "/groups/auto-attendants/status"
        
        data = {     
            "instances": [{'serviceUserId': auto_attendant_user_id, 'isActive': status} 
                          for auto_attendant_user_id in auto_attendant_user_ids]
        }
        
        return self.requester.put(endpoint, data=data)

    def auto_attendant(self, service_provider_id: str, group_id, auto_attendant_user_id: str, updates: dict):
        """Updates a single target Auto Attendant.
        
        Note: Needs the service instance profile to use this method.

        Args:
            service_provider_id (str): Service Provider ID where Group is hosted.
            group_id (str): Group ID where target Auto Attendant is located.
            auto_attendant_user_id (str): Target Auto Attendant User ID.
            updates (dict): Updates to be applied to Auto Attendant.

        Returns:
            Dict: Updated version of the Auto Attendant with updates applied. 
        """
        
        endpoint = "/groups/auto-attendants"
        
        if 'serviceInstanceProfile' not in updates:     
            updates.setdefault('serviceInstanceProfile', {})

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
        
        
        endpoint = "/groups/auto-attendants/submenus"
        
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

        endpoint = "/groups/call-centers/status"
        
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
        
        endpoint = "/groups/call-centers"
        
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
        
        endpoint = "/groups/call-centers/agents"
        
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
        
        endpoint = "/groups/call-centers/agents"
        
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
        
        endpoint = "/groups/call-centers/bounced-calls"
        
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
        
        endpoint = "/groups/call-centers/dnis/instances"
        
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
        
        endpoint = "/groups/call-centers/forced-forwarding"
        
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
        
        endpoint = "/groups/call-centers/overflow"
        
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
        
        endpoint = "/groups/call-centers/stranded-calls"
        
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
        
        endpoint = "/groups/call-centers/stranded-calls-unavailable"
        
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
        
        endpoint = "/groups/call-centers/supervisors"
        
        data = {
            "serviceUserId": call_center_user_id,
            "supervisorUserId": supervisor_user_id,
            "supervisors": [{"userId": agent_id} for agent_id in agent_ids]
        }

        return self.requester.put(endpoint, data=data) 
    
    
    def user_call_center(self, user_id: str, updates: dict):
        """Update an agent's status in a Call Center (CC).

        Args:
            user_id (str): User ID of the target user.
            updates (dict): Updates to be applied to the user.

        Returns:
            Dict: Agents ACD status and status in each CC they are assigned to.
        """
        
        endpoint = "/users/call-center"
        
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
        
        endpoint = "/user/call-centers/agents"
        
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
        
        endpoint = "/user/call-centers/agents/sign-out"
        
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

    def user_call_processing_policy(self, user_id: str, updates: dict):
        """
        Update the Call Processing Policies for a specified user. 

        Args:
            user_id (str): The user ID of the user whose call processing policies need updating.
            updates (dict): Updates to apply to the specified user. 
        
        Returns:
            Dict: Returns the updated call processing policies.
        """
        
        endpoint = "/users/call-processing-policy"

        updates["userId"] = user_id

        return self.requester.put(endpoint, data=updates)

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
            Dict: Python dictionary of the new state after updates have been applied.
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
        """Update a single tag assigned to a device at the Service Provider or Enterprise level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            device_name (str): Device name of the target device.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """
        
        endpoint = "/service-providers/devices/tags"
        
        data = {
            "tagName": f"%{tag_name}%",
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "deviceName": device_name
        }     
        
        return self.requester.put(endpoint, data=data)
        
        
    def system_device_tag(self, device_name: str, tag_name: str, tag_value: str):
        """Update a single tag assigned to a device at the System level.

        Args:
            device_name (str): Device name of the target device.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """
        
        endpoint = "/system/devices/tags"
        
        data = {
            "tagName": f"%{tag_name}%",
            "tagValue": tag_value,
            "deviceName": device_name
        }     
        
        return self.requester.put(endpoint, data=data)
    
    
    def group_device_type_file(self, service_provider_id: str, group_id: str, 
                               device_type: str, updates: dict):
        """Set config file for all devices of a specific type at the group level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_type (str): The device type you would like to apply the changes to.
            updates (dict): Cupdates (dict): Updates to apply to the target device.
            
        Returns:
            None: This method does not return any specific value.
        """
    
        endpoint = "/groups/device-types/files"
        
        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["deviceType"] = device_type
        
        return self.requester.put(endpoint, data=updates)
        
    
    def group_device_type_tag(self, service_provider_id: str, group_id: str, 
                              device_type: str, tag_name: str, tag_value: str):
        """Update tags applied to device types at the Group level. 
                
        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_type (str): The target device type to apply the updates.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """
        
        endpoint = "/groups/system/device-types/tags"
        
        data = {
            "tagName": tag_name,
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceType": device_type
        }     
        
        return self.requester.put(endpoint, data=data)
    
    
    def service_provider_device_type_tag(self, service_provider_id: str, device_type: str, 
                                         tag_name: str, tag_value: str):
        """Update tags applied to device types at the Service Provider or Enterprise level. 
                
        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            device_type (str): The target device type to apply the updates.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """
        
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

    def group_dns_activate(self, service_provider_id: str, group_id: str, activated: bool, 
                           numbers: list):
        """Update activation state of a list of numbers assigned to a group.

        Args:
            service_provider_id (str): Service provider ID where the group is located. 
            group_id (str): Group ID where numbers are hosted.
            activated (bool): True to activate number and False to deactivate.
            numbers (list): List of target numbers to update. These must be strings and follow correct format.

        Returns:
            JSON: All numbers assigned to group with activation state.
        """
        
        endpoint = "/groups/dns"
        
        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "dns": [{"activated": activated, "min": num, "max": None} for num in numbers]
        }
        
        return self.requester.put(endpoint, data=data)
        

#DO NOT DISTURB

    def user_do_not_disturb(self, user_id: str, dnd_active: bool = False, ring_splash_active: bool = False ):
        """Updates a user's DND and Ring Splash status.

        Args:
            user_id (str): Target user id of user you would like to update the state of. 
            dnd_active (bool): True to enable DND and False to disable DND. Defaults to False.
            ring_splash_active (bool): True to enable Ring Splash and False to disable Ring Splash. Defaults to False.

        Returns:
            Dict: New DND and Ringsplash state of the user.
        """
        
        
        data = {
            "isActive":dnd_active,
            "ringSplash":ring_splash_active,
            "userId": user_id
        }
        
        endpoint = f"/users/do-not-disturb"
        
        return self.requester.put(endpoint, data)
        
        

#DOMAINS
#EMERGENCY NOTIFICATIONS
#EMERGENCY ZONES

    def group_emergency_zones(self, service_provider_id: str, group_id: str, is_active: bool=True, zone_rules: str=None, emergency_notification_email: str=None, ip_addresses: list=None):
        """Updates the Emergency Zone configuration in the group. 
       
        Args:
            service_provider_id (str): Service provider ID where the Emergency Zone to be updated exists.
            group_id (str): Group ID where the Emergency Zone to be updated exists.
            is_active (bool, optional): Whether the Emergency Zone service is active or not. Defaults to True
            zone_rules (str, optional): The rules of the Emergency Zone. This will either be "Prohibit all registrations and call originations" or "Prohibit emergency call originations".
            emergency_notification_email (str, optional): The email address where emergency call notifications should be sent. 
            ip_addresses (list, optional): A list of IP address ranges (dicts) to be added to the Emergency Zone. If the IP address to be applied is not a range, the min and max values should be the same.
            
        Returns:
            Dict: Updated Emergency Zone configuration.
        """

        endpoint = "/groups/emergency-zones"

        data = {
            "groupId": group_id, 
            "serviceProviderId": service_provider_id
        }

        if is_active:
            data["isActive"] = is_active
        if zone_rules:
            data["emergencyZonesProhibition"] = zone_rules
        if emergency_notification_email:
            data["sendEmergencyCallNotifyEmail"] = True
            data["emergencyCallNotifyEmailAddress"] = emergency_notification_email
        if ip_addresses:
            data["ipAddresses"] = ip_addresses
        
        return self.requester.put(endpoint, data)        


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
    
    def group_hunt_groups_status(self, service_user_ids: list, status: bool =True):
        """Updates a list of Hunt Groups (HG) status to either active or inactive.

        Args:
            service_user_ids (list): List of service user IDs of target HGs.
            status (bool, optional): Status to apply to target HGs. Defaults to True.

        Returns:
            None: This method does not return any specific value.
        """
    
        endpoint = f"/groups/hunt-groups/status"
        
        data = {     
            "instances": [{'serviceUserId': service_user_id, 'isActive': status} 
                          for service_user_id in service_user_ids]
        }
        
        return self.requester.put(endpoint, data=data)
        
    
    def group_hunt_group(self, service_provider_id: str, group_id: str, service_user_id: str, updates: dict):
        """Update a Hunt Group's (HG) settings.

        Args:
            service_provider_id (str): Service provider ID of where the group that hosts the HG is located.
            group_id (str): Group ID of where the HG is located.
            service_user_id (str): Target service user ID of the HG.
            updates (dict): Updates to be applied to HG.

        Returns:
            None: This method does not return any specific value.
        """
    
        endpoint = f"/groups/hunt-groups"
        
        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["serviceUserId"] = service_user_id
        if not updates.get("serviceInstanceProfile"):
            updates["serviceInstanceProfile"] = {}          
        
        return self.requester.put(endpoint, data=updates)
            
        
    def group_hunt_group_weighted_call_distribution(self, service_provider_id: str, group_id, service_user_id: str, 
                                                    agents: list):
        """Update the Weighted Call Distribution (WCD) between users in a Hunt Group (HG).

        Args:
            service_provider_id (str): Service provider ID where the group is located. 
            group_id (_type_): Group ID where the HG is located.
            service_user_id (str): Service user ID of the target HG.
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
            "serviceUserId": service_user_id,
            "agents": agents
        }
        
        max_weights = 100
        assigned_weight = 0
        
        for agent in agents:
            assigned_weight += agent["weight"]                
        if not assigned_weight == max_weights:
            raise OSInvalidWeighting
      
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
        """Update the services assigned to a user. NOT service/feature packs.

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
    
    def user_service_settings(self, user_id: str, settings: dict):
        """Updates specific service settings for a given user.
        This function allows you to modify one or more service settings associated with a particular user.

        Args:
            user_id (str): The ID of the target user
            settings (dict): A dictionary containing the new settings to be applied. The structure of this dictionary should mirror the API's expected format for updating service settings.

        Returns:
            Dict: A dictionary representing the updated service settings for the specified user.
        """

        endpoint = f"/users/services/settings"

        data = {
            "userId": user_id,
            **settings
        }

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

    def group_trunk_groups_call_capacity(self, service_provider_id: str, group_id: str, max_active_calls: int=None,
                                         bursting_max_active_calls: int=None, number_of_bursting_btlus: int=None):
        """
        Updates the trunking call capacity in the specified group. 
        NOTE: The max available active calls cannot be changed here. Please see service_providers_trunk_group_call_capacity to update this.

        Args:
            service_provider_id (str): Service provider ID where the target group is built
            group_id (str): Group ID whose trunk group call capacity needs updating
            max_active_calls (int, optional): The max active calls for the group. 
            bursting_max_active_calls (int, optional): The bursting max active calls for the group.
            number_of_bursting_btlus (int, optional): The number of Business Trunking License Units for bursting. 

        Returns: 
            Dict: Returns the updated state of the trunk group call capacity.
        """

        endpoint = "/groups/trunk-groups/call-capacity"
        
        updates = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        if max_active_calls:
            updates["maxActiveCalls"] = max_active_calls
        if bursting_max_active_calls:
            updates["burstingMaxActiveCalls"] = bursting_max_active_calls
        if number_of_bursting_btlus:
            updates["numberOfBurstingBTLUs"] = number_of_bursting_btlus

        return self.requester.put(endpoint, data=updates)


    def group_trunk_group(self, service_provider_id: str, group_id: str, trunk_group_name: str, updates: dict):
        """
        Updates trunk group (TG) information.

        Args: 
            service_provider_id (str): Service provider ID where the target group is built
            group_id (str): Group ID whose trunk group call capacity needs updating
            trunk_group_name (str): The name of the trunk group that is being updated. 
            updates (dict): Updates to be applied to the TG. 

        Returns:
            Dict: Returns the updated Trunk Group profile.
        """

        endpoint = "/groups/trunk-groups"

        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["name"] = trunk_group_name

        return self.requester.put(endpoint, data=updates)


    def service_providers_trunk_group_call_capacity(self, service_provider_id: str, max_active_calls: int, bursting_max_active_calls: int =None):
        """
        Updates the max active calls and the bursting max active calls for the given service provider.

        Args: 
            service_provider_id (str): Service provider ID for which the max active calls needs to be updated 
            updates (dict): The updates to be applied to the service provider's trunking call capacity
        
        Returns:
            Dict: Returns the updated call capacity for the service provider. 
        """

        endpoint = "/service-providers/trunk-groups/call-capacity"
        
        data = {
            "maxActiveCalls": max_active_calls,
            "serviceProviderId": service_provider_id
        }
        
        if bursting_max_active_calls:
            data["burstingMaxActiveCalls"] = bursting_max_active_calls

        return self.requester.put(endpoint, data=data)

#TWO STAGE DIALING
#USERS

    def users_bulk(self, users: list, updates: dict):
        """
        Updates specified list of User's options, such as extension, name and etc.

        Note: Available options to change can be seen through: get.user_by_id()

        Args: 
            users (list): List of specified User IDs to update
            updates (dict): The updates to be applied to the list of Users e.g {"extension":"9999"}
        
        Returns:
            Dict: Returns the changes made including the list of User IDs and updates.
        """
        endpoint = "/users/bulk"
        
        target_users = [{"userId": user} for user in users]
        
        data = {
            "users": target_users,
            "data": updates 
        }
        
        return self.requester.put(endpoint, data=data)


    def user(self, service_provider_id: str, group_id: str, user_id: str, updates: dict):
        """
        Updates specified User's options, such as extension, name and etc.

        Note: Available options to change can be seen through: get.user_by_id()

        Args: 
            service_provider_id (str): 
            updates (dict): The updates to be applied Target Service Provider where group is located
            group_id (str): Target Group ID where user is located
            user_id (str): Target User IDto the list of Users e.g {"extension":"9999"}
        
        Returns:
            Dict: Returns the changes made including User ID and updates.
        """
        endpoint = "/users"
        
        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["userId"] = user_id
        
        return self.requester.put(endpoint, data=updates)
        
    
    def user_portal_passcode(self, user_id: str, new_passcode: str):
        """Updates the specified User's portal passcode.

        Args:
            user_id (str): User ID of the target user you would like to change the portal passcode for. 
            new_passcode (int): New portal passcode to set for the target user.

        Raises:
            AOInvalidCode: If code is less than 4 or higher than 6.

        Returns:
            None: This method does not return any specific value.
        """
        
        if len(new_passcode) < 4 or len(new_passcode) > 6:
            raise OSInvalidCode
        
        endpoint = "/users/portal-passcode"
        
        data = {
            "userId": user_id,
            "newPasscode": new_passcode
        }
        
        return self.requester.put(endpoint, data=data)

    def user_id(self, user_id: str, new_id: str):
        """
        Updates A Specified Users User Identifier

        Args:
            user_id (str): Users Original Identifier
            new_id (str): New User Identifier

        Returns:
            None: No Specified Return Type
        """
        endpoint = "/users/user-id"
        
        data = {
            "userId": user_id,
            "newUserId": new_id
        }
        
        return self.requester.put(endpoint, data=data)

    def user_group_id_update(
        self,
        user_id: str,
        new_group_id: str,
        evaluate_only: bool = False
    ):
        """
        Update The Group ID Associated With A User

        Args:
            user_id (str): Users Identifier
            new_group_id (str): New Group Identifier
            evaluate_only (bool): Evaluates Whether The Change Is Possible

        Returns:
            None: No Specified Return Type
        """
        
        endpoint = "/users/group-id"

        data = {
            "userId": user_id,
            "newGroupId": new_group_id,
            "evaluateOnly": evaluate_only
        }

        return self.requester.put(endpoint, data=data)
    
    def user_login_info(
        self,
        user_id: str,
        new_user_id: str
    ):
        """
        Gets The Specified Users Login Information

        Args:
            user_id (str): Users Original Identifier
            new_id (str): New User Identifier

        Returns:
            Json: A Stub Of The Users Login Information
        """
        
        endpoint = "/users/login?userId=" + user_id

        data = {
            "userId": user_id,
            "newUserId": new_user_id
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
