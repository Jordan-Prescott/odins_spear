import logging

from logging.handlers import SysLogHandler
from logging import FileHandler

class Logger:
    
    def __init__(self, api: str = None, user: str = None, 
                 url: str = None, port_number: int = 0,) -> None:

        self.url = url
        self.port_number = port_number
        
        self._api = api
        self._user = user
        
        # logging.basicConfig(
        #     filename='app.log',
        #     level=logging.INFO,
        #     format='%(asctime)s - %(levelname)s - %(message)s',
        #     datefmt='%Y-%m-%d %H:%M:%S',
        #     filemode='a',
        #     encoding='utf-8'
        #     )
    
        self._logger_obj = logging.getLogger("Odin's Spear")
        self._logger_obj.addHandler(FileHandler('app.log'))
        self._logger_obj.addHandler(SysLogHandler(address=(self.url, self.port_number)))
       
        # self._file_handler = FileHandler('app.log')
        # self._sys_log_handler = SysLogHandler(address=(self.url, self.port))
        
    def log_request(self, message: str):
        self._logger_obj.info(message)