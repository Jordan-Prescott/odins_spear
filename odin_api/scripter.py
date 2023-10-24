# user will use this module as an entry to oa_scripts for example:
# odin_aip.scripts.find_alias('foo') will call the relevant script in oa_scipts = oa_scripts.find_alias('foo')
import scripts

class Scripter:
    """ scripter

    :param api: 
    """
    def __init__(self, api) -> None:
        self.api = api

    def find_alias(self, api, group, alias):
        return scripts.find_alias.main(api, group, alias)