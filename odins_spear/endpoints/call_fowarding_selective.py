from .base_endpoint import BaseEndpoint


class CallForwardingSelective(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_user_call_forwarding_selective(self, user_id: str):
        """Retrieves the Forwarding Selective status for a specified User, alongside the criteria.

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Forwarding enabled status and the Forwarding criteria.
        """

        endpoint = "/users/call-forwarding-selective"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_forwarding_selective_criterias(self, user_id: str):
        """Retrieves the Forwarding Selective status for a specified User, alongside the criteria's assigned.

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Forwarding enabled status and the Forwarding criteria's names and settings.
        """

        endpoint = "/users/call-forwarding-selective/criteria"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_forwarding_selective_criteria(self, user_id: str, criteria_name: str):
        """Retrieves the Forwarding Selective status for a specified User, alongside the specified Criteria

        Args:
            user_id (str): Target User ID
            criteria_name (str): Target Criteria Name

        Returns:
            Dict: Forwarding enabled status and the specified Criterias Settings.
        """

        endpoint = "/users/call-forwarding-selective/criteria"

        params = {"criteriaName": criteria_name, "userId": user_id}

        return self._requester.get(endpoint, params=params)


    # POST

    # PUT

    # DELETE
