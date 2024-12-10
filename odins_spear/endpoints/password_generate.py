from .base_endpoint import BaseEndpoint


class PasswordGenerate(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_password_generate(self, service_provider_id: str, group_id: str) -> dict:
        """Generates a single passwords following the groups rules.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate password for.

        Returns:
            dict: Single password generated according to the groups rules.
        """

        endpoint = "/password/generate"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    def get_passwords_generate(
        self, service_provider_id: str, group_id: str, limit: int = 10
    ) -> dict:
        """Generates a multiple passwords to the limit set in pararmeters.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate password for.
            limit (int, optional): Number of passwords api will return. Defaults to 10.

        Returns:
            dict: Multiple passwords generated according to the groups rules.
        """

        endpoint = "/password/generate"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "limit": limit,
        }

        return self._requester.get(endpoint, params=params)

    def get_passcode_generate(self, service_provider_id: str, group_id: str) -> dict:
        """Generates a single passcode following group rules.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate passcode for.

        Returns:
            dict: Single passcode generated according to the groups rules.
        """

        endpoint = "/passcode/generate"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    def get_passcodes_generate(
        self, service_provider_id: str, group_id: str, limit: int = 10
    ) -> dict:
        """Generates a multiple passcodes to the limit set in pararmeters.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate passcodes for.
            limit (int, optional): Number of passwords api will return. Defaults to 10.

        Returns:
            dict: Multiple passcodes generated according to the groups rules.
        """

        endpoint = "/passcode/generate"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "limit": limit,
        }

        return self._requester.get(endpoint, params=params)

    def get_sip_password_generate(self) -> dict:
        """Generates a single SIP password.

        Args:
            service_provider_id (str): Service Provider ID where Group is located.
            group_id (str): Group ID to generate SIP password for.

        Returns:
            dict: Single SIP password generated according to the groups rules.
        """

        endpoint = "/sip-password/generate"

        return self._requester.get(endpoint)

    def get_sip_passwords_generate(self, limit: int = 10) -> dict:
        """Generates multiple SIP passwords to the limit set in parameters. Defaults to 10.

        Args:
            limit (int, optional): Number of passwords api will return. Defaults to 10.

        Returns:
            dict: Mutliple SIP passwords generated according to the groups rules.
        """

        endpoint = "/password/generate"

        params = {"limit": limit}

        return self._requester.get(endpoint, params=params)


# POST

# PUT

# DELETE
