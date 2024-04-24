# from loguru import logger
import logging 
from logging import Formatter


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
                
            # self._log_format = "{time} | {message} | {extra}" 
            # self._logger_obj = logger
            # self._logger_obj.remove() 
            
            #Remove handlers from root logger
            for handler in logging.root.handlers[:]:
                if isinstance(handler, logging.StreamHandler):
                    logging.root.removeHandler(handler)
            
            self._format = Formatter(fmt="%(asctime)s | %(name)s | %(message)s | %(response_code)s | %(endpoint)s")
            
            self._logger_obj = logging.getLogger("Odin's Spear")
            self._logger_obj.setLevel(logging.DEBUG)
            
            self.set_up_file_handler()
            
            Logger.__instance = self
    
    
    def set_up_file_handler(self, path='os.log'):
        """_summary_

        Args:
            path (str, optional): _description_. Defaults to 'app.log'.
        """
        
        from logging import FileHandler
        
        file_handler = FileHandler(path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self._format)
        
        self._logger_obj.addHandler(file_handler)
        
        # self._logger_obj.add(
        #     path,
        #     format=self._log_format
        # )
                
        
    def set_up_sys_log_handler(self, url: str, port_number: int):
        """_summary_

        Args:
            url (str): _description_
        """
        
        from logging.handlers import SysLogHandler

        self.url = url
        self.port_number = port_number
        
        syslog_handler = SysLogHandler(address=(url, port_number))
        syslog_handler.setLevel(logging.DEBUG)
        syslog_handler.setFormatter(self._format)
        
        self._logger_obj.addHandler(syslog_handler)

        
        # self._logger_obj.add(
        #     self.url,
        #     format=self._log_format,
        #     serialize=True,
        # )
        
        
    def _log_request(self, **kwargs):
        """_summary_

        Args:
            endpoint (str): _description_
            response_code (int): _description_
        """
        # with self._logger_obj.contextualize(
        #     user=self._user, 
        #     **kwargs):
            
        #     self._logger_obj.info(
        #         "Odin's Spear"
        #     )
        
        
        self._logger_obj.info(
            self._user,
            extra= kwargs
        )
        
    # def _unpack_kwargs(**kwargs):
    #     kwargs_dict = {}
    #     return kwargs_dict.update(kwargs)