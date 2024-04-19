from loguru import logger

class Logger:
    def __init__(self, user: str = None) -> None:

        self._user = user
             
        self._logger_obj = logger
        self._logger_obj.remove() 
        
        self.set_up_file_handler()
    
    
    def set_up_file_handler(self, path='app.log'):
          
        self._logger_obj.add(
            path,
            format="{time} | {message} | {extra}"
        )
                
        
    def set_up_sys_log_handler(self, url: str):
        
        self.url = url
        
        self._logger_obj.add(
            self.url,
            format="{time} | {message} | {extra}"
        )
        
        
    def _log_request(self, endpoint: str, response_code: int):
        with self._logger_obj.contextualize(
            user=self._user, 
            endpoint=endpoint, 
            response_code=response_code):
            
            self._logger_obj.info(
                "odins_spear"
            )
        