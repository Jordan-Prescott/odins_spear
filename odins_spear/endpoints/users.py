from .base_endpoint import BaseEndpoint
from ..utils.formatters import format_filter_value


class Users(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET
    def get_users(
        self,
        service_provider_id: str = None,
        group_id: str = None,
        filter: str = None,
        filter_type: str = None,
        filter_value: str = None,
        limit: int = None,
        extended=False,
    ):
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

        return self._requester.get(endpoint, params=params)

    def get_user_by_id(self, user_id: str):
        """Returns extensive details of a single user including alias, enpoint device, and more common
        details like first and last name.

        Args:
            user_id (str): Target user ID of the user you would like to review.

        Returns:
            Dict: Python dictionary of the users details
        """

        endpoint = "/users"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    # POST
    def post_user(
        self,
        service_provider_id: str,
        group_id: str,
        user_id: str,
        first_name: str,
        last_name: str,
        extension: str,
        web_auth_password: str,
        payload: dict = {},
    ):
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

        payload["callingLineIdFirstName"] = (
            first_name
            if not payload.get("callingLineIdFirstName")
            else payload["callingLineIdFirstName"]
        )
        payload["callingLineIdLastName"] = (
            last_name
            if not payload.get("callingLineIdLastName")
            else payload["callingLineIdLastName"]
        )

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["userId"] = user_id
        payload["firstName"] = first_name
        payload["lastName"] = last_name
        payload["extension"] = extension
        payload["password"] = web_auth_password

        return self._requester.post(endpoint, data=payload)

    # PUT
    def put_users_bulk(self, users: list, updates: dict):
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

        data = {"users": target_users, "data": updates}

        return self._requester.put(endpoint, data=data)

    def put_user(
        self, service_provider_id: str, group_id: str, user_id: str, updates: dict
    ):
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

        return self._requester.put(endpoint, data=updates)

    def put_user_portal_passcode(self, user_id: str, new_passcode: str):
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
            from ..exceptions import OSInvalidCode

            raise OSInvalidCode

        endpoint = "/users/portal-passcode"

        data = {"userId": user_id, "newPasscode": new_passcode}

        return self._requester.put(endpoint, data=data)

    # DELETE
