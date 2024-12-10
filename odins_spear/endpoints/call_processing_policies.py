from .base_endpoint import BaseEndpoint


class CallProcessingPolicies(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    # POST

    # PUT

    def put_user_call_processing_policy(self, user_id: str, updates: dict):
        """
        Update the Call Processing Policies for a specified user.

        Args:
            user_id (str): The user ID of the user whose call processing policies need updating.
            updates (dict): Updates to apply to the specified user.

        Returns:
            Dict: Returns the updated call processing policies.
        """

        endpoint = "/users/call-processing-policy"

        updates["userId"] = user_id

        return self._requester.put(endpoint, data=updates)

    # DELETE
