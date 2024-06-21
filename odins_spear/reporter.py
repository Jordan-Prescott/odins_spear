from . import reports

class Reporter:
    """ generates human friendly reports.
    """
    
    def __init__(self, api) -> None:
        self.api = api
        
        
    def call_flow(self, service_provider_id: str, group_id: str, number: str, number_type: str,
                  broadworks_entity_type: str):
        """Generates a graphical flow chart of how a call to a specified number routes 
        through the broadworks system.

        Args:
            service_provider_id (str): Service Provider/ Enterprise where group is hosted.
            group_id (str): Group ID where target number for call flow is located. 
            number (str): Target number for call flow. 
            number_type (str): Type of number, options: "dn": Direct Number, "extension": Extension, "alias": Alias
            broadworks_entity_type (str): Broadworks entity type target number is associated with. \
            Options: "auto_attendant": Auto Attendant, "call_center": Call Center, "hunt_group": Hunt Group, "user": User
        """
        
        return reports.call_flow.main(self.api, service_provider_id, group_id, number, number_type,
                                      broadworks_entity_type)
        
    def group_users_call_statistics(self, service_provider_id: str, group_id: str, 
                                    start_date:str, end_date: str = None, 
                                    start_time: str = "00:00:00", end_time:str = "23:59:59", 
                                    time_zone: str = "Z"):
        """Generates a CSV deatiling each users incoming and outgoing call statistics over 
        a specified period for a single group. Each row contains user extension, user ID, and call stats.

        Args:
            service_provider_id (str):  Service Provider/ Enterprise where group is hosted.
            group_id (str): Target Group you would like to know user statistics for.
            start_date (str): Start date of desired time period. Date must follow format 'YYYY-MM-DD'
            end_date (str, optional): End date of desired time period. Date must follow format 'YYYY-MM-DD'.\
                If this date is the same as Start date you do not need this parameter. Defaults to None.
            start_time (_type_, optional): Start time of desired time period. Time must follow formate 'HH:MM:SS'. \
                If you do not need to filter by time and want the whole day leave this parameter. Defaults to "00:00:00". MAX Request is 3 months.
            end_time (_type_, optional): End time of desired time period. Time must follow formate 'HH:MM:SS'. \
                If you do not need to filter by time and want the whole day leave this parameter. Defaults to "23:59:59". MAX Request is 3 months.
            time_zone (str, optional): A specified time you would like to see call records in. \
                Time zone must follow format 'GMT', 'EST', 'PST'. Defaults to "Z" (UTC Time Zone).
        """
        return reports.group_users_call_statistics.main(self.api, service_provider_id, group_id, 
                                                        start_date, end_date, start_time, end_time, time_zone)
      
    