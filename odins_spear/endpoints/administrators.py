from .base_endpoint import BaseEndpoint


class Administrators(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    # POST
    def post_group_admin(
        self,
        service_provider_id: str,
        group_id: str,
        user_id: str,
        password: str,
        payload: dict = {},
    ):
        """Builds a group-level administrator.

        Args:
            service_provider_id (str): Service provider ID where the admin should be built.
            group_id (str): Group ID where the admin should be built
            user_id (str): User ID of the admin.
            password (str): Password for the administrator profile. Note get.password_generate() can be used to get this.
            payload (dict, optional): Admin configuration data.

        Returns:
            Dict: Returns the admin profile.
        """

        endpoint = "/groups/admins"

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["userId"] = user_id
        payload["password"] = password

        return self._requester.post(endpoint, data=payload)

    def post_group_admin_policies_bulk(self, user_ids: list, policy_config: dict):
        """Applies policy settings to multiple group administrators.

        Note: See docs for formatting of parameters.

        Args:
            user_ids (list): User IDs of admins to apply policy to.
            policy_config (dict): Policy settings to apply to target users.

        Returns:
            Dict: Returns admins and policy applied.
        """
        endpoint = "/groups/admins/policies/bulk"

        data = {"users": [{"userId": user} for user in user_ids], "data": policy_config}

        self._requester.post(endpoint, data=data)

    # PUT
    # DELETE
    