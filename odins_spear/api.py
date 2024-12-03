import requests

from .requester import Requester
from .methods import *
from .logger import Logger
from .scripter import Scripter
from .reporter import Reporter
from .exceptions import (
    OSApiAuthenticationFail,
    OSSessionRefreshFail,
    OSFailedToLocateSession,
)

from .endpoints import *


class API:
    def __init__(
        self, base_url: str, username: str, password: str, rate_limit: bool = True
    ) -> None:
        """ Connection to Odin API, all interactions with the api are here.

        Args:
            base_url (str): Base url of your odin instance api.
            username (str): Username used when logging into odin account.
            password (str): Password used when logging into odin account stored as virtual environment.
            rate_limit (bool): Enables (True) or Disables (False) rate limiting to 5 calls per second. Defaults to True.
            
        Vars: 
            authorised (bool): Boolean value to indicate if api is authorised.\
            token (str): Token string returned from odin api.
        """

        self.base_url = base_url
        self.username = username
        self.password = password
        self.rate_limit = rate_limit

        self.authorised = False
        self.token = ""

        self.logger = Logger.get_instance(self.username)
        self._requester = Requester(self.base_url, self.rate_limit, self.logger)

        self.scripter = Scripter(api=self)
        self.reporter = Reporter(api=self)

        self.call_records = CallRecords(self._requester)
        self.administrators = Administrators(self._requester)

    def authenticate(self):
        """Authenticates session with username and password supplied by user.

        Raises:
            OSApiAuthenticationFail: Raised if authenticaion fails.

        Returns:
            Bool: Returns True to indicate authentication was successful.
        """

        endpoint = "/auth/token"

        payload = {"username": self.username, "password": self.password}

        try:
            response = self._requester.post(endpoint, data=payload)
            self._update_requester(response)
            return True
        except requests.exceptions.HTTPError:
            raise OSApiAuthenticationFail()

    def refresh_authorisation(self):
        """Re-authenticates the session with the API. Used if API key is to expire.

        Raises:
            OSSessionRefreshFail: Raised if authentication fails.

        Returns:
            Bool: Returns True to indicate authentication was successful.
        """

        endpoint = "/auth/session"

        try:
            response = self._requester.put(endpoint)
            self._update_requester(response)
            return True
        except requests.exceptions.HTTPError:
            raise OSSessionRefreshFail()

    def get_auth_details(self):
        """Gets current session details.

        Raises:
            OSFailedToLocateSession: Raised when session details can't be found.
                Most likely because session has expired.

        Returns:
            Dict: Current session details.
        """

        endpoint = "/auth/session"

        try:
            return self._requester.get(endpoint)
        except requests.exceptions.HTTPError:
            raise OSFailedToLocateSession()

    def _update_requester(self, session_response):
        """When authenticating or re-auth update requester with token so it can make
        api calls

        Args:
            session_response (obj): Requests mod response.
        """

        self.token = session_response["token"]
        self._requester.headers["Authorization"] = f"Bearer {self.token}"
        self.authorised = True

    def __str__(self) -> str:
        return (
            f"API - url: {self.base_url}, username: {self.username}"
            f"Authenticated: {self.authorised}"
        )
