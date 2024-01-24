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

    def auto_attendants_status(self, auto_attendant_user_ids: list, status: bool =True):
        
        endpoint = f"/groups/auto-attendants/status"
        
        data = {     
            "instances": [{'serviceUserId': auto_attendant_user_id, 'isActive': status} 
                          for auto_attendant_user_id in auto_attendant_user_ids]
        }
        
        self.requester.put(endpoint, data=data)
        
        
    def auto_attendant(self, service_provider_id: str, group_id, auto_attendant_user_id: str, updates: dict):
        
        endpoint = f"/groups/auto-attendants"
        
        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["serviceUserId"] = auto_attendant_user_id
    
        return self.requester.put(endpoint, data=updates)
    
    
    def auto_attendant_submenu(self, auto_attendant_user_id: str, submenu_id: str, updates: dict):
        
        endpoint = f"/groups/auto-attendants/submenus"
        
        updates["serviceUserId"] = auto_attendant_user_id,
        updates["submenuId"] = submenu_id
        
        self.request.put(endpoint, data=updates)
        

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

    def group_call_centers_status(self, call_center_user_ids: list, status: bool =True):
        
        endpoint = f"/groups/call-centers/status"
        
        data = {     
            "instances": [{'serviceUserId': call_center_user_id, 'isActive': status} 
                          for call_center_user_id in call_center_user_ids]
        }
        
        self.requester.put(endpoint, data=data)
        
        
    def group_call_center(self, call_center_user_id: str, updates: dict):
        
        endpoint = f"/groups/call-centers"
        
        updates["serviceUserId"] = call_center_user_id

        return self.requester.put(endpoint, data=updates)
    
    
    def group_call_center_agents(self, call_center_user_id: str, agent_user_ids: list):
        
        endpoint = f"/groups/call-centers/agents"
        
        data = {
            "serviceUserId": call_center_user_id,
            "agents": [{"userId": agent_id} for agent_id in agent_user_ids]
        }

        return self.requester.put(endpoint, data=data)
        
    
    def group_call_center_agents_levels(self, call_center_user_id: str, agent_user_ids: list, 
                                        skill_level: int):
        
        endpoint = f"/groups/call-centers/agents"
        
        data = {
            "serviceUserId": call_center_user_id,
            "agents": [{"userId": agent_id, "skillLevel": skill_level} for agent_id in agent_user_ids]
        }

        return self.requester.put(endpoint, data=data) 
    
    
    def group_call_center_bounced_calls(self, call_center_user_id: str, updates: dict):
        
        endpoint = f"/groups/call-centers/bounced-calls"
        
        updates["serviceUserId"]: call_center_user_id
        
        return self.requester.put(endpoint, data=updates) 
    
    
    def group_call_center_dnis_instance(self, call_center_user_id: str, updates: dict):
        
        endpoint = f"/groups/call-centers/dnis/instances"
        
        updates["serviceUserID"] = call_center_user_id

        return self.requester.put(endpoint, data=updates) 
    
    
    def group_call_center_forced_forwarding(self, call_center_user_id: str, updates: dict):
        
        endpoint = f"/groups/call-centers/forced-forwarding"
        
        updates["serviceUserID"] = call_center_user_id

        return self.requester.put(endpoint, data=updates) 


    def group_call_center_forced_forwarding(self, call_center_user_id: str, updates: dict):
        
        endpoint = f"/groups/call-centers/stranded-calls"
        
        updates["serviceUserID"] = call_center_user_id

        return self.requester.put(endpoint, data=updates) 
    

    def group_call_center_forced_forwarding(self, call_center_user_id: str, updates: dict):
        
        endpoint = f"/groups/call-centers/stranded-calls-unavailable"
        
        updates["serviceUserID"] = call_center_user_id

        return self.requester.put(endpoint, data=updates) 
    
    
    def group_call_center_forced_forwarding(self, call_center_user_id: str, supervisor_ids: list):
        
        endpoint = f"/groups/call-centers/supervisors"
        
        data = {
            "serviceUserId": call_center_user_id,
            "supervisors": [{"userId": supervisor_id} for supervisor_id in supervisor_ids]
        }

        return self.requester.put(endpoint, data=data) 
    
    
    def user_call_center(self, user_id: str, updates: dict):
        """
        available in this means joined in the call center object
    
            {
                "serviceUserId":"testing_test@testlab.ev.com",
                "available":true,
                "skillLevel":10
            }
        """
        
        endpoint = f"/users/call-center"
        
        updates["userId"] = user_id
           
        return self.requester.put(endpoint, data=updates)


    def user_call_center_agents_update(self, user_id: str, call_center_service_ids: list):
        
        endpoint = f"/user/call-centers/agents"
        
        data = {
            "agentUserId": user_id,
            "callCenters": [{"userId": call_center_id} for call_center_id in call_center_service_ids]
        }

        return self.requester.put(endpoint, data=data)   


    def user_call_center_agent_sign_out(self, user_id: str):
        
        endpoint = f"/user/call-centers/agents/sign-out"
        
        data = {
            "agentUserId": user_id,
        }

        return self.requester.put(endpoint, data=data)  
    
    
    def user_call_center_supervisor_agents(self, call_center_service_id: str, supervisor_user_id: str,
                                           user_ids: list):
        
        endpoint = f"/user/call-centers/agents/sign-out"
        
        data = {
            "serviceUserId": call_center_service_id,
            "supervisorUserId": supervisor_user_id,
            "users": [{"userId": user_id} for user_id in user_ids]
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
    
    def group_hunt_groups_status(self, service_user_ids: list, status: bool =True):
    
        endpoint = f"/groups/hunt-groups/status"
        
        data = {     
            "instances": [{'serviceUserId': service_user_id, 'isActive': status} 
                          for service_user_id in service_user_ids]
        }
        
        self.requester.put(endpoint, data=data)
        
    
    def group_hunt_group(self, service_provider_id: str, group_id, service_user_id: str, updates: dict):
    
        endpoint = f"/groups/hunt-groups"
        
        updates["serviceProviderId"] = [service_provider_id]
        updates["groupId"] = [group_id]
        updates["serviceUserId"] = [service_user_id]
        
        return self.requester.put(endpoint, data=updates)
            
        
    def group_hunt_group_weighted_call_distribution(self, service_provider_id: str, group_id, service_user_id: str, 
                                                    agents: dict):
        
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

    def user_services(self, user_id: str, services: list, assigned: bool =True):
        
        endpoint = f"/users/services"
        
        data = {
            "userId": user_id,
            "userServices": [{'service': service, 'assigned': assigned} for service in services]
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