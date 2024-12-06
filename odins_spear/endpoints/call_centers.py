from .base_endpoint import BaseEndpoint


class CallCenters(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_group_call_centers(self, service_provider_id: str, group_id: str):
        """Retrieves a list of active call centers within a specified group, along with their settings.

        Args:
            service_provider_id (str): Target Service Provider where group is hosted
            group_id (str): Target Group ID

        Returns:
            List: List of Call Centers and their settings.
        """

        endpoint = "/groups/call-centers"
        params = {"serviceProviderId": service_provider_id, "groupId": group_id}
        return self._requester.get(endpoint, params=params)

    def get_group_call_center(self, service_user_id: str):
        """Retrieves deatiled information on a single Call Center.

        Args:
            service_user_id (str): Target Call Center's ID

        Returns:
            Dict: Target Call Centers details.
        """

        endpoint = "/groups/call-centers"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_center(self, user_id: str):
        """Retrieves a list of call centers that the specified user is currently associated with.

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Agents Call Centers setting and a list of the User's associated Call Centers.
        """

        endpoint = "/users/call-center"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_agents(self, service_user_id: str):
        """Returns list of agents assigned to the target call center.

        Args:
            service_user_id (str): Service user ID of target call center.

        Returns:
            Dict: List of agents assigned to call center
        """

        endpoint = "/groups/call-centers/agents"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_bounced_calls(self, service_user_id: str):
        """Retrieves the number of rings before a call is bounced from the specified call center.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Amount of Rings before a call is Bounced
        """

        endpoint = "/groups/call-centers/bounced-calls"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_forced_forwarding(self, service_user_id: str):
        """Retrieves the forwarding number for a call center if it is set to forward calls, along with any associated audio messages.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Number to be Forwarded to, alongside any Audio Messages.
        """

        endpoint = "/groups/call-centers/forced-forwarding"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_overflow(self, service_user_id):
        """Retrieves the forwarding number for a user when all call center agents are busy, along with any associated audio messages.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Dict: Call Centers overflow configuration.
        """

        endpoint = "/groups/call-centers/overflow"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_stranded_calls(self, service_user_id):
        """Retrieves the forwarding number for a user when a call center doesn't answer, along with any associated audio messages.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Call Centers stranded call configuration.
        """

        endpoint = "/groups/call-centers/stranded-calls"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_stranded_calls_unavailable(self, service_user_id):
        """Retrieves the forwarding number for a user when a call center doesn't answer, along with the count of agents with an unavailable code in the call center.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Number to be Forwarded to, and Agents with an Unavailable Code set.
        """

        endpoint = "/groups/call-centers/stranded-calls-unavailable"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    # POST

    # PUT
    def put_group_call_centers_status(
        self, call_center_user_ids: list, status: bool = True
    ):
        """Updates a list of call centers (CC) status to either active or inactive.

        Args:
            call_center_user_ids(list): List of service user IDs (CC IDs), the status given will be applied to these.
            status (bool): Boolean value of True (Activate) or False (Deactivate) which will be applied to list of AAs.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/status"

        data = {
            "instances": [
                {"serviceUserId": call_center_user_id, "isActive": status}
                for call_center_user_id in call_center_user_ids
            ]
        }

        return self._requester.put(endpoint, data=data)

    def put_group_call_center(self, call_center_user_id: str, updates: dict):
        """Allows you to update a specific call center.

        Args:
            call_center_user_id (str): Service user id of the target call center.
            updates (dict): Updates to apply in in a dictionary format.

        Returns:
            Dict: The call center with the new applied updates.
        """

        endpoint = "/groups/call-centers"

        updates["serviceUserId"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_agents(
        self, call_center_user_id: str, agent_user_ids: list
    ):
        """Add or remove agents to a call center.

        Note: Leave the agent_user_ids blank to remove all users and to remove some only include
        the users you would like to include in this call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.
            agent_user_ids (list): List of user IDs to be added to call center.

        Returns:
            Dict: Dictionary of the new state of the CC.
        """

        endpoint = "/groups/call-centers/agents"

        data = {
            "serviceUserId": call_center_user_id,
            "agents": [{"userId": agent_id} for agent_id in agent_user_ids],
        }

        return self._requester.put(endpoint, data=data)

    def put_group_call_center_agents_levels(
        self, call_center_user_id: str, agent_user_ids: list, skill_level: int
    ):
        """Update a list of agents skill level in a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the call center users belong to.
            agent_user_ids (list): List of the target users.
            skill_level (int): Skill level that will be applied to the list of users in the target call center.

        Returns:
            Dict: CC ID and list of the agent and their updated skill level.
        """

        endpoint = "/groups/call-centers/agents"

        data = {
            "serviceUserId": call_center_user_id,
            "agents": [
                {"userId": agent_id, "skillLevel": skill_level}
                for agent_id in agent_user_ids
            ],
        }

        return self._requester.put(endpoint, data=data)

    def put_group_call_center_bounced_calls(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the bounced call settings of a single Call Center (CC)

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/bounced-calls"

        updates["serviceUserId"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_dnis_instance(
        self, call_center_user_id: str, updates: dict
    ):
        """Update a DNIS instance of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/dnis/instances"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_forced_forwarding(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the forced forwarding settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/forced-forwarding"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_overflow(self, call_center_user_id: str, updates: dict):
        """Update the overflow settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/overflow"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_stranded_calls(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the stranded calls settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/stranded-calls"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_stranded_calls_unavailable(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the stranded calls unavailable settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/stranded-calls-unavailable"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_user_call_center_supervised_agents(
        self, call_center_user_id: str, supervisor_user_id: str, agent_ids: list
    ):
        """Update the list of agents a supervisor has in a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            supervisor_user_id (str): User ID of the supervisor.
            agent_ids (list): List of user IDs of agents to apply to supervisor.

        Returns:
            Dict: Superivor ID and list of agents they supervise.
        """

        endpoint = "/groups/call-centers/supervisors"

        data = {
            "serviceUserId": call_center_user_id,
            "supervisorUserId": supervisor_user_id,
            "supervisors": [{"userId": agent_id} for agent_id in agent_ids],
        }

        return self._requester.put(endpoint, data=data)

    def put_user_call_center(self, user_id: str, updates: dict):
        """Update an agent's status in a Call Center (CC).

        Args:
            user_id (str): User ID of the target user.
            updates (dict): Updates to be applied to the user.

        Returns:
            Dict: Agents ACD status and status in each CC they are assigned to.
        """

        endpoint = "/users/call-center"

        updates["userId"] = user_id

        return self._requester.put(endpoint, data=updates)

    def put_user_call_center_agents_update(
        self, user_id: str, call_center_service_ids: list
    ):
        """Update the Call Centers (CC) a user is assigned to.

        Args:
            user_id (str): User ID of the target user.
            call_center_service_ids (list): List of CC service user IDs to update the user with.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/user/call-centers/agents"

        data = {
            "agentUserId": user_id,
            "callCenters": [
                {"userId": call_center_id} for call_center_id in call_center_service_ids
            ],
        }

        return self._requester.put(endpoint, data=data)

    def put_user_call_center_agent_sign_out(self, user_id: str):
        """Sign the user out of their assigned Call Centers (CC).

        Args:
            user_id (str): User ID of the target user.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/user/call-centers/agents/sign-out"

        data = {
            "agentUserId": user_id,
        }

        return self._requester.put(endpoint, data=data)


# DELETE
