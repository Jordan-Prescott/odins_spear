from .base_endpoint import BaseEndpoint


class Registration(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_user_registration(self, user_id: str):
        """Gets a users devices and if those devices are registered. This includes soft phones.

        Args:
            user_id (str): Target user ID to check registration

        Returns:
            dict: All users devices and details on device such as registration.
        """

        endpoint = "/users/registration"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_bulk_user_registration(self, service_provider_id: str, group_id: str):
        """Gets all users in a group and their device registrations. This includes soft phones.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is hosted.
            group_id (str): Target Group ID where users are located.

        Returns:
            dict: All users devices and details on device such as registration.
        """

        endpoint = "/users/registration/bulk"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)


# POST

# PUT

# DELETE
