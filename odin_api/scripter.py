# user will use this module as an entry to oa_scripts for example:
# odin_aip.scripts.find_alias('foo') will call the relevant script in oa_scipts = oa_scripts.find_alias('foo')
import scripts

class Scripter:
    """ scripter

    :param api: 
    """
    def __init__(self, api) -> None:
        self.api = api

    #TODO: How will users be passed in
    def bulk_enable_voicemail(self, users):
        return scripts.bulk_enable_voicemail(self.api, users)
    
    #TODO: How will users be passed in
    def bulk_password_reset(self, users):
        return scripts.find_alias(self.api, users)
    
    def find_alias(self, group, alias):
        return scripts.find_alias.main(self.api, group, alias)
    
    def group_audit(self, group):
        return scripts.group_audit(self.api, group)
    
    def user_activity(self, user):
        return scripts.user_activity(self.api, user)
    
    def user_huntgroup_membership(self, user):
        return scripts.user_huntgroup_membership(self.api, user)
