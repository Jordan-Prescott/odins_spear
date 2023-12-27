class Get():
    def __init__(self, requester):
        self.requester = requester
        
    # AUTO ATTENDANTS
    
    def auto_attendants(self, service_provider_id, group_id):
        """_summary_

        Args:
            service_provider_id (_type_): _description_
            group_id (_type_): _description_

        Returns:
            _type_: _description_
        """

        endpoint = f"/auto-attendants?serviceProviderId={service_provider_id}&groupId={group_id}"
        
        return self.requester.get(endpoint)
    
     # REPORTS  
    
    def user_report(self, user_id):
        """ Detailed report of user including services and service packs assigned.

        Args:
            user_id (str): Target user id of user.

        Returns:
            dict: Detailed report of user including services and service packs.
        """
        
        endpoint = f"/users/reports/users?userId={user_id}"
        
        return self.requester.get(endpoint)

    # USER 
    
    def users(self, servive_provider_id: str =None, group_id: str =None, 
                  filter: str =None, filter_type: str =None, filter_value: str =None,
                  limit: int =None):
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
            endpoint += f"{self._format_filter(filter, filter_type, filter_value)}"   
        if limit:
            # TODO: Limit is failing when needed, odin to resolve
            endpoint += f"&limit={limit}"

        return self.requester.get(endpoint)
    
    def user_by_id(self, user_id):
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        endpoint = f"/users?userId={user_id}"
        
        return self.requester(endpoint)
    
