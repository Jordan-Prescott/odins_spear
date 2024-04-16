import logging

from logging.handlers import SysLogHandler, RotatingFileHandler
from logging import FileHandler

class Logger:
    
    def __init__(self, user: str = None) -> None:

        self._user = user
            
        self._logger_obj = logging.getLogger('os')
        self._logger_obj.setLevel(logging.DEBUG)
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s - %(user)s - %(endpoint)s - %(response_code)s')
        
        self._logger_obj.handlers.clear()
        
        self.set_up_file_handler()
    
    
    def set_up_file_handler(self):
            
        log_file = 'app.log'
        backup_count = 5
        
        handler = RotatingFileHandler(log_file, backupCount=backup_count)
        handler.setFormatter(self._formatter)
        
        self._logger_obj.addHandler(handler)
        
        
    def set_up_sys_log_handler(self, url: str, port_number: int):
        
        self.url = url
        self.port_number = port_number
        
        self._logger_obj.addHandler(SysLogHandler(address=(self.url, self.port_number)))
        
        
    def log_request(self, endpoint: str, response_code: int):
        self._logger_obj.info(
            "LOG", 
            extra={
                'user': self._user, 
                'endpoint': endpoint,
                'response_code': response_code}
            )
        