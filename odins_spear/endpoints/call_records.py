from .base_endpoint import BaseEndpoint


class CallRecords(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET
    def get_users_stats(
        self,
        user_id: str,
        start_date: str,
        end_date: str = None,
        start_time: str = "00:00:00",
        end_time: str = "23:59:59",
        time_zone: str = "Z",
    ):
        """Pulls a single users call statistics for a specified period of time. 

        Args:
            user_id (str): Target user ID you would like to pull call statistics for.
            start_date (str): Start date of desired time period. Date must follow format 'YYYY-MM-DD'
            end_date (str, optional): End date of desired time period. Date must follow format 'YYYY-MM-DD'.\
                If this date is the same as Start date you do not need this parameter. Defaults to None.
            start_time (_type_, optional): Start time of desired time period. Time must follow formate 'HH:MM:SS'. \
                If you do not need to filter by time and want the whole day leave this parameter. Defaults to "00:00:00". MAX Request is 3 months.
            end_time (_type_, optional): End time of desired time period. Time must follow formate 'HH:MM:SS'. \
                If you do not need to filter by time and want the whole day leave this parameter. Defaults to "23:59:59". MAX Request is 3 months.
            time_zone (str, optional): A specified time you would like to see call records in. \
                Time zone must follow format 'GMT', 'EST', 'PST'. Defaults to "Z" (UTC Time Zone).

        Returns:
            Dict: Users call record statistics for specified time period.
        """

        # checks if end_date has been left and therefore we assume user wants same date.
        if not end_date:
            end_date = start_date

        endpoint = "/users/call-records/stats"

        params = {
            "userIds": user_id,
            "startTime": f"{start_date}T{start_time}{time_zone}",
            "endTime": f"{end_date}T{end_time}{time_zone}",
        }

        return self._requester.get(endpoint, params=params)

    # POST
    # PUT
    # DELETE
