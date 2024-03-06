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
        

        :param service_provider_id: Service Provider ID or Enterprise ID containing the Group ID.
        :param group_id: Group ID to generate the report for.

        :return JSON: A JSON formatted report of service packs assigned to AA, CC, and HG. 
        """  
        return scripts.aa_cc_hg_audit.main(self.api, service_provider_id, group_id)

    # TODO: How will users be passed in
    def bulk_enable_voicemail(self, users):
        return scripts.bulk_enable_voicemail.main(self.api, users)


    def bulk_password_reset(self, service_provider_id: str, group_id: str, users: list, password_type: str):
        """ Resets a list of users SIP passwords or Voicemail passcodes. Specifify in password_type with the options of
        'SIP' or 'Voicemail' and the script will perform the necessary actions. 

        Args:
            service_provider_id (str): Service Provider ID where group is hosted.
            group_id (str): Group ID where target users are located.
            users (list): List of User IDs of the target users to reset the password.
            password_type (str): Type of password to reset either 'SIP' or 'Voicemail'. Only accepts these two options. 

        Returns:
            Dict: Users and their new passwords.
        """
        return scripts.bulk_password_reset.main(self.api, service_provider_id, group_id, users, password_type)


    def find_alias(self, service_provider_id: str, group_id: str, alias: str):
        """ Locates alias if assigned to broadworks entity. 

        :param service_provider_id (str): Service Prodiver where group is hosted.
        :param group_id (str): Group where alias is located.
        :param alias (int): Alias number to identify e.g. 0

        :return str: Returns type and name/ userId of entity where alias located. 
        :raise AOALiasNotFound: If alias not found AOAliasNotFound error raised 
        """
        return scripts.find_alias.main(self.api, service_provider_id, group_id,
                                       alias)


    def group_audit(self, service_provider_id: str, group_id: str):
        """
        Produces a report of key information within the group.
        Reports on DN usage, Service and Service pack usage, Trunking call capacity and group info.

        :param service_provider_id (str): Service Provider ID or Enterprise ID containing the Group ID.
        :param group_id (str): Group ID to generate the report for.

        :return str: A JSON formatted report of the group.
        """
        return scripts.group_audit.main(self.api, service_provider_id, group_id)


    def service_pack_audit(self, servive_provider_id, group_id):
        """
        A stripped down version of group audit focussing only on the service packs assigned within
        the group. This only shows the service packs assigned and total count of unlike group audit 
        which details the users this is assigned to.

        :param service_provider_id (str): Service Provider ID or Enterprise ID containing the Group ID.
        :param group_id (str): Group ID to generate the report for.

        :return str: A JSON formatted report of service packs assigned in the group.
        """
        return scripts.service_pack_audit.main(self.api, servive_provider_id, group_id)


    def user_activity(self, user):
        return scripts.user_activity.main(self.api, user)


    def user_association(self, service_provider_id: str, group_id: str, user_id: str):
        """ 
        identify a user's associations with Call Centers (CC), Hunt Groups (HG), 
        and Pick Up Groups.

        :pararm service_provider_id (str): Service Provider where the group is hosted.
        :pararm group_id (str): Group where the User is located.
        :pararm user_id (str): Target user ID.

        :returns (str): Formatted output of the user showing all CC, HG, and Pick Up user is assigned to.
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
        return scripts.remove_numbers(self.api, service_provider_id, group_id, start_of_range_number, 
                       end_of_range_number)
    