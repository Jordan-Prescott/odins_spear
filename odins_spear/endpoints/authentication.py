from .base_endpoint import BaseEndpoint


class Authentication(BaseEndpoint):
    def __init__(self):
        super().__init__()


# GET

# POST

# PUT


def put_user_authentication_service(self, user_id: str, new_password: str):
    """Set new SIP Authentication password for a single user.

    Args:
        user_id (str): Target user ID to reset the SIP authentication password.
        new_password (str): New SIP authentication password to apply to new user.

    Returns:
        None: This method does not return any specific value.
    """

    endpoint = "/users/authentication"

    data = {"userId": user_id, "newPassword": new_password}

    return self._requester.put(endpoint, data=data)


def put_user_web_authentication_password(self, user_id: str, new_password: str):
    """Set new Web Authentication password for a single user.

    Args:
        user_id (str): Target user ID to reset the web authentication password.
        new_password (str): New web authentication password to apply to new user.

    Returns:
        None: This method does not return any specific value.
    """

    endpoint = "/users/passwords"

    data = {"userId": user_id, "newPassword": new_password}

    return self._requester.put(endpoint, data=data)


# DELETE
