from .base_endpoint import BaseEndpoint


class DoNotDisturb(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_user_do_not_disturb(self, user_id: str):
        """Returns the specificied users DND and Ring Splash state.

        Args:
            user_id (str): Target user id to return data.

        Returns:
            Dict: States DND and Ring Splash status.
        """

        endpoint = "/users/do-not-disturb"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    # POST

    # PUT

    def put_user_do_not_disturb(
        self, user_id: str, dnd_active: bool = False, ring_splash_active: bool = False
    ):
        """Updates a user's DND and Ring Splash status.

        Args:
            user_id (str): Target user id of user you would like to update the state of.
            dnd_active (bool): True to enable DND and False to disable DND. Defaults to False.
            ring_splash_active (bool): True to enable Ring Splash and False to disable Ring Splash. Defaults to False.

        Returns:
            Dict: New DND and Ringsplash state of the user.
        """

        data = {
            "isActive": dnd_active,
            "ringSplash": ring_splash_active,
            "userId": user_id,
        }

        endpoint = "/users/do-not-disturb"

        return self._requester.put(endpoint, data)

    # DELETE
