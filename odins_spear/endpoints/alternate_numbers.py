from .base_endpoint import BaseEndpoint


class AlternateNumbers(BaseEndpoint):
    def __init__(self):
        super().__init__()


# GET


def get_user_alternate_numbers(self, user_id: str):
    """Fetches a list of a user/ service such as Auto Attendant, Hunt Group, or Call Centres
    alternate numebrs.

    Args:
        user_id (str): Target user/ service_user_id

    Returns:
        Dict: List of all alternate numbers assigned to the user/ service.
    """

    endpoint = "/users/alternate-numbers"

    params = {"userId": user_id}

    return self._requester.get(endpoint, params=params)


# POST

# PUT

# DELETE
