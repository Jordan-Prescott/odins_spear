from loguru import logger

class Logger:
    
    __instance = None

    @staticmethod
    def get_instance(user: str):
        if Logger.__instance is None:
            Logger(user)
        return Logger.__instance
    
    def __init__(self, user: str = None) -> None:
        """_summary_

        Args:
            user (str, optional): _description_. Defaults to None.
        """

        if Logger.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            
            self._user = user
                
            self._log_format = "{time} | {message} | {extra}" 
            self._logger_obj = logger
            self._logger_obj.remove() 
            
            self.set_up_file_handler()
            
            Logger.__instance = self
    
    
    def set_up_file_handler(self, path='OS.log'):
        """_summary_

        Args:
            path (str, optional): _description_. Defaults to 'app.log'.
        """
        
        self._logger_obj.add(
            path,
            format=self._log_format
        )
                
        
    def set_up_sys_log_handler(self, url: str):
        """_summary_

        Args:
            url (str): _description_
        """
        
        self.url = url
        
        self._logger_obj.add(
            self.url,
            format=self._log_format,
            serialize=True,
        )
        
        
    def _log_request(self, **kwargs):
        """_summary_

        Args:
            endpoint (str): _description_
            response_code (int): _description_
        """
        with self._logger_obj.contextualize(
            user=self._user, 
            **kwargs):
            
            self._logger_obj.info(
                "Odin's Spear"
            )
        