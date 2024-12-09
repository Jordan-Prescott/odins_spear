from .base_endpoint import BaseEndpoint


class AutoAttendants(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_auto_attendants(self, service_provider_id: str, group_id: str):
        """Returns a complete list of all Auto Attendants in a single group.

        Args:
            service_provider_id (str): Service Provider where Group is hosted.
            group_id (str): Target Group where Auto Attendants are hosted.

        Returns:
            List: List of Auto Attendants with basic info on them.
        """

        endpoint = "/groups/auto-attendants"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    def get_auto_attendant(self, service_user_id: str):
        """Returns detailed information of a single Auto Attendant.

        Args:
            service_user_id (str): User ID of target Auto Attendant.

        Returns:
            dict: Detailed information of target Auto Attendant.
        """

        endpoint = "/groups/auto-attendants"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_auto_attendant_user(
        self, service_provider_id: str, group_id: str, user_id: str
    ):
        """Returns detailed information about all Auto Attendants (AA) built in the same group as the specified user.

        Args:
            service_provider_id (str): Service Provider ID of the group where the user is built.
            group_id (str): Group ID of the group where the user is built.
            user_id (str): User ID of the user being queried.

        Returns:
           List: Returns a list of the AAs built in the group.
        """

        endpoint = "/groups/auto-attendants/user"

        params = {
            "userId": user_id,
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_auto_attendant_submenus(self, service_user_id: str):
        """Returns a list of the submenus of the specified Auto Attendant (AA). Works with Standard AAs only, basic AAs do not have submenus.

        Args:
            service_user_id (str): The service user ID of the AA

        Returns:
            List: Returns a list of the submenus associated with the AA.
        """

        endpoint = "/groups/auto-attendants/submenus"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_auto_attendant_submenu_usage(self, service_user_id: str, submenu_id: str):
        """Returns the type of the specified Auto Attendant (AA) submenu. NOTE: This method does not return any usage data.

        Args:
            service_user_id (str): The service user ID of the AA being queried.
            submenu_id (str): The submenu ID of the submenu being queried.

        Returns:
            List: Returns a list containing a single dict of the submenu.
        """

        endpoint = "/groups/auto-attendants/submenus/usage"

        params = {"serviceUserId": service_user_id, "submenuId": submenu_id}

        return self._requester.get(endpoint, params=params)

    # POST

    def post_auto_attendant(
        self,
        service_provider_id: str,
        group_id: str,
        service_user_id: str,
        aa_name: str,
        aa_type: str = "Basic",
        payload: dict = {},
    ):
        """Builds an Auto Attendant (AA) from the given payload.

        Args:
            service_provider_id (str): Service Provider ID of the group where the AA should be built.
            group_id (str): Group ID where the AA should be built.
            service_user_id (str): Service User ID of the AA (including the domain).
            aa_name (str): Name of the AA
            aa_type (str, optional): Type of AA: "Basic" or "Standard". Will default to "Basic". NOTE: The "Auto Attendant - Standard" service must be enabled on the group in order for the aa_type to be set to "Standard".
            payload (dict, optional): Additional AA configuration data.

        Returns:
            Dict: Returns the AA profile.
        """

        endpoint = "/groups/auto-attendants"

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["serviceUserId"] = service_user_id
        payload["serviceInstanceProfile"]["name"] = aa_name
        payload["type"] = aa_type

        default_payload_values = {
            "enableVideo": "false",
            "extensionDialingScope": "Group",
            "nameDialingScope": "Group",
            "nameDialingEntries": "LastName + FirstName",
            "firstDigitTimeoutSeconds": 1,
        }

        for key, default_value in default_payload_values.items():
            payload.setdefault(key, default_value)

        return self._requester.post(endpoint, data=payload)

    def post_auto_attendant_remove_user(
        self, service_provider_id: str, group_id: str, user_id: str
    ):
        """Returns a list of the available Auto Attendants (AAs) built in the same group as the specified user.

        Args:
            service_provider_id (str): Service Provider ID where the user is built.
            group_id (str): Group ID where the user is built.
            user_id (str): User ID of the user.

        Returns:
            List: List of the Service User IDs of the AAs in the group.
        """

        endpoint = "/groups/auto-attendants/removeUser"

        payload = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "userId": user_id,
        }

        return self._requester.post(endpoint, data=payload)

    def post_auto_attendant_submenu(
        self,
        service_user_id: str,
        submenu_id: str,
        announcement_selection: str = "Default",
        extension_dialing: bool = True,
    ):
        """Posts a new submenu to the specified Auto Attendant (AA).

        Args:
            service_user_id (str): Service User ID of the AA.
            submenu_id (str): ID of the submenu to be created.
            announcement_selection (str, optional): "Default" or "Personal". Defaults to "Default".
            extension_dialing (bool, optional): Whether Level Extension Dialing is enabled or not. Defaults to True.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/auto-attendants/submenus"

        payload = {
            "serviceUserId": service_user_id,
            "submenuId": submenu_id,
            "announcementSelection": announcement_selection,
            "enableLevelExtensionDialing": extension_dialing,
        }

        return self._requester.post(endpoint, data=payload)

    # PUT

    def put_auto_attendants_status(
        self, auto_attendant_user_ids: list, status: bool = True
    ):
        """Updates a list of auto attendants (AA) status to either active or inactive.

        Args:
            auto_attendant_user_ids (list): List of service user IDs (AA IDs), the status given
            will be applied to these.
            status (bool, optional): Boolean value of True (Activate) or False (Deactivate)
            which will be applied to list of AAs. Defaults to True.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/auto-attendants/status"

        data = {
            "instances": [
                {"serviceUserId": auto_attendant_user_id, "isActive": status}
                for auto_attendant_user_id in auto_attendant_user_ids
            ]
        }

        return self._requester.put(endpoint, data=data)

    def put_auto_attendant(
        self,
        service_provider_id: str,
        group_id,
        auto_attendant_user_id: str,
        updates: dict,
    ):
        """Updates a single target Auto Attendant.

        Note: Needs the service instance profile to use this method.

        Args:
            service_provider_id (str): Service Provider ID where Group is hosted.
            group_id (str): Group ID where target Auto Attendant is located.
            auto_attendant_user_id (str): Target Auto Attendant User ID.
            updates (dict): Updates to be applied to Auto Attendant.

        Returns:
            Dict: Updated version of the Auto Attendant with updates applied.
        """

        endpoint = "/groups/auto-attendants"

        if "serviceInstanceProfile" not in updates:
            updates.setdefault("serviceInstanceProfile", {})

        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["serviceUserId"] = auto_attendant_user_id

        return self._requester.put(endpoint, data=updates)

    def put_auto_attendant_submenu(
        self, auto_attendant_user_id: str, submenu_id: str, updates: dict
    ):
        """This method allows you to update the configuration of the submenus for your AAs

        Args:
            auto_attendant_user_id (str): Service user ID of your auto attendant.
            submenu_id (str): Service user ID of your submenu
            updates (dict): Updates your applying to your submenu.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/auto-attendants/submenus"

        updates["serviceUserId"] = (auto_attendant_user_id,)
        updates["submenuId"] = submenu_id

        return self.request.put(endpoint, data=updates)

    # DELETE

    def delete_auto_attendant(self, service_user_id: str):
        """Removes an Auto Attendant (AA) from a group.

        Args:
            service_user_id(str): The service user ID of the AA.

        Returns:
            Dict: Returns the profile of the deleted AA.
        """

        endpoint = "/groups/auto-attendants"

        params = {"serviceUserId": service_user_id}

        return self._requester.delete(endpoint, params=params)

    def delete_auto_attendant_submenu(self, service_user_id: str, submenu_id: str):
        """Removes an Auto Attendant (AA) Submenu from the AA configuration. Submenus are only a feature of the 'Auto Attendant - Standard' service. These are not available on Basic AAs.

        Args:
            service_user_id(str): The service user ID of the AA.
            submenu_id (str): The ID of the Submenu to be removed from the AA.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/auto-attendants/submenus"

        params = {"serviceUserId": service_user_id, "submenuId": submenu_id}

        return self._requester.delete(endpoint, params=params)
