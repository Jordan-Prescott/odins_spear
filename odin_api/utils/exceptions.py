""" put some stuff here.
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
        return f"""Unsupported filter. Supported: macAddress, lastName, 
    firstName, dn, emailAddress, userId, extension"""