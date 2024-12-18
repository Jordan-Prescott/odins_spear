from .base_endpoint import BaseEndpoint


class Services(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_user_services_assigned(self, user_id: str):
        """

        Args:
            user_id (str): _description_
        """
        endpoint = "/users/services/assigned"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_services(self, user_id: str):
        """Fetch all services assigned to a broadwrok entity, this can be
        a user, AA, CC, or HG.

        Args:
            user_id (str): User ID of the target Broadworks entity.

        Returns:
            Dict: Broadwork entiy and a list of services assigned.
        """

        endpoint = "/users/services"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_service_settings(self, user_id: str):
        """Retrieves all service settings for a specific user.

        Args:
            user_id (str): ID of the target user

        Returns:
            Dict: A dictionary containing all the service settings for the specified user.
        """

        endpoint = "/users/services/settings"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_services(self, group_id: str, service_provider_id: str):
        """
        Fetch all userServices, groupServices and servicePackServices assigned to a group.

        Args:
            group_id (str): GroupID of the target
            service_provider_id (str): Service Provider or Enterprise ID of the target.

        Returns:
            Dict: Authorised and assigned services within the group.
        """

        endpoint = "/groups/services"

        params = {"groupId": group_id, "serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_group_services_user_assigned(
        self,
        group_id: str,
        service_provider_id: str,
        service_name: str,
        service_type: str,
    ):
        """
        Get details of the user/service instances where a particular service is assigned.

        Args:
            group_id (str): GroupID being targeted
            service_provider_id (str): Service provider/Enterprise ID where the group is located.
            service_name (str): Name of the service querying
            service_type (str): Type of service. Either: serviceName or servicePackName

        Returns:
            Dict: Users/Service Instances where the service is assigned.
        """

        endpoint = "/groups/services/assigned"

        params = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id,
            "serviceType": service_type,
            "serviceName": service_name,
        }

        return self._requester.get(endpoint, params=params)

    # POST

    # PUT

    def put_user_services(
        self,
        user_id: str,
        services: list = None,
        service_packs: list = None,
        assigned: bool = True,
    ):
        """Update the services assigned to a user. NOT service/feature packs.

        Args:
            user_id (str): User ID of the target user.
            services (list): List of services to be applied to user.
            service_packs (list): List of service packs to be applied to user.
            assigned (bool, optional): Assign (True) or unassign(False). Defaults to True.

        Returns:
            Dict: User services assigned to the user.
        """

        endpoint = "/users/services"

        data = {"userId": user_id}

        if services:
            data["userServices"] = [
                {"serviceName": service, "assigned": assigned} for service in services
            ]
        if service_packs:
            data["servicePackServices"] = [
                {"serviceName": service_pack, "assigned": assigned}
                for service_pack in service_packs
            ]
        return self._requester.put(endpoint, data=data)

    def put_user_service_settings(self, user_id: str, settings: dict):
        """Updates specific service settings for a given user.
        This function allows you to modify one or more service settings associated with a particular user.

        Args:
            user_id (str): The ID of the target user
            settings (dict): A dictionary containing the new settings to be applied. The structure of this dictionary should mirror the API's expected format for updating service settings.

        Returns:
            Dict: A dictionary representing the updated service settings for the specified user.
        """

        endpoint = "/users/services/settings"

        data = {"userId": user_id, **settings}

        return self._requester.put(endpoint, data=data)


# DELETE
