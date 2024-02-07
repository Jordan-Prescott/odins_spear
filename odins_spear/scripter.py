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

    # TODO: How will users be passed in
    def bulk_enable_voicemail(self, users):
        return scripts.bulk_enable_voicemail.main(self.api, users)

    # TODO: How will users be passed in
    def bulk_password_reset(self, users):
        return scripts.bulk_password_reset.main(self.api, users)

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

    def user_activity(self, user):
        return scripts.user_activity.main(self.api, user)

    def user_association(self, service_provider_id: str, group_id: str, user_id: str):
        """ identify a user's associations with Call Centers (CC), Hunt Groups (HG), 
        and Pick Up Groups.

        :pararm service_provider_id (str): Service Provider where the group is hosted.
        :pararm group_id (str): Group where the User is located.
        :pararm user_id (str): Target user ID.

        :returns (str): Formatted output of the user showing all CC, HG, and Pick Up user is assigned to.
        """
        return scripts.user_association.main(self.api, service_provider_id, group_id, user_id)
