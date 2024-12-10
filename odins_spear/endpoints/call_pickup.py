from .base_endpoint import BaseEndpoint


class CallPickup(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_call_pickup_group_user(
        self, service_provider_id: str, group_id: str, user_id: str
    ):
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
            "userId": user_id,
        }

        return self._requester.get(endpoint, params=params)

    # POST

    # PUT

    # DELETE
