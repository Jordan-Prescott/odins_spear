from .base_endpoint import BaseEndpoint


class DNs(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_group_dns(self, service_provider_id: str, group_id: str):
        """Gets all numbers assigned to group.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where group is hosted.
            group_id (str): Group ID of target group.

        Returns:
            Dict: Dictionary containing all DNs assigned to group.
        """

        endpoint = "/groups/dns"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    def get_group_dn_search(
        self,
        service_provider_id: str,
        group_id: str,
        dn: int,
        filter_type: str = None,
        limit: int = None,
    ):
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
        from ..utils.formatters import format_filter_value

        endpoint = "/groups/dns/search"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        if filter_type:
            params["dn"] = format_filter_value(filter_type, dn)
        if limit:
            params["limit"] = limit

        return self._requester.get(endpoint, params=params)

    def get_group_dn_details(self, service_provider_id: str, group_id: str):
        """Gets all numbers assigned to Group in detail. This will show where the number is assigned
        in a group such as which user or hunt group.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where group is hosted.
            group_id (str): Group ID of target group where numbers are located.

        Returns:
            Dict: Dictionary of numbers with details of each number.
        """

        endpoint = "/groups/dns/details"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    def get_system_dn_search(self, dn: int):
        """Searches for number from System level. This will return where the number is located on the system.
        It will show the Service Provider/ Enterprise, Group ID, and User ID the number is assigned to.

        Args:
            dn (int): Target number excluding country code e.g. 123456789

        Returns:
            List: List of dictionaries containing details of each number that fit the search criteria.
        """

        endpoint = "/system/dns/search"

        params = {"dn": f"+{dn}"}

        return self._requester.get(endpoint, params=params)

    def get_system_dn(self, dn: int):
        """Searches for number from System level. This will return where the number is located on the system.
        It will show the Service Provider/ Enterprise, Group ID, and User ID the number is assigned to.

        Args:
            dn (int): Target number excluding country code e.g. 123456789

        Returns:
            List: List of dictionaries containing details of each number that fit the search criteria.
        """

        endpoint = "/system/dns"

        params = {"phoneNumber": f"+{dn}"}

        return self._requester.get(endpoint, params=params)

    def get_system_dn_summary(self):
        """Returns all numbers assigned to system.

        Returns:
            List: List of all Service Providers/ Enterprises and numbers assigned in ranges.
        """

        endpoint = "/system/dns/summary"

        return self._requester.get(endpoint)

    def get_system_dn_utilization(self):
        """Returns DN statistics for each Service Provider/ Enterprise such as total DNs assigned.

        Returns:
            List: List of all Service Provider/ Enterprises with statistics of DNs for each.
        """

        endpoint = "/system/dns/utilization"

        return self._requester.get(endpoint)

    def get_service_provider_dn_search(
        self,
        service_provider_id: str,
        dn: int,
        filter_type: str = None,
        limit: int = None,
    ):
        """Searches for numbers assigned to Service Provider/ Enterprise and allows search criteria and limiting result.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where group is hosted.
            dn (int): Number/ part of number to search for.
            filter_type (str, optional): Options: equal to, starts with, or contains. Defaults to None.
            limit (int, optional): Limits the amount of values API returns. Defaults to None.

        Returns:
            List: List of numbers matching search criteria
        """
        from ..utils.formatters import format_filter_value

        endpoint = "/service-providers/dns/search"

        params = {"serviceProviderId": service_provider_id}

        if filter_type:
            params["dn"] = format_filter_value(filter_type, dn)
        if limit:
            params["limit"] = limit

        return self._requester.get(endpoint, params=params)

    def get_service_provider_dns(self, service_provider_id: str):
        """Returns all numbers assigned to Service Provider/ Enterprise with the group its assigned to
        and if the numbers can be deleted.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where target numbers are located.

        Returns:
            Dict: All numbers assigend to Service Provider/ Enterprise with group and delete status.
        """

        endpoint = "/service-providers/dns"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    # POST

    def post_group_dns(
        self,
        service_provider_id: str,
        group_id: str,
        start_of_range_number: str,
        end_of_range_number: str,
    ):
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
            "dns": [{"min": start_of_range_number, "max": end_of_range_number}],
        }

        return self._requester.post(endpoint, data=data)

    def post_group_dns_assign_bulk(
        self,
        service_provider_id: str,
        group_id: str,
        start_of_range_number: int,
        end_of_range_number: int,
    ):
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
            "dns": [{"min": start_of_range_number, "max": end_of_range_number}],
        }

        return self._requester.post(endpoint, data=data)

    def post_group_dns_unassign_bulk(
        self,
        service_provider_id: str,
        group_id: str,
        start_of_range_number: int,
        end_of_range_number: int,
    ):
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
            "dns": [{"min": start_of_range_number, "max": end_of_range_number}],
        }

        return self._requester.post(endpoint, data=data)

    def post_service_provider_dns(
        self,
        service_provider_id: str,
        start_of_range_number: int,
        end_of_range_number: int,
    ):
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
            "dns": [{"min": start_of_range_number, "max": end_of_range_number}],
        }

        return self._requester.post(endpoint, data=data)

    # PUT

    def put_group_dns_activate(
        self, service_provider_id: str, group_id: str, activated: bool, numbers: list
    ):
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
            "dns": [
                {"activated": activated, "min": num, "max": None} for num in numbers
            ],
        }

        return self._requester.put(endpoint, data=data)

    # DELETE

    def delete_group_dns(
        self,
        service_provider_id: str,
        group_id: str,
        start_of_range_number: str,
        end_of_range_number: str,
    ):
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
            ],
        }

        return self._requester.delete(endpoint, data=data)

    def service_provider_dns(
        self,
        service_provider_id: str,
        start_of_range_number: str,
        end_of_range_number: str,
    ):
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
            "dns": [{"min": start_of_range_number, "max": end_of_range_number}],
        }

        return self._requester.delete(endpoint, data=data)
