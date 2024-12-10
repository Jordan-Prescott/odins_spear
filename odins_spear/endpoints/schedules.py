from .base_endpoint import BaseEndpoint


class Schedules(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_group_schedules(self, service_provider_id: str, group_id: str):
        """Retrieves the Business Schedules for the specified group.

        Args:
            service_provider_id (str): Target Service Provider ID where group is hosted.
            group_id (str): Target Group ID with schedules.

        Returns:
            List: List of all the groups schedules, including Name, Type and Level.
        """

        endpoint = "/groups/schedules"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    def get_group_events(
        self, service_provider_id: str, group_id: str, name: str, type: str
    ):
        """Retrieves the Business Schedule's Events for the specified group.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID
            name (str): Name of the target Busisness Schedule
            type (str): The type of the Business Schedule (Time, Holiday)

        Returns:
            List: List of each Business Schedule Event, including startTime and endTime.
        """

        endpoint = "/groups/events"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "name": name,
            "type": type,
        }

        return self._requester.get(endpoint, params=params)


# POST

# PUT

# DELETE
