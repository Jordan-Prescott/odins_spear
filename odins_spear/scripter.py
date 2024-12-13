from typing import Dict, Any, Optional

from . import scripts

from .api import API


class Scripter:
    """This object acts as the gateway to all pre-written scripts in /scripts/.


    Each api object created creates its own associated Scripter object on api creation.
    Additionally, this object can be created solely and passed an api, however, this
    will result in two exact Scripter objects.

    Intended use: odin_api.scripter.{script function}

    :param api: api object in package odin_api, this is used in the scripts to achieve objective.
    """

    __instance = None

    @staticmethod
    def get_instance(api: API = None) -> "Scripter":
        """
        Singleton implementation for Scripter object.

        Args:
            api (API): API object to be used in the scripts.

        Returns:
            Scripter: Scripter object.
        """
        if Scripter.__instance is None:
            Scripter(api)
        return Scripter.__instance

    def __init__(
        self,
        api: API,
    ) -> None:
        if Scripter.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.api = api
            Scripter.__instance = self

    def _run_script(self, script_name: str, *args, **kwargs) -> Dict[str, Any]:
        """
        Dynamically runs the specified script.

        Args:
            script_name (str): Name of the script to run.
            *args: Positional arguments for the script.
            **kwargs: Keyword arguments for the script.

        Returns:
            Dict[str, Any]: Output of the script.

        Raises:
            AttributeError: If the script is not found in the `scripts` module.
        """
        try:
            script_function = getattr(scripts, script_name)
        except AttributeError:
            raise AttributeError(
                f"Script '{script_name}' not found in 'scripts' module."
            )
        return script_function(self.api, *args, **kwargs)

    def aa_cc_hg_audit(self, service_provider_id: str, group_id: str) -> Dict[str, Any]:
        """
            This script returns the services assigned to Auto Attendants,
            Call Centres, and Hunt Groups. Only services are applied to these
            entities and there are scenarios one would need to focus services
            assigned to these entities.

        Args:
            service_provider_id: Service Provider ID or Enterprise ID containing the Group ID.
            group_id: Group ID to generate the report for.

        Returns:
            Dict: Formatted report of service packs assigned to AA, CC, and HG.
        """
        return self._run_script("aa_cc_hg_audit", service_provider_id, group_id)

    def bulk_password_reset(
        self, service_provider_id: str, group_id: str, users: list, password_type: str
    ) -> Dict[str, any]:
        """Resets a list of users SIP passwords or Voicemail passcodes. Specify in password_type with the options of
        'SIP' or 'Voicemail' and the script will perform the necessary actions.

        Args:
            service_provider_id (str): Service Provider ID where group is hosted.
            group_id (str): Group ID where target users are located.
            users (list): List of User IDs of the target users to reset the password.
            password_type (str): Type of password to reset either 'SIP' or 'Voicemail'. Only accepts these two options.

        Raises:
            OSInvalidPasswordType: Only valid password options are SIP, VM, WEB. If another is requested this will be raised.

        Returns:
            Dict: Users and their new passwords.
        """
        return self._run_script(
            "bulk_password_reset", service_provider_id, group_id, users, password_type
        )

    def find_alias(
        self, service_provider_id: str, group_id: str, alias: str
    ) -> Dict[str, any]:
        """Locates alias if assigned to broadworks entity.

        Args:
            service_provider_id (str): Service Prodiver where group is hosted.
            group_id (str): Group where alias is located.
            alias (int): Alias number to identify e.g. 0

        Raises:
             AOALiasNotFound: If alias not found AOAliasNotFound error raised

        Returns:
            Dict: Returns type and name/ userId of entity where alias located.

        """
        return self._run_script("find_alias", service_provider_id, group_id, alias)

    def group_audit(self, service_provider_id: str, group_id: str) -> Dict[str, any]:
        """
        Produces a report of key information within the group.
        Reports on DN usage, Service and Service pack usage, Trunking call capacity and group info.

        Args:
            service_provider_id (str): Service Provider ID or Enterprise ID containing the Group ID.
            group_id (str): Group ID to generate the report for.

        Returns:
            Dict: Formatted report of the group.
        """
        return self._run_script("group_audit", service_provider_id, group_id)

    def locate_free_extension(
        self, service_provider_id: str, group_id: str, range_start: int, range_end: int
    ) -> Dict[str, any]:
        """Locates the lowest value free extension given the provided range of extension numbers.

        Raises: OSExtensionNotFound: Raises when a free extension is not located within the passed range.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located which hosts needed free extensions
            group_id (str): Group ID where target extensions are located.
            range_start (int): integral value specifying the starting range for free extensions
            range_end (int): integral value specifying the ending range for free extensions

        Returns:
            Dict: Data of the free extension {extension: "1000"}
        """
        return self._run_script(
            "locate_free_extension",
            service_provider_id,
            group_id,
            range_start,
            range_end,
        )

    def move_numbers(
        self,
        current_service_provider_id: str,
        current_group_id: str,
        target_service_provider_id: str,
        target_group_id: str,
        start_of_range_number: str,
        end_of_range_number: Optional[str] = None,
    ) -> bool:
        """Moves a list of numbers from existing group to another group on the same broadworks instance.
        This can move numbers between Service Provider/ Enterprise and groups in the same Service Provider/ Enterprise.

        Note: Numbers need to be strings and follow this format: +{country code}-{number}.

        Args:
            current_service_provider_id (str): Current Service Provider/ Enterprise where numbers are located.
            current_group_id (str): Current Group ID where numbers are located.
            target_service_provider_id (str): Target Service Provider/ Enterprise to move the numbers to.
            target_group_id (str): Target Group to move numbers to.
            start_of_number_range (str): Starting number in range of numbers you would like to move.
            end_of_number_range (str): Ending nummber in range of numbers you would like to move. If you need to move
            only one number do not enter a value for this paramter. Defaults to None.

        Returns:
            Bool: Returns a True once complete.
        """
        return self._run_script(
            "move_numbers",
            current_service_provider_id,
            current_group_id,
            target_service_provider_id,
            target_group_id,
            start_of_range_number,
            end_of_range_number,
        )

    def remove_numbers(
        self,
        service_provider_id: str,
        group_id: str,
        start_of_range_number: str,
        end_of_range_number: Optional[str] = None,
    ) -> bool:
        """Removes a singular or range of numbers from the entire Broadworks instance.

        Note: Numbers need to be strings and follow this format: +{country code}-{number}.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located which hosts target numbers.
            group_id (str): Group ID where target numbers are located.
            start_of_number_range (str): Starting number in range of numbers you would like to remove.
            end_of_number_range (str): Ending nummber in range of numbers you would like to remove. If you need to remove
            only one number do not enter a value for this paramter. Defaults to None.

        Returns:
            Bool: Returns a True once complete.
        """
        return self._run_script(
            "remove_numbers",
            service_provider_id,
            group_id,
            start_of_range_number,
            end_of_range_number,
        )

    def service_pack_audit(self, service_provider_id, group_id) -> Dict[str, any]:
        """
        A stripped down version of group audit focussing only on the service packs assigned within
        the group. This only shows the service packs assigned and total count of unlike group audit
        which details the users this is assigned to.

        Args:
            service_provider_id (str): Service Provider ID or Enterprise ID containing the Group ID.
            group_id (str): Group ID to generate the report for.

        Returns:
            Dict: Formatted report of service packs assigned in the group.
        """
        return self._run_script("service_pack_audit", service_provider_id, group_id)

    def service_provider_trunking_capacity(
        self, service_provider_id: str
    ) -> Dict[str, any]:
        """Returns a JSON breakdown of the Trunking Call Capacity of a Service Provider/ Enterprise (SP/ENT). 
        This will show the totals at each level from SP/ ENT to Group to Trunk Groups located in Groups. 
        At each level Max Active Calls and Bursting Max Active calls are detailed and then differences at 
        calculated.
        
        Raises: 
            OSServiceNotAssigned: Raises when the SP/ Ent does not have the service 'Trunk Group' assigned. 

        Args:
            service_provider_id (str): Target Service Provider ID/ Enterprise ID that you would like the \
                Trunk Call Capacity breakdown.

        Returns:
            Dict: Data of Trunking Call Capacity details of SP/ ENT, Groups, and Trunk Groups.
        """
        return self._run_script(
            "service_provider_trunking_capacity", service_provider_id
        )

    def user_association(
        self, service_provider_id: str, group_id: str, user_id: str
    ) -> Dict[str, any]:
        """
        Identify a user's associations with Call Centers (CC), Hunt Groups (HG),
        and Pick Up Groups.

        Args:
            service_provider_id (str): Service Provider where the group is hosted.
            group_id (str): Group where the User is located.
            user_id (str): Target user ID.

        Returns:
            Dict: Formatted output of the user showing all CC, HG, and Pick Up user is assigned to.
        """
        self._run_script("user_association", service_provider_id, group_id, user_id)

    def user_registration(
        self, service_provider_id: str, group_id: str
    ) -> Dict[str, any]:
        """Generates a dictionary detailing each Users ID, device name and registration status within a group.

        Args:
            service_provider_id (str):  Service Provider/ Enterprise where group is hosted.
            group_id (str): Target Group you would like to know user statistics for.

        Returns:
            Dict: User's ID, Device Name, and Registration status.
        """
        return self._run_script("user_registration", service_provider_id, group_id)

    def webex_builder(
        self,
        service_provider_id: str,
        group_id: str,
        user_id: str,
        device_type: str,
        email: str,
        primary_device: bool = True,
        webex_feature_pack_name: Optional[str] = None,
        enable_integrated_imp: bool = True,
    ) -> Dict[str, any]:
        """Builds a Webex device and assigns to user either as the primary device or a
        Shared Call Appearance.

        Args:
            service_provider_id (str): Service Provider ID where group is hosted.
            group_id (str): Group ID where target user is hosted.
            user_id (str): Target user to build and add webex device.
            device_type (str): Name of the device profile to apply.
            email (str): Email of user. This will be used to sign into the webex client.
            primary_device (bool, optional): Setting to False will assign as SCA, True is primary. Defaults to True.
            webex_feature_pack_name (str, optional): Feature pack to assign for Webex services. Defaults to None.
            enable_integrated_imp (bool, optional): Enables Integrated IMP service for the user if True .Defaults to True.

        Returns:
            Dict: Webex user/ device details. Includes webex client username and password, and if primary device
            device type set.

        Raises:
            OSLicenseNonExistent: Raised if user does not have correct license which allows for SCA devices.
        """

        return self._run_script(
            "webex_builder",
            service_provider_id,
            group_id,
            user_id,
            device_type,
            email,
            primary_device,
            webex_feature_pack_name,
            enable_integrated_imp,
        )
