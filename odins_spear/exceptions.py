""" Library exceptions.
"""


class OAError(Exception):
    """ Odin Api Exceptions
    """

    def __str__(self) -> str:
        return f"I dont think you can be trusted in a combat situation"


class OAApiAuthenticationFail(OAError):
    """
    Raised when api fails to authenticate
    """

    def __str__(self) -> str:
        return f"Failed to authenticate. Check username, password, and url." 


class OARequestTypeError(OAError):
    """ Raised when unsupport request type is given. 
    """

    def __str__(self) -> str:
        return f"Non-supported request type, supported: GET, POST, PUT, DELETE."
    

class OAObjectParseError(OAError):
    """ Raised when parsing Broadworks Entity fails. 
    """

    def __str__(self) -> str:
        return f"Parsing Broadwork Entity failed."
    
class OAUnsupportedFilter(OAError):
    """ Raised when user requests to filter on unsupported filter
    """

    def __str__(self) -> str:
        return f"Unsupported filter. Supported: macAddress, lastName," \
            f"firstName, dn, emailAddress, userId, extension"
    
class AOAliasNotFound(OAError):
    """ Raised when alias is not found in Broadowks Group. 
    """

    def __str__(self) -> str:
        return f"Alias not found, it either does not exist or check alias."
    
class AOSessionRefreshFail(OAError):
    """ Raised when refreshing session fails.
    """

    def __str__(self) -> str:
        return f"Refreshing sesion failed. Check credentials are valid and " \
            f"token has not yet expired. If expired request another."
            
class AOLogoutFailed(OAError):
    """ Raised when logout attempt failed.
    """

    def __str__(self) -> str:
        return f"Failed to logout, session still valid. Please try again."
    
class AOFailedToLocateSession(OAError):
    """ Raised when user attempts to get session details but session cant be found.
    """

    def __str__(self) -> str:
        return f"Session details not found. Check token is valid and not exppired."