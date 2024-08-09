""" Library exceptions.
"""


class OSError(Exception):
    """ Odin Api Exceptions
    """

    def __str__(self) -> str:
        return f"I dont think you can be trusted in a combat situation"


class OSApiAuthenticationFail(OSError):
    """
    Raised when api fails to authenticate
    """

    def __str__(self) -> str:
        return f"Failed to authenticate. Check username, password, and url." 


class OSRequestTypeError(OSError):
    """ Raised when unsupport request type is given. 
    """

    def __str__(self) -> str:
        return f"Non-supported request type, supported: GET, POST, PUT, DELETE."
    

class OSObjectParseError(OSError):
    """ Raised when parsing Broadworks Entity fails. 
    """

    def __str__(self) -> str:
        return f"Parsing Broadwork Entity failed."
    
class OSUnsupportedFilter(OSError):
    """ Raised when user requests to filter on unsupported filter
    """

    def __str__(self) -> str:
        return f"Unsupported filter. Supported: macAddress, lastName," \
            f"firstName, dn, emailAddress, userId, extension"
    
class OSAliasNotFound(OSError):
    """ Raised when alias is not found in Broadowks Group. 
    """

    def __str__(self) -> str:
        return f"Alias not found, it either does not exist or check alias."
    
class OSSessionRefreshFail(OSError):
    """ Raised when refreshing session fails.
    """

    def __str__(self) -> str:
        return f"Refreshing sesion failed. Check credentials are valid and " \
            f"token has not yet expired. If expired request another."
            
class OSLogoutFailed(OSError):
    """ Raised when logout attempt failed.
    """

    def __str__(self) -> str:
        return f"Failed to logout, session still valid. Please try again."
    
class OSFailedToLocateSession(OSError):
    """ Raised when user attempts to get session details but session cant be found.
    """

    def __str__(self) -> str:
        return f"Session details not found. Check token is valid and not exppired."
    
class OSInvalidCode(OSError):
    """ Raised when code is less than 4 and higher than 6.
    """

    def __str__(self) -> str:
        return f"Code needs to be between 4 and 6 digits."
    
class OSInvalidWeighting(OSError):
    """ Raised when invalid weighted call distribution set.
    """

    def __str__(self) -> str:
        return f"Weighted call distribution is not equal to 100. This weight must add up to 100."
    

class OSInvalidData(OSError):
    """ Raised when data used in request is invalid or incomplete.
    """

    def __str__(self) -> str:
        return f"Data invalid or incomplete, please check data passed to method is correct."

class OSInvalidBroadworkService(OSError):
    """ Raised when service given by user is not a valid license of Broadworks.
    """

    def __str__(self) -> str:
        return f"Service invalid, please check the services you have given are valid Broadwork services."
    
 
class OSInvalidPasswordType(OSError):
    """ Raised when password requested is invalid or not supported.  
    """

    def __str__(self) -> str:
        return f"Invalid or unsupported password, please review supported passwords."   
    

class OSServiceNotAssigned(OSError):
    """ Raised a service needed is not assigned to a Broadworks entity.  
    """

    def __str__(self) -> str:
        return f"Service not assigend to target Broadworks entity. Please check services assigned."   

class OSFileNotFound(OSError):
    """ Raised when a file can not be found.  
    """

    def __str__(self) -> str:
        return f"File can not be found, please check path and file name."   

class OSLicenseNonExistent(OSError):
    """ Raised when the Specified Entity doesn't exist due to licensing.  
    """

    def __str__(self) -> str:
        return f"Specified Entity doesn't have the correct License." 