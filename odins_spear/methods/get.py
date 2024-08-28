from ..utils.formatting import format_filter_value
from ..exceptions import *

class Get():

    filters = [
        "macAddress", "lastName", "firstName", "dn",
        "emailAddress", "userId", "extension"
    ]

    def __init__(self, requester):
        self.requester = requester

#SESSION

    def session(self):

        endpoint = "/auth/session"

        return self.requester.get(endpoint)

#ACCOUNT AUTHORIZATION CODES
#ADMINISTRATORS
#ADVICE OF CHARGE
#ALTERNATE NUMBERS

    def user_alternate_numbers(self, user_id: str):
        """Fetches a list of a user/ service such as Auto Attendant, Hunt Group, or Call Centres 
        alternate numebrs.

        Args:
            user_id (str): Target user/ service_user_id

        Returns:
            Dict: List of all alternate numbers assigned to the user/ service.
        """
        
        endpoint = "/users/alternate-numbers"
        
        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)

#ANSWER CONFIRMATION
#ALTERNATE USER ID
#ANNOUNCEMENTS
#ANONYMOUS CALL REJECTION
#ATTENDANT CONSOLE
#AUTHENTICATION
#AUTO ATTENDANTS

    def auto_attendants(self, service_provider_id: str, group_id: str):
        """Returns a complete list of all Auto Attendants in a single group.

        Args:
            service_provider_id (str): Service Provider where Group is hosted.
            group_id (str): Target Group where Auto Attendants are hosted.

        Returns:
            List: List of Auto Attendants with basic info on them.
        """

        endpoint = "/groups/auto-attendants"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)

    def auto_attendant(self, service_user_id: str):
        """Returns detailed information of a singel Auto Attendant.

        Args:
            service_user_id (str): User ID of target Auto Attendant.

        Returns:
            dict: Detailed information of target Auto Attendant.
        """

        endpoint = "/groups/auto-attendants"

        params = {
            "serviceUserId": service_user_id
        }

        return self.requester.get(endpoint, params=params)

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

    def group_call_centers(self, service_provider_id: str, group_id: str):
        """Retrieves a list of active call centers within a specified group, along with their settings.

        Args:
            service_provider_id (str): Target Service Provider where group is hosted
            group_id (str): Target Group ID

        Returns:
            List: List of Call Centers and their settings.
        """

        endpoint = "/groups/call-centers"
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }
        return self.requester.get(endpoint, params=params)


    def group_call_center(self, service_user_id: str):
        """Retrieves deatiled information on a single Call Center.

        Args:
            service_user_id (str): Target Call Center's ID

        Returns:
            Dict: Target Call Centers details.
        """

        endpoint = "/groups/call-centers"

        params = {
            "serviceUserId": service_user_id
        }

        return self.requester.get(endpoint, params=params)


    def user_call_center(self, user_id: str):
        """Retrieves a list of call centers that the specified user is currently associated with.

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Agents Call Centers setting and a list of the User's associated Call Centers.
        """

        endpoint = "/users/call-center"

        params = {
            "userId": user_id
        }
        try:
            import requests.exceptions
            response = self.requester.get(endpoint, params=params)
        except requests.exceptions.RequestException:
            raise OSLicenseNonExistent
        else:
            return response
    
    
    def group_call_center_bounced_calls(self, service_user_id: str):
        """Retrieves the number of rings before a call is bounced from the specified call center.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Amount of Rings before a call is Bounced
        """
        
        endpoint = "/groups/call-centers/bounced-calls"
        
        params = {
            "serviceUserId": service_user_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def group_call_center_forced_forwarding(self, service_user_id: str):
        """Retrieves the forwarding number for a call center if it is set to forward calls, along with any associated audio messages.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Number to be Forwarded to, alongside any Audio Messages.
        """
        
        endpoint = "/groups/call-centers/forced-forwarding"
        
        params = {
            "serviceUserId": service_user_id
        }

        return self.requester.get(endpoint, params=params)

    
    def group_call_center_overflow(self, service_user_id):
        """Retrieves the forwarding number for a user when all call center agents are busy, along with any associated audio messages.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Dict: Call Centers overflow configuration.
        """
        
        endpoint = "/groups/call-centers/overflow"
        
        params = {
            "serviceUserId": service_user_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def group_call_center_stranded_calls(self, service_user_id):
        """Retrieves the forwarding number for a user when a call center doesn't answer, along with any associated audio messages.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Call Centers stranded call configuration.
        """
        
        endpoint = "/groups/call-centers/stranded-calls"
        
        params = {
            "serviceUserId": service_user_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def group_call_center_stranded_calls_unavailable(self, service_user_id):
        """Retrieves the forwarding number for a user when a call center doesn't answer, along with the count of agents with an unavailable code in the call center.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Number to be Forwarded to, and Agents with an Unavailable Code set.
        """
        
        endpoint = "/groups/call-centers/stranded-calls-unavailable"
        
        params = {
            "serviceUserId": service_user_id
        }

        return self.requester.get(endpoint, params=params)
    
#CALL CONTROL
#CALL FORWARDING ALWAYS

    def user_call_forwarding_always(self, user_id: str):

        """Retrieves the Forwarding Always status for the specified User.

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Forwarding enabled status, and the Number to be Forwarded to.
        """
        
        endpoint = "/users/call-forwarding-always"
        
        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params) 
    
    
    def bulk_call_forwarding_always(self, service_provider_id: str, group_id: str):

        """Retrieves the Forwarding Always status for all users within a specified group.

        Args:
            service_provider_id (str): Target Service Provider where group is hosted
            group_id (str): Target Group ID

        Returns:
            List: Forwarding enabled status, the Number to be Forwarded to, and User information.
        """
        
        endpoint = "/users/call-forwarding-always/bulk"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)


#CALL FORWARDING BUSY

    def user_call_forwarding_busy(self, user_id: str):
        """Retrieves the Forwarding Not Reachable status for the specified user.

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Forwarding enabled status, and the Number to be Forwarded to.
        """
        
        endpoint = "/users/call-forwarding-busy"
        
        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def bulk_call_forwarding_busy(self, service_provider_id: str, group_id: str):
        """Retrieves the Forwarding Busy status for all users within a specified group.

        Args:
            service_provider_id (str): Target Service Provider where group is hosted
            group_id (str): Target Group ID
            

        Returns:
            List: Forwarding enabled status, the Number to be Forwarded to, and User information.
        """
        
        endpoint = "/users/call-forwarding-busy/bulk"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)


#CALL FORWARDING NO ANSWER

    def user_call_forwarding_no_answer(self, user_id: str):
        """Retrieves the Forwarding No Answer status for the specified user

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Forwarding enabled status, and the Number to be Forwarded to.
        """
        
        endpoint = "/users/call-forwarding-no-answer"
        
        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def bulk_call_forwarding_no_answer(self, service_provider_id: str, group_id: str):
        """Retrieves the Forwarding No Answer status for all users within a specified group.

        Args:
            service_provider_id (str): Target Service Provider where group is hosted
            group_id (str): Target Group ID
            

        Returns:
            List: Forwarding enabled status, the Number to be Forwarded to, and User information.
        """
        
        endpoint = "/users/call-forwarding-no-answer/bulk"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)


#CALL FORWARDING NOT REACHABLE

    def user_call_forwarding_not_reachable(self, user_id: str):
        """Retrieves the Forwarding Not Reachable status for the specified user

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Forwarding enabled status, and the Number to be Forwarded to.
        """
        
        endpoint = "/users/call-forwarding-not-reachable"
        
        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def bulk_call_forwarding_not_reachable(self, service_provider_id: str, group_id: str):
        """Retrieves the Forwarding Not Reachable status for all users within a specified group.

        Args:
            service_provider_id (str): Target Service Provider where group is hosted
            group_id (str): Target Group ID
            

        Returns:
            List: Forwarding enabled status, the Number to be Forwarded to, and User information.
        """
        
        endpoint = "/users/call-forwarding-not-reachable/bulk"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)


#CALL FORWARDING SELECTIVE

    def user_call_forwarding_selective(self, user_id: str):
        """Retrieves the Forwarding Selective status for a specified User, alongside the criteria.

        Args:
            user_id (str): Target User ID
            
        Returns:
            Dict: Forwarding enabled status and the Forwarding criteria.
        """
        
        endpoint = "/users/call-forwarding-selective"
        
        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def user_call_forwarding_selective_criterias(self, user_id: str):
        """Retrieves the Forwarding Selective status for a specified User, alongside the criteria's assigned.

        Args:
            user_id (str): Target User ID
            
        Returns:
            Dict: Forwarding enabled status and the Forwarding criteria's names and settings.
        """
        
        endpoint = "/users/call-forwarding-selective/criteria"
        
        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def user_call_forwarding_selective_criteria(self, user_id: str, criteria_name: str):
        """Retrieves the Forwarding Selective status for a specified User, alongside the specified Criteria

        Args:
            user_id (str): Target User ID
            criteria_name (str): Target Criteria Name
            
        Returns:
            Dict: Forwarding enabled status and the specified Criterias Settings.
        """
        
        endpoint = "/users/call-forwarding-selective/criteria"
        
        params = {
            "criteriaName": criteria_name,
            "userId": user_id
        }
        
        return self.requester.get(endpoint, params=params)

#CALL NOTIFY
#CALL PARK
#CALL PICKUP

    def call_pickup_group_user(self, service_provider_id, group_id, user_id):
        """Retrieves Pickup Group information for the specified user.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): The Target Group ID the user is apart of.
            user_id (str): Target User ID
            
        Returns:
            Dict: Specified users pickup group, and the users within that group.
        """

        endpoint = "/groups/call-pickup/user"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)

#CALL POLICIES
#CALL PROCESSING POLICIES
#CALL RECORDING
#CALL RECORDS

    def users_stats(self, user_id: str, start_date:str, end_date: str = None, 
                    start_time: str = "00:00:00", end_time:str = "23:59:59", time_zone: str = "Z"):
        """Pulls a single users call statistics for a specified period of time. 

        Args:
            user_id (str): Target user ID you would like to pull call statistics for.
            start_date (str): Start date of desired time period. Date must follow format 'YYYY-MM-DD'
            end_date (str, optional): End date of desired time period. Date must follow format 'YYYY-MM-DD'.\
                If this date is the same as Start date you do not need this parameter. Defaults to None.
            start_time (_type_, optional): Start time of desired time period. Time must follow formate 'HH:MM:SS'. \
                If you do not need to filter by time and want the whole day leave this parameter. Defaults to "00:00:00". MAX Request is 3 months.
            end_time (_type_, optional): End time of desired time period. Time must follow formate 'HH:MM:SS'. \
                If you do not need to filter by time and want the whole day leave this parameter. Defaults to "23:59:59". MAX Request is 3 months.
            time_zone (str, optional): A specified time you would like to see call records in. \
                Time zone must follow format 'GMT', 'EST', 'PST'. Defaults to "Z" (UTC Time Zone).

        Returns:
            Dict: Users call record statistics for specified time period.
        """
        
        #checks if end_date has been left and therefore we assume user wants same date.
        if not end_date:
            end_date = start_date
        
        endpoint = "/users/call-records/stats"

        params = {
            "userIds": user_id,
            "startTime": f"{start_date}T{start_time}{time_zone}",
            "endTime": f"{end_date}T{end_time}{time_zone}"
        }

        return self.requester.get(endpoint, params=params)

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

    def group_dns(self, service_provider_id:str, group_id:str):
        """Gets all numbers assigned to group.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where group is hosted.
            group_id (str): Group ID of target group.

        Returns:
            Dict: Dictionary containing all DNs assigned to group. 
        """

        endpoint = "/groups/dns"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }
        
        return self.requester.get(endpoint, params=params)
    
    
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

        endpoint = "/groups/dns/search"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }
        
        if filter_type:
            params["dn"] = format_filter_value(filter_type, dn)
        if limit:
            params["limit"] = limit
            
        return self.requester.get(endpoint, params=params)
    
    
    def group_dn_details(self, service_provider_id:str, group_id:str):
        """Gets all numbers assigned to Group in detail. This will show where the number is assigned
        in a group such as which user or hunt group. 

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where group is hosted.
            group_id (str): Group ID of target group where numbers are located.

        Returns:
            Dict: Dictionary of numbers with details of each number.
        """
        
        endpoint = "/groups/dns/details"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def system_dn_search(self, dn: int):
        """Searches for number from System level. This will return where the number is located on the system.
        It will show the Service Provider/ Enterprise, Group ID, and User ID the number is assigned to.

        Args:
            dn (int): Target number excluding country code e.g. 123456789

        Returns:
            List: List of dictionaries containing details of each number that fit the search criteria. 
        """
        
        endpoint = "/system/dns/search"

        params = {
            "dn": f"+{dn}"
        }    

        return self.requester.get(endpoint, params=params)
    
    
    def system_dn(self, dn: int):
        """Searches for number from System level. This will return where the number is located on the system.
        It will show the Service Provider/ Enterprise, Group ID, and User ID the number is assigned to.

        Args:
            dn (int): Target number excluding country code e.g. 123456789

        Returns:
            List: List of dictionaries containing details of each number that fit the search criteria. 
        """
        
        endpoint = "/system/dns"
        
        params = {
            "phoneNumber": f"+{dn}"
        } 

        return self.requester.get(endpoint, params=params)
    
    
    def system_dn_summary(self):
        """Returns all numbers assigned to system.

        Returns:
            List: List of all Service Providers/ Enterprises and numbers assigned in ranges.
        """
        
        endpoint = "/system/dns/summary"
        
        return self.requester.get(endpoint)
    
    
    def system_dn_utilization(self):
        """Returns DN statistics for each Service Provider/ Enterprise such as total DNs assigned.

        Returns:
            List: List of all Service Provider/ Enterprises with statistics of DNs for each.
        """
        
        endpoint = "/system/dns/utilization"   
       
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

        endpoint = "/service-providers/dns/search"
        
        params = {
            "serviceProviderId": service_provider_id
        }
        
        if filter_type:
            params["dn"] = format_filter_value(filter_type, dn)
        if limit:
            params["limit"] = limit

        return self.requester.get(endpoint, params=params)
        
    
    def service_provider_dns(self, service_provider_id: str):
        """Returns all numbers assigned to Service Provider/ Enterprise with the group its assigned to
        and if the numbers can be deleted.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where target numbers are located.

        Returns:
            Dict: All numbers assigend to Service Provider/ Enterprise with group and delete status.
        """
        
        endpoint = "/service-providers/dns"
        
        params = {
            "serviceProviderId": service_provider_id
        }

        return self.requester.get(endpoint, params=params)
        
    
#DO NOT DISTURB

    def user_do_not_disturb(self, user_id: str):
        """Returns the specificied users DND and Ring Splash state.

        Args:
            user_id (str): Target user id to return data. 

        Returns:
            Dict: States DND and Ring Splash status.
        """
        
        endpoint = "/users/do-not-disturb"
        
        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)

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
    
    def groups(self, service_provider_id: str):
        """Returns the specificied Service Provider's Groups.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            List: List of groups and their Names, alongside groupID's and userLimits.
        """

        endpoint = "/groups"
        
        params = {
            "serviceProviderId": service_provider_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def group(self, service_provider_id, group_id):
        """Returns the specificied Group's settings and information.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID

        Returns:
            Dict: Returns information about the specified group, such as the DID, userCount and Domain.
        """

        endpoint = "/groups"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)

#GROUP NAVIGATION
#HOTELING GUEST
#HOTELING HOST
#HUNT GROUPS

    def group_hunt_groups(self, service_provider_id, group_id):
        """Returns a list of all the Hunt Groups within the specified Group.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID

        Returns:
            List: Returns a list of every Hunt Group within a Group, alongside their extension and name.
        """

        endpoint = "/groups/hunt-groups"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)

    def group_hunt_group(self, service_user_id):
        """Returns detailed information about the specified Hunt Group.

        Args:
            service_user_id (str): UserID of the target Hunt Group.

        Returns:
            Dict: Returns the specified Hunt Groups settings and information, such as group policies, agents, and extension.
        """

        endpoint = "/groups/hunt-groups"

        params = {
            "serviceUserId" : service_user_id
        }

        return self.requester.get(endpoint, params=params)

    def group_hunt_group_user(self, service_provider_id, group_id, user_id):
        """Returns the Hunt Group's the specified User is apart of.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID
            user_id (str): Target User ID

        Returns:
            List: Returns the Hunt Group's a user is within, alongside their settings within that Hunt Group.
        """

        endpoint = "/groups/hunt-groups/user"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)
    
    def group_hunt_groups_available_users(self, service_provider_id: str, group_id: str):

        """Returns a list of all users within the service provider that are available to be assigned to a hunt group in the specified group. 

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID

        Returns:
            List: available users (dict)
        """

        endpoint = "/groups/hunt-groups/users"

        params = {
            "serviceProviderId": service_provider_id, 
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)


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

    def password_generate(self, service_provider_id: str, group_id: str) -> dict:
        """Generates a single passwords following the groups rules.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate password for. 

        Returns:
            dict: Single password generated according to the groups rules.
        """
        
        endpoint = "/password/generate"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def passwords_generate(self, service_provider_id: str, group_id: str, limit: int =10) -> dict:
        """Generates a multiple passwords to the limit set in pararmeters.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate password for. 
            limit (int, optional): Number of passwords api will return. Defaults to 10.

        Returns:
            dict: Multiple passwords generated according to the groups rules.
        """
                
        endpoint = "/password/generate"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "limit": limit
        }

        return self.requester.get(endpoint, params = params)
        
    
    def passcode_generate(self, service_provider_id: str, group_id: str) -> dict:
        """Generates a single passcode following group rules.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate passcode for. 

        Returns:
            dict: Single passcode generated according to the groups rules.
        """
        
        endpoint = "/passcode/generate"
    
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params = params)
    
    
    def passcodes_generate(self, service_provider_id: str, group_id: str, limit: int =10) -> dict:
        """Generates a multiple passcodes to the limit set in pararmeters.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate passcodes for. 
            limit (int, optional): Number of passwords api will return. Defaults to 10.

        Returns:
            dict: Multiple passcodes generated according to the groups rules.
        """
        
        endpoint = "/passcode/generate"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "limit": limit
        }

        return self.requester.get(endpoint, params = params)
    
    
    def sip_password_generate(self) -> dict:
        """Generates a single SIP password.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate SIP password for. 

        Returns:
            dict: Single SIP password generated according to the groups rules.
        """
        
        endpoint = "/sip-password/generate"
        
        return self.requester.get(endpoint)
    
    
    def sip_passwords_generate(self, limit: int =10) -> dict:
        """Generates multiple SIP passwords to the limit set in parameters. Defaults to 10.

        Args:
            limit (int, optional): Number of passwords api will return. Defaults to 10.

        Returns:
            dict: Mutliple SIP passwords generated according to the groups rules.
        """

        endpoint = "/password/generate"
        
        params = {
            "limit": limit
        }

        return self.requester.get(endpoint, params = params)

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

    def user_registration(self, user_id: str):
        """Gets a users devices and if those devices are registered. This includes soft phones.

        Args:
            user_id (str): Target user ID to check registration

        Returns:
            dict: All users devices and details on device such as registration.
        """
        
        endpoint = "/users/registration"

        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def bulk_user_registration(self, service_provider_id: str, group_id: str):
        """Gets all users in a group and their device registrations. This includes soft phones.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is hosted. 
            group_id (str): Target Group ID where users are located. 

        Returns:
            dict: All users devices and details on device such as registration.
        """
        
        endpoint = "/users/registration/bulk"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)

#REMOTE OFFICE
#REPORTS

    def user_report(self, user_id: str):
        """ Detailed report of user including services and service packs assigned.

        Args:
            user_id (str): Target user id of user.

        Returns:
            dict: Detailed report of user including services and service packs.
        """

        endpoint = "/users/reports/users"

        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)

#RESELLERS
#ROUTE LIST
#ROUTING PROFILE
#SCHEDULES

    def group_schedules(self, service_provider_id: str, group_id: str):
        """ Retrieves the Business Schedules for the specified group.

        Args:
            service_provider_id (str): Target Service Provider ID where group is hosted.
            group_id (str): Target Group ID with schedules.

        Returns:
            List: List of all the groups schedules, including Name, Type and Level.
        """
        
        endpoint = "/groups/schedules"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def group_events(self, service_provider_id: str, group_id: str, name: str, type: str):
        """ Retrieves the Business Schedule's Events for the specified group.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID
            name (str): Name of the target Busisness Schedule
            type (str): The type of the Business Schedule (Time, Holiday)

        Returns:
            List: List of each Business Schedule Event, including startTime and endTime.
        """
        
        endpoint = "/groups/events"
        
        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "name": name,
            "type": type
        }

        return self.requester.get(endpoint, params=params)   
    
    
#SECURITY CLASSIFICATION
#SELECTIVE CALL ACCEPTANCE
#SELECTIVE CALL REJECTION
#SEQUENTIAL RING
#SERIES COMPLETION
#SERVICE PACKS
#SERVICE PROVIDERS

    def service_providers(self, reseller_id=None):
        """
        Args:
            reseller_id (str): Only list the Service Provider IDs within the specified Reseller.
        """
        endpoint = "/service-providers"
        params = {
            "resellerId": reseller_id
        }
        
        return self.requester.get(endpoint, params=params)


    def service_provider(self, service_provider_id: str):
        """
        Args:
            reseller_id (str): Only list the Service Provider IDs within the specified Reseller.
        """
        
        endpoint = "/service-providers"
        
        params = {
            "serviceProviderId": service_provider_id
        }

        return self.requester.get(endpoint, params=params)

#SERVICES

    def user_services_assigned(self, user_id: str):
        """

        Args:
            user_id (str): _description_
        """
        endpoint = "/users/services/assigned"
        
        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)

    def user_services(self, user_id: str):
        """Fetch all services assigned to a broadwrok entity, this can be 
        a user, AA, CC, or HG.

        Args:
            user_id (str): User ID of the target Broadworks entity.

        Returns:
            Dict: Broadwork entiy and a list of services assigned.
        """

        endpoint = "/users/services"

        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)

    def group_services(self, group_id: str, service_provider_id: str):
        """
        Fetch all userServices, groupServices and servicePackServices assigned to a group.

        Args:
            group_id (str): GroupID of the target 
            service_provider_id (str): Service Provider or Enterprise ID of the target.

        Returns:
            Dict: Authorised and assigned services within the group.
        """

        endpoint = "/groups/services"

        params = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id
        }

        return self.requester.get(endpoint, params=params)

    def group_services_user_assigned(self, group_id: str, service_provider_id: str, service_name: str, service_type: str):
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

        endpoint = "/groups/services/assigned"

        params = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id,
            "serviceType": service_type,
            "serviceName": service_name
        }

        return self.requester.get(endpoint, params=params)

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
    
    def group_trunk_groups_call_capacity(self, service_provider_id: str, group_id: str):
        """Fetches Trunk Call Capacity data for a single Group. 

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located.
            group_id (str): Target Group to return data on.

        Returns:
            Dict: Trunk Group Call Capacity data of target group.
        """
        
        endpoint = "/groups/trunk-groups/call-capacity"
        
        params = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def group_trunk_group(self, service_provider_id: str, group_id: str, trunk_group_name: str):
        """Fetches all Trunk Group details of a single Trunk Group in a Group.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located.
            group_id (str): Group ID where the target Trunk Group is located.
            trunk_group_name (str): Target Trunk Group Name.

        Returns:
            Dict: Details of a target trunk group.
        """
        
        endpoint = "/groups/trunk-groups"
        
        params = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id,
            "name": trunk_group_name
        }

        return self.requester.get(endpoint, params=params)
    
    
    def group_trunk_groups(self, service_provider_id: str, group_id: str):
        """Fetches list of all trunk groups in a single group.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located.
            group_id (str): Group ID where the target Trunk Group is located.

        Returns:
            List: List of core details of all Trunk Groups located in a single Group.
        """
        
        endpoint = "/groups/trunk-groups"
        
        params = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def service_provider_trunk_group_call_capacity(self, service_provider_id: str):
        """Fetches trunk call capacity details of a single Service Provider.

        Args:
            service_provider_id (str): Target Service Provider/ Enterprise ID.

        Returns:
            Dict: Trunk call capacity details of a single Service Provider/ Enterprise ID.
        """
        
        endpoint = "/service-providers/trunk-groups/call-capacity"
        
        params = {
            "serviceProviderId": service_provider_id
        }

        return self.requester.get(endpoint, params=params)
    
    
    def service_provider_trunk_call_capacity_report(self, service_provider_id: str):
        """Fetches trunk call capacity details of Service Provider/ Enterprise and all Groups in the SP/ ENT.

        Args:
            servive_provider_id (str): Target Service Provider/ Enterprise ID.

        Returns:
            Dict: Breakdown of all trunk call capacity details of target Service Provider/ Enterprise and all Groups \
                in the target SP/ ENT.
        """
        
        endpoint = "/service-providers/trunk-groups/call-capacity/reports"
        
        params = {
            "serviceProviderId": service_provider_id
        }

        return self.requester.get(endpoint, params=params)
        

#TWO STAGE DIALING
#USERS

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

        #Supported Filters
        macAddress: search by device
        lastName: filter by lastName
        firstName: filter by firstName
        dn: filter by dn
        emailAddress: filter by emailAddress
        userId: filter by userId
        extension: filter by extension

        ####Examples
        Get all users in Enterprise ent1
        GET /api/v2/users?serviceProviderId=ent1

        Get all users in Group grp1
        GET /api/v2/users?serviceProviderId=ent1&groupId=grp1

        Get up to 10 users in the system with a last name that contains smith
        GET /api/v2/users?lastName=*smith*&limit=10

        Get the users in grp1 that have a phone number that starts with 513333
        GET /api/v2/users?serviceProviderId=ent1&groupId=grp1&dn=513333*
        """

        endpoint = "/users?"
        
        params = {}

        if service_provider_id:
            params["serviceProviderId"] = service_provider_id
            if group_id:
                params["groupId"] = group_id
        if filter:
            params[filter] = format_filter_value(filter_type, filter_value)
        if limit:
            params["limit"] = limit
        if extended:
            params["extended"] = True

        return self.requester.get(endpoint, params=params)

    def user_by_id(self, user_id: str):
        """Returns extensive details of a single user including alias, enpoint device, and more common
        details like first and last name. 

        Args:
            user_id (str): Target user ID of the user you would like to review.

        Returns:
            Dict: Python dictionary of the users details 
        """

        endpoint = "/users"

        params = {
            "userId": user_id
        }

        return self.requester.get(endpoint, params=params)

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
