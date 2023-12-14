class OAError(Exception):
    """ Odin Api Exceptions
    """

    def __str__(self) -> str:
        return f"Odin API Exception"


class OAApiAuthenticationFail(OAError):
    """ Raised when api fails to authenticate
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
    
