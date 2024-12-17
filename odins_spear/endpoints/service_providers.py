from .base_endpoint import BaseEndpoint


class ServiceProviders(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_service_providers(self, reseller_id: str = None):
        """
        Fetches list of service providers.

        Args:
            reseller_id (str): Only list the Service Provider IDs within the specified Reseller.

        Returns:
            dict: A dictionary containing the response from the

        """
        endpoint = "/service-providers"
        params = {"resellerId": reseller_id}

        return self._requester.get(endpoint, params=params)

    def get_service_provider(self, service_provider_id: str):
        """
        Fetches a service provider by ID with further details.

        Args:
            reseller_id (str): Only list the Service Provider IDs within the specified Reseller.

        Returns:
            dict: Dictionary of details for the service provider.
        """

        endpoint = "/service-providers"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)


# POST

# PUT

# DELETE
