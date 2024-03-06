from . import reports

class Reporter:
    """ generates human friendly reports.
    """
    
    def __init__(self, api) -> None:
        self.api = api
        
        
    def call_flow(self, service_provider_id: str, group_id: str, number: int, number_type: str,
                  broadworks_entity_type: str):
        """Generates a graphical flow chart of how a call to a specified number routes 
        through the broadworks system.

        Args:
            service_provider_id (str): Service Provider/ Enterprise where group is hosted.
            group_id (str): Group ID where target number for call flow is located. 
            number (int): Target number for call flow. 
            number_type (str): Type of number, options: DN, Extension, Alias
            broadworks_entity_type (str): Broadworks entity type target number is associated with. 
                Options: Auto Attendant, Call Centre, Hunt Group, User
        """
        
        return reports.call_flow(self.api, service_provider_id, group_id, number)
      
    