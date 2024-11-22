from . import scripts


class Scripter:
    """ This object acts as the gateway to all pre-written scripts in /scripts/.
    

    Each api object created creates its own associated Scripter object on api creation. 
    Additionally, this object can be created solely and passed an api, however, this 
    will result in two exact Scripter objects.

    Intended use: odin_api.scripter.{script function}

    :param api: api object in package odin_api, this is used in the scripts to achieve objective.
    """

    def __init__(self, api) -> None:
        self.api = api

    def aa_cc_hg_audit(self, service_provider_id: str, group_id: str):
        """
            This script returns the services assigned to Auto Attendants, 
            Call Centres, and Hunt Groups. Only services are applied to these 
            entities and there are scenarios one would need to focus services 
            assigned to these entities.
        
        Args:
            service_provider_id: Service Provider ID or Enterprise ID containing the Group ID.
            group_id: Group ID to generate the report for.

        Returns:
            JSON: A JSON formatted report of service packs assigned to AA, CC, and HG. 
        """  
        return scripts.aa_cc_hg_audit.main(self.api, service_provider_id, group_id)

    # TODO: How will users be passed in
    def bulk_enable_voicemail(self, users):
        return scripts.bulk_enable_voicemail.main(self.api, users)


    def bulk_password_reset(self, service_provider_id: str, group_id: str, users: list, password_type: str):
        """ Resets a list of users SIP passwords or Voicemail passcodes. Specify in password_type with the options of
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
        return scripts.bulk_password_reset.main(self.api, service_provider_id, group_id, users, password_type)


    def find_alias(self, service_provider_id: str, group_id: str, alias: str):
        """ Locates alias if assigned to broadworks entity. 

        Args:
            service_provider_id (str): Service Prodiver where group is hosted.
            group_id (str): Group where alias is located.
            alias (int): Alias number to identify e.g. 0

        Raises:
             AOALiasNotFound: If alias not found AOAliasNotFound error raised
        
        Returns:
            str: Returns type and name/ userId of entity where alias located. 
        
        """
        return scripts.find_alias.main(self.api, service_provider_id, group_id,
                                       alias)


    def group_audit(self, service_provider_id: str, group_id: str):
        """
        Produces a report of key information within the group.
        Reports on DN usage, Service and Service pack usage, Trunking call capacity and group info.

        Args:
            service_provider_id (str): Service Provider ID or Enterprise ID containing the Group ID.
            group_id (str): Group ID to generate the report for.

        Returns:
            str: A JSON formatted report of the group.
        """
        return scripts.group_audit.main(self.api, service_provider_id, group_id)


    def service_pack_audit(self, servive_provider_id, group_id):
        """
        A stripped down version of group audit focussing only on the service packs assigned within
        the group. This only shows the service packs assigned and total count of unlike group audit 
        which details the users this is assigned to.

        Args:
            service_provider_id (str): Service Provider ID or Enterprise ID containing the Group ID.
            group_id (str): Group ID to generate the report for.

        Returns:
            str: A JSON formatted report of service packs assigned in the group.
        """
        return scripts.service_pack_audit.main(self.api, servive_provider_id, group_id)


    def user_activity(self, user):
        return scripts.user_activity.main(self.api, user)


    def user_association(self, service_provider_id: str, group_id: str, user_id: str):
        """ 
        Identify a user's associations with Call Centers (CC), Hunt Groups (HG), 
        and Pick Up Groups.

        Args:
            service_provider_id (str): Service Provider where the group is hosted.
            group_id (str): Group where the User is located.
            user_id (str): Target user ID.

        Returns:
            str: Formatted output of the user showing all CC, HG, and Pick Up user is assigned to.
        """
        return scripts.user_association.main(self.api, service_provider_id, group_id, user_id)


    def move_numbers(self, current_service_provider_id: str, current_group_id: str, target_service_provider_id: str, 
                     target_group_id: str, start_of_range_number: str, end_of_range_number: str = None) -> bool:
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
        return scripts.move_numbers.main(self.api, current_service_provider_id, current_group_id, 
                                        target_service_provider_id, target_group_id, start_of_range_number, 
                                        end_of_range_number )
        
        
    def remove_numbers(self, service_provider_id: str, group_id: str, start_of_range_number: str, 
                       end_of_range_number: str = None):
        """Removes a singular or range of numbers from the entire Broadworks instance.

        Note: Numbers need to be strings and follow this format: +{country code}-{number}.
        
        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located which hosts target numbers.
            group_id (str): Group ID where target numbers are located.
            start_of_number_range (str): Starting number in range of numbers you would like to remove. 
            end_of_number_range (str): Ending nummber in range of numbers you would like to remove. If you need to remove
            only one number do not enter a value for this paramter. Defaults to None.
        """
        return scripts.remove_numbers.main(self.api, service_provider_id, group_id, start_of_range_number, 
                       end_of_range_number)
        
    def locate_free_extension( self, service_provider_id: str, group_id: str, range_start: int, range_end: int ):
        """Locates the lowest value free extension given the provided range of extension numbers.

        Raises: OSExtensionNotFound: Raises when a free extension is not located within the passed range.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located which hosts needed free extensions
            group_id (str): Group ID where target extensions are located.
            range_start (int): integral value specifying the starting range for free extensions
            range_end (int): integral value specifying the ending range for free extensions

        Returns:
            JSON: JSON data of the free extension {extension: "1000"}
        """
        return scripts.locate_free_extension.main( self.api, service_provider_id, group_id, range_start, range_end )
    
    def service_provider_trunking_capacity(self, service_provider_id: str):
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
            JSON: JSON data of Trunking Call Capacity details of SP/ ENT, Groups, and Trunk Groups.
        """
        return scripts.service_provider_trunking_capacity.main(self.api, service_provider_id)
    
    
    def webex_builder(self, service_provider_id: str, group_id: str, user_id: str, 
                      device_type: str, email:str, primary_device: bool =True, 
                      webex_feature_pack_name: str =None, enable_integrated_imp: bool =True):
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
            dict: Webex user/ device details. Includes webex client username and password, and if primary device 
            device type set. 
            
        Raises:
            OSLicenseNonExistent: Raised if user does not have correct license which allows for SCA devices.
        """
        
        return scripts.webex_builder.main(self.api, service_provider_id, group_id, user_id, device_type, 
                                          email, primary_device, webex_feature_pack_name, enable_integrated_imp)