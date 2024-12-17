from .base_endpoint import BaseEndpoint


class Groups(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_groups(self, service_provider_id: str) -> list:
        """Returns the specificied Service Provider's Groups.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            List: List of groups and their Names, alongside groupID's and userLimits.
        """

        endpoint = "/groups"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_group(self, service_provider_id: str, group_id: str) -> dict:
        """Returns the specificied Group's settings and information.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID

        Returns:
            Dict: Returns information about the specified group, such as the DID, userCount and Domain.
        """

        endpoint = "/groups"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)


# POST

# PUT

# DELETE
