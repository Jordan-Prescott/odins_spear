from typing import Optional

from . import reports
from .api import API


class Reporter:
    """generates human friendly reports."""

    __instance = None

    @staticmethod
    def get_instance(api: API):
        """Static method to fetch the current instance."""
        if Reporter.__instance is None:
            Reporter(api)
        return Reporter.__instance

    def __init__(self, api: API) -> None:
        if Reporter.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.api = api
            Reporter.__instance = self

    def _run_report(self, report_name: str, *args, **kwargs):
        """Run a report function from the reports module."""
        try:
            report_function = getattr(reports, report_name)
        except AttributeError:
            raise AttributeError(
                f"Report '{report_name}' not found in 'reports' module."
            )
        return report_function(self.api, *args, **kwargs)

    def call_flow(
        self,
        service_provider_id: str,
        group_id: str,
        number: str,
        number_type: str,
        broadworks_entity_type: str,
    ) -> bool:
        """Generates a graphical flow chart of how a call to a specified number routes 
        through the broadworks system.
        
        NOTE: Report will be saved in .os_reports/ folder as a .svg file.

        Args:
            service_provider_id (str): Service Provider/ Enterprise where group is hosted.
            group_id (str): Group ID where target number for call flow is located. 
            number (str): Target number for call flow. 
            number_type (str): Type of number, options: "dn": Direct Number, "extension": Extension, "alias": Alias
            broadworks_entity_type (str): Broadworks entity type target number is associated with. \
            Options: "auto_attendant": Auto Attendant, "call_center": Call Center, "hunt_group": Hunt Group, "user": User
            
        Returns: Boolean True if report was generated successfully.
        """

        return self._run_report(
            "call_flow",
            service_provider_id,
            group_id,
            number,
            number_type,
            broadworks_entity_type,
        )

    def group_users_call_statistics(
        self,
        service_provider_id: str,
        group_id: str,
        start_date: str,
        end_date: Optional[str] = None,
        start_time: str = "00:00:00",
        end_time: str = "23:59:59",
        time_zone: str = "Z",
    ) -> bool:
        """Generates a CSV deatiling each users incoming and outgoing call statistics over 
        a specified period for a single group. Each row contains user extension, user ID, and call stats.
        
        NOTE: Report will be saved in .os_reports/ folder as a .csv file.

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
                
        Returns: Boolean True if report was generated successfully.
        """
        return self._run_report(
            "group_users_call_statistics",
            service_provider_id,
            group_id,
            start_date,
            end_date,
            start_time,
            end_time,
            time_zone,
        )

    def user_registration_report(self, service_provider_id: str, group_id: str) -> bool:
        """Generates an Excel Worksheet detailing each Users ID, device name and registration status within a group.

        NOTE: Xlsx File into .os_reports/ named "Registration_report_for_(GroupID)"

        Args:
            service_provider_id (str):  Service Provider/ Enterprise where group is hosted.
            group_id (str): Target Group you would like to check the registration of.

        Returns: Boolean True if report was generated successfully.
        """
        return self._run_report(
            "user_registration_report", service_provider_id, group_id
        )
