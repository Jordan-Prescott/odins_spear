from .base_endpoint import BaseEndpoint


class Devices(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    # POST
    def post_group_device(
        self,
        service_provider_id: str,
        group_id: str,
        device_name: str,
        device_type: str,
        payload: dict = {},
    ):
        """Adds a new device to a group.

        Args:
            service_provider_id (str): Service provider ID where the device should be built.
            group_id (str): Group ID where the device should be built
            device_name (str): Name of the new device
            device_type (str): Type of device.
            payload (dict, optional): Device configuration data.

        Returns:
            Dict: Returns the device profile.
        """

        endpoint = "/groups/devices"

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["deviceName"] = device_name
        payload["deviceType"] = device_type

        return self._requester.post(endpoint, data=payload)

    # PUT
    def put_group_devices(
        self, service_provider_id: str, group_id: str, device_name: str, updates: dict
    ):
        """Update a single device in a group.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """

        endpoint = "/groups/devices"

        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["deviceName"] = device_name

        return self._requester.put(endpoint, data=updates)

    def put_service_provider_device(
        self, service_provider_id: str, device_name: str, updates: dict
    ):
        """Update a single device in a Service Provider or Enterprise.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where device is located.
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """

        endpoint = "/service-providers/devices"

        updates["serviceProviderId"] = service_provider_id
        updates["deviceName"] = device_name

        return self._requester.put(endpoint, data=updates)

    def put_system_devices(self, device_name: str, updates: dict):
        """Update a single device in the Broadworks system.

        Args:
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """

        endpoint = "/service-providers/devices"

        updates["deviceName"] = device_name

        return self._requester.put(endpoint, data=updates)

    def put_system_device_file(self, device_name: str, updates: dict):
        """Update a config file for a single device at the system level.

        Args:
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/system/devices/files"

        updates["deviceName"] = device_name

        return self._requester.put(endpoint, data=updates)

    def put_service_provider_device_file(self, device_name: str, updates: dict):
        """Update a config file for a single device at Service Provider or
        Enterprise level.

        Args:
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/service_provider/devices/files"

        updates["deviceName"] = device_name

        return self._requester.put(endpoint, data=updates)

    def put_group_device_file(self, device_name: str, updates: dict):
        """Update a config file for a single device at Group level.

        Args:
            device_name (str): Device name of the target device.
            updates (dict): Updates to apply to the target device.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/devices/files"

        updates["deviceName"] = device_name

        return self._requester.put(endpoint, data=updates)

    def put_group_device_tags_profile(
        self, service_provider_id: str, group_id: str, device_name: str, tags: list
    ):
        """Update tags assigned to single device at group level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_name (str): Device name of the target device.
            tags (dict): List of dictionaries tag name and value entries.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """

        endpoint = "/groups/devices/profile"

        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name,
            "tags": [{"elements": tags}],
        }

        return self._requester.put(endpoint, data=data)

    def put_group_device_tag(
        self,
        service_provider_id: str,
        group_id: str,
        device_name: str,
        tag_name: str,
        tag_value: str,
    ):
        """Update a single tag assigned to a device at group level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_name (str): Device name of the target device.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """

        endpoint = "/groups/devices/tags"

        data = {
            "tagName": f"%{tag_name}%",
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name,
        }

        return self._requester.put(endpoint, data=data)

    def put_service_provider_device_tag(
        self, service_provider_id: str, device_name: str, tag_name: str, tag_value: str
    ):
        """Update a single tag assigned to a device at the Service Provider or Enterprise level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            device_name (str): Device name of the target device.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """

        endpoint = "/service-providers/devices/tags"

        data = {
            "tagName": f"%{tag_name}%",
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "deviceName": device_name,
        }

        return self._requester.put(endpoint, data=data)

    def put_system_device_tag(self, device_name: str, tag_name: str, tag_value: str):
        """Update a single tag assigned to a device at the System level.

        Args:
            device_name (str): Device name of the target device.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """

        endpoint = "/system/devices/tags"

        data = {
            "tagName": f"%{tag_name}%",
            "tagValue": tag_value,
            "deviceName": device_name,
        }

        return self._requester.put(endpoint, data=data)

    def put_group_device_type_file(
        self, service_provider_id: str, group_id: str, device_type: str, updates: dict
    ):
        """Set config file for all devices of a specific type at the group level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_type (str): The device type you would like to apply the changes to.
            updates (dict): Cupdates (dict): Updates to apply to the target device.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/device-types/files"

        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["deviceType"] = device_type

        return self._requester.put(endpoint, data=updates)

    def put_group_device_type_tag(
        self,
        service_provider_id: str,
        group_id: str,
        device_type: str,
        tag_name: str,
        tag_value: str,
    ):
        """Update tags applied to device types at the Group level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            group_id (str): Group ID where target device is located.
            device_type (str): The target device type to apply the updates.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """

        endpoint = "/groups/system/device-types/tags"

        data = {
            "tagName": tag_name,
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceType": device_type,
        }

        return self._requester.put(endpoint, data=data)

    def put_service_provider_device_type_tag(
        self, service_provider_id: str, device_type: str, tag_name: str, tag_value: str
    ):
        """Update tags applied to device types at the Service Provider or Enterprise level.

        Args:
            service_provider_id (str): Service Provider or Enterprise ID where Group is located.
            device_type (str): The target device type to apply the updates.
            tag_name (str): Name of the tag to add or update.
            tag_value (str): Value of tag to add or update.

        Returns:
            Dict: Python dictionary of the new state after updates have been applied.
        """

        endpoint = "/service-providers/device-types/tags"

        data = {
            "tagName": tag_name,
            "tagValue": tag_value,
            "serviceProviderId": service_provider_id,
            "deviceType": device_type,
        }

        return self._requester.put(endpoint, data=data)


# DELETE
