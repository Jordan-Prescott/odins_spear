import os
import logging
from logging import Formatter


class Logger:
    __instance = None

    # Singleton implementation
    @staticmethod
    def get_instance(user: str):
        if Logger.__instance is None:
            Logger(user)
        return Logger.__instance

    def __init__(self, user: str) -> None:
        """Logger class logs API calls made using Odin's Spear.
        Details logged are: Date/ Time, Name (Odin's Spear), User (You the developer), response code, endpoint.
        Logs are sent to os.log by default but can be changed in set_up_file_handler() method.
        Logs can also be sent to an external syslog server using the set_up_sys_log_handler method.

        NOTE: This object is a singleton and can't be instatiated more than once.

        Args:
            user (str): Username used when creating API object.
        """

        if Logger.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self._user = user

            # Remove handlers from root logger
            for handler in logging.root.handlers[:]:
                if isinstance(handler, logging.StreamHandler):
                    logging.root.removeHandler(handler)

            self._format = Formatter(
                fmt="%(asctime)s | %(name)s | %(message)s | %(response_code)s | %(endpoint)s"
            )

            self._logger_obj = logging.getLogger("Odin's Spear")
            self._logger_obj.setLevel(logging.DEBUG)

            self.set_up_file_handler()

            Logger.__instance = self

    def set_up_file_handler(self, path="os.log"):
        """Creates file handler for Logger object. This defaults to 'os.log' file but this
        can be changed by passing in a path.

        Args:
            path (str, optional): Path to file to send logs. Defaults to 'os.log'.
        """

        from logging import FileHandler

        try:
            file_handler = FileHandler(path)
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception:
            print(f"You do not have permission create {path}. Logs saved to os.logg")
            path = "os.log"
            file_handler = FileHandler(path)

        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self._format)

        self._logger_obj.addHandler(file_handler)

    def set_up_sys_log_handler(self, url: str, port_number: int):
        """Sets up a Syslog Server handler which will send logs generated to syslog server.
        URL to server as well as the port number is needed to send logs.

        Args:
            url (str): IP/ URL to syslog server e.g. 1.1.1.1 or mysyslogserver.com/
            port_number (int): Port number the logs will sent on to URL
        """

        from logging.handlers import SysLogHandler

        self.url = url
        self.port_number = port_number

        syslog_handler = SysLogHandler(address=(url, port_number))
        syslog_handler.setLevel(logging.DEBUG)
        syslog_handler.setFormatter(self._format)

        self._logger_obj.addHandler(syslog_handler)

    def _log_request(self, **kwargs):
        """Takes in the response call and response details from Requester
        and logs this information with logging level INFO.

        Args:
            kwargs: Two keyword arguements: endpoint and response_code
        """

        self._logger_obj.info(self._user, extra=kwargs)
