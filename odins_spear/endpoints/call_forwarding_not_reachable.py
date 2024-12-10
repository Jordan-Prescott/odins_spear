from .base_endpoint import BaseEndpoint


class CallForwardingNotReachable(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_user_call_forwarding_not_reachable(self, user_id: str):
        """Retrieves the Forwarding Not Reachable status for the specified user

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Forwarding enabled status, and the Number to be Forwarded to.
        """

        endpoint = "/users/call-forwarding-not-reachable"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_bulk_call_forwarding_not_reachable(
        self, service_provider_id: str, group_id: str
    ):
        """Retrieves the Forwarding Not Reachable status for all users within a specified group.

        Args:
            service_provider_id (str): Target Service Provider where group is hosted
            group_id (str): Target Group ID


        Returns:
            List: Forwarding enabled status, the Number to be Forwarded to, and User information.
        """

        endpoint = "/users/call-forwarding-not-reachable/bulk"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

# POST

# PUT

# DELETE
