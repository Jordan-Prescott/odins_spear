from .base_endpoint import BaseEndpoint


class SharedCallAppearance(BaseEndpoint):
    def __init__(self):
        super().__init__()

# GET

# POST

def post_user_shared_call_appearance_endpoint(
        self, user_id: str, line_port: str, device_name: str
    ):
        """Creates a new Shared Call Apprance (SCA) on a single user.

        Args:
            user_id (str): Target user id of user to create SCA on.
            line_port (str): Line port to be assigned to the new SCA.
            device_name (_type_): Device to add for SCA from available devices.

        Returns:
            dict: New SCA details applied to user.
        """

        endpoint = "/users/shared-call-appearance/endpoints"

        data = {
            "userId": user_id,
            "linePort": line_port,
            "isActive": True,
            "allowOrigination": True,
            "allowTermination": True,
            "deviceName": device_name,
            "deviceLevel": "Group",
        }

        return self._requester.post(endpoint, data=data)

# PUT

# DELETE
