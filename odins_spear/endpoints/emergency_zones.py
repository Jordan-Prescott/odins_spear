from .base_endpoint import BaseEndpoint


class EmergencyZones(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    # POST
    def post_group_emergency_zones(
        self, service_provider_id: str, group_id: str, ip_addresses: list
    ):
        """Updates the IP address(es) for the Emergency Zone configured in the group.

        Args:
            service_provider_id (str): Service provider ID where the Emergency Zone to be updated exists.
            group_id (str): Group ID where the Emergency Zone to be updated exists.
            ip_addresses (list): A list of IP address ranges (dicts) to be added to the Emergency Zone. If the IP address to be applied is not a range, the min and max values should be the same.

        Returns:
            Dict: Emergency Zone profile with updated IP addresses.
        """

        endpoint = "/groups/emergency-zones"

        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "ipAddresses": ip_addresses,
        }

        return self._requester.post(endpoint, data=data)

    # PUT
    def put_group_emergency_zones(
        self,
        service_provider_id: str,
        group_id: str,
        is_active: bool = True,
        zone_rules: str = None,
        emergency_notification_email: str = None,
        ip_addresses: list = None,
    ):
        """Updates the Emergency Zone configuration in the group.

        Args:
            service_provider_id (str): Service provider ID where the Emergency Zone to be updated exists.
            group_id (str): Group ID where the Emergency Zone to be updated exists.
            is_active (bool, optional): Whether the Emergency Zone service is active or not. Defaults to True
            zone_rules (str, optional): The rules of the Emergency Zone. This will either be "Prohibit all registrations and call originations" or "Prohibit emergency call originations".
            emergency_notification_email (str, optional): The email address where emergency call notifications should be sent.
            ip_addresses (list, optional): A list of IP address ranges (dicts) to be added to the Emergency Zone. If the IP address to be applied is not a range, the min and max values should be the same.

        Returns:
            Dict: Updated Emergency Zone configuration.
        """

        endpoint = "/groups/emergency-zones"

        data = {"groupId": group_id, "serviceProviderId": service_provider_id}

        if is_active:
            data["isActive"] = is_active
        if zone_rules:
            data["emergencyZonesProhibition"] = zone_rules
        if emergency_notification_email:
            data["sendEmergencyCallNotifyEmail"] = True
            data["emergencyCallNotifyEmailAddress"] = emergency_notification_email
        if ip_addresses:
            data["ipAddresses"] = ip_addresses

        return self._requester.put(endpoint, data)

    # DELETE
