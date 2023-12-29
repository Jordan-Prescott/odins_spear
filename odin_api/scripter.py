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

    #TODO: How will users be passed in
    def bulk_enable_voicemail(self, users):
        return scripts.bulk_enable_voicemail.main(self.api, users)
    
    #TODO: How will users be passed in
    def bulk_password_reset(self, users):
        return scripts.bulk_password_reset.main(self.api, users)
    
    def find_alias(self, service_provider_id, group_id, alias):
        return scripts.find_alias.main(self.api, service_provider_id, group_id, 
                                       alias)
    
    def group_audit(self, group):
        return scripts.group_audit.main(self.api, group)
    
    def user_activity(self, user):
        return scripts.user_activity.main(self.api, user)
    
    def user_huntgroup_membership(self, user):
        return scripts.user_huntgroup_membership.main(self.api, user)
