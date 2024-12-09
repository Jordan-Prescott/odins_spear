from .base_endpoint import BaseEndpoint


class HuntGroups(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_group_hunt_groups(self, service_provider_id, group_id):
        """Returns a list of all the Hunt Groups within the specified Group.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID

        Returns:
            List: Returns a list of every Hunt Group within a Group, alongside their extension and name.
        """

        endpoint = "/groups/hunt-groups"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    def get_group_hunt_group(self, service_user_id):
        """Returns detailed information about the specified Hunt Group.

        Args:
            service_user_id (str): UserID of the target Hunt Group.

        Returns:
            Dict: Returns the specified Hunt Groups settings and information, such as group policies, agents, and extension.
        """

        endpoint = "/groups/hunt-groups"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_hunt_group_user(self, service_provider_id, group_id, user_id):
        """Returns the Hunt Group's the specified User is apart of.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID
            user_id (str): Target User ID

        Returns:
            List: Returns the Hunt Group's a user is within, alongside their settings within that Hunt Group.
        """

        endpoint = "/groups/hunt-groups/user"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "userId": user_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_group_hunt_groups_available_users(
        self, service_provider_id: str, group_id: str
    ):
        """Returns a list of all users within the service provider that are available to be assigned to a hunt group in the specified group.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID

        Returns:
            List: available users (dict)
        """

        endpoint = "/groups/hunt-groups/users"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    # POST

    def post_group_hunt_group(
        self,
        service_provider_id: str,
        group_id: str,
        service_user_id: str,
        clid_first_name: str,
        clid_last_name: str,
        extension: str,
        payload: dict = {},
        agents: list = [],
        policy: str = "Regular",
        no_answer_number_of_rings: int = 5,
        forward_timeout_seconds: int = 0,
    ):
        """
        Builds a hunt group (HG) in the specified group.

        Args:
            service_provider_id (str): The service provider ID in which the target group is built.
            group_id (str): The group ID where the HG should be built.
            service_user_id (str): The service user ID for the new HG. This must include the domain of the user.
            clid_first_name (str): The Calling Line ID first name.
            clid_last_name (str): The Calling Line ID last name.
            extension (str): The extension number for the HG. This must be entered as a string.
            payload (dict, optional): HG configuration data.
            agents (list, optional): List of user IDs (str) that should be assigned to the new HG. The user(s) must already exist in the group.
            policy (str, optional): Regular, Circular, Simultaneous, Uniform, Weighted. Defaults to Regular.
            no_answer_number_of_rings (int, optional): Defaults to 5.
            forward_timeout_seconds (int, optional): Defaults to 0.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/hunt-groups"

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["serviceUserId"] = service_user_id
        payload["policy"] = policy
        payload["noAnswerNumberOfRings"] = no_answer_number_of_rings
        payload["forwardTimeoutSeconds"] = forward_timeout_seconds

        if agents:
            payload["agents"] = [{"userId": agent} for agent in agents]

        if "serviceInstanceProfile" not in payload:
            payload.setdefault("serviceInstanceProfile", {})

        payload["serviceInstanceProfile"]["callingLineIdFirstName"] = clid_first_name
        payload["serviceInstanceProfile"]["callingLineIdLastName"] = clid_last_name
        payload["serviceInstanceProfile"]["name"] = (
            f"{clid_first_name} {clid_last_name}"
        )
        payload["serviceInstanceProfile"]["extension"] = extension

        return self._requester.post(endpoint, data=payload)

    def post_group_hunt_groups_remove_user(
        self, service_provider_id: str, group_id: str, user_id: str
    ):
        """Removes the specified user from all hunt groups in which it currently exists.

        Args:
            service_provider_id (str): The service provider ID in which the target user exists.
            group_id (str): The group ID where the user exists.
            user_id (str): The User ID of the user that is to be removed from the hunt group(s).

        Returns:
            List: Service user ID's (str) of the hunt groups from which the specified user has been removed.
        """

        endpoint = "/groups/hunt-groups/removeUser"

        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "userId": user_id,
        }

        return self._requester.post(endpoint, data=data)

    # PUT

    def put_group_hunt_groups_status(self, service_user_ids: list, status: bool = True):
        """Updates a list of Hunt Groups (HG) status to either active or inactive.

        Args:
            service_user_ids (list): List of service user IDs of target HGs.
            status (bool, optional): Status to apply to target HGs. Defaults to True.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/hunt-groups/status"

        data = {
            "instances": [
                {"serviceUserId": service_user_id, "isActive": status}
                for service_user_id in service_user_ids
            ]
        }

        return self._requester.put(endpoint, data=data)

    def put_group_hunt_group(
        self,
        service_provider_id: str,
        group_id: str,
        service_user_id: str,
        updates: dict,
    ):
        """Update a Hunt Group's (HG) settings.

        Args:
            service_provider_id (str): Service provider ID of where the group that hosts the HG is located.
            group_id (str): Group ID of where the HG is located.
            service_user_id (str): Target service user ID of the HG.
            updates (dict): Updates to be applied to HG.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/hunt-groups"

        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["serviceUserId"] = service_user_id
        if not updates.get("serviceInstanceProfile"):
            updates["serviceInstanceProfile"] = {}

        return self._requester.put(endpoint, data=updates)

    def put_group_hunt_group_weighted_call_distribution(
        self, service_provider_id: str, group_id, service_user_id: str, agents: list
    ):
        """Update the Weighted Call Distribution (WCD) between users in a Hunt Group (HG).

        Args:
            service_provider_id (str): Service provider ID where the group is located.
            group_id (_type_): Group ID where the HG is located.
            service_user_id (str): Service user ID of the target HG.
            agents (list): Updates of WCD to be applied to HG.

        Raises:
            AOInvalidWeighting: The WCD must equal 100 if it does not this error will be returned.

        Returns:
            None: This method does not return any specific value.
        """
        from ..exceptions import OSInvalidWeighting

        endpoint = "/groups/hunt-groups/weighted-call-distribution"

        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "serviceUserId": service_user_id,
            "agents": agents,
        }

        max_weights = 100
        assigned_weight = 0

        for agent in agents:
            assigned_weight += agent["weight"]
        if not assigned_weight == max_weights:
            raise OSInvalidWeighting

        return self._requester.put(endpoint, data=data)

    # DELETE

    def delete_group_hunt_group(self, service_user_id: str):
        """Deletes the specified hunt group.

        Args:
            service_user_id (str): The service user ID of the hunt group to be deleted.

        Returns:
            Dict: Profile of the deleted hunt group.

        """

        endpoint = "/groups/hunt-groups"

        params = {"serviceUserId": service_user_id}

        return self._requester.delete(endpoint, params=params)
