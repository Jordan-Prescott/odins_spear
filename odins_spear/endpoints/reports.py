from .base_endpoint import BaseEndpoint


class Reports(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_user_report(self, user_id: str):
        """Detailed report of user including services and service packs assigned.

        Args:
            user_id (str): Target user id of user.

        Returns:
            dict: Detailed report of user including services and service packs.
        """

        endpoint = "/users/reports/users"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)


# POST

# PUT

# DELETE
