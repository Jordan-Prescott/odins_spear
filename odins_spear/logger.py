from loguru import logger

class Logger:
    def __init__(self, user: str = None) -> None:
        """_summary_

        Args:
            user (str, optional): _description_. Defaults to None.
        """

        self._user = user
             
        self._logger_obj = logger
        self._logger_obj.remove() 
        
        self.set_up_file_handler()
    
    
    def set_up_file_handler(self, path='app.log'):
        """_summary_

        Args:
            path (str, optional): _description_. Defaults to 'app.log'.
        """
        
        self._logger_obj.add(
            path,
            format="{time} | {message} | {extra}"
        )
                
        
    def set_up_sys_log_handler(self, url: str):
        """_summary_

        Args:
            url (str): _description_
        """
        
        self.url = url
        
        self._logger_obj.add(
            self.url,
            format="{time} | {message} | {extra}"
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
                "odins_spear"
            )
        