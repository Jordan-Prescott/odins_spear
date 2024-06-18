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
        """_summary_

        Args:
            service_provider_id (str): _description_
            group_id (str): _description_
            start_date (str): _description_
            end_date (str, optional): _description_. Defaults to None.
            start_time (_type_, optional): _description_. Defaults to "00:00:00".
            end_time (_type_, optional): _description_. Defaults to "23:59:59".
            time_zone (str, optional): _description_. Defaults to "Z".

        Returns:
            _type_: _description_
        """
        return reports.group_users_call_statistics.main(self.api, service_provider_id, group_id, 
                                                        start_date, end_date, start_time, end_time, time_zone)
      
    