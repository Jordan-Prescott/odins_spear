"""Library exceptions."""


class OSError(Exception):
    """Odin's Spears Exceptions"""

    def __str__(self) -> str:
        return "I dont think you can be trusted in a combat situation"


# API


class OSApiResponseError(OSError):
    """Raised when Odin Api returns an error code."""

    def __init__(self, response):
        response = response.json()
        self.response = (
            f"{response['details']} {response['status']}: {response['error']}"
        )

    def __str__(self) -> str:
        return self.response


class OSRequestTypeError(OSError):
    """Raised when unsupport request type is given."""

    def __str__(self) -> str:
        return "Non-supported request type, supported: GET, POST, PUT, DELETE."


# AUTHENTICATION


class OSApiAuthenticationFail(OSError):
    """Raised when api fails to authenticate"""

    def __str__(self) -> str:
        return "Failed to authenticate. Check username, password, and url."


class OSSessionRefreshFail(OSError):
    """Raised when refreshing session fails."""

    def __str__(self) -> str:
        return (
            "Refreshing sesion failed. Check credentials are valid and "
            "token has not yet expired. If expired request another."
        )


class OSLogoutFailed(OSError):
    """Raised when logout attempt failed."""

    def __str__(self) -> str:
        return "Failed to logout, session still valid. Please try again."


class OSFailedToLocateSession(OSError):
    """Raised when user attempts to get session details but session cant be found."""

    def __str__(self) -> str:
        return "Session details not found. Check token is valid and not exppired."


# NOT-FOUND


class OSExtensionNotFound(OSError):
    """Raised when a searched extension is not found"""

    def __str__(self) -> str:
        return "Cannot locate extension. Please alter search criteria"


# FILTER


class OSUnsupportedFilter(OSError):
    """Raised when user requests to filter on unsupported filter"""

    def __init__(self, filter_attempt):
        self.filter_attempt = filter_attempt

    def __str__(self) -> str:
        return f"Filter '{self.filter_attempt}' is unsupported. Supported: macAddress, lastName, firstName, dn, emailAddress, userId, extension"


class OSUnsupportedFilterType(OSError):
    """Raised when user requests to filter on unsupported filter"""

    def __init__(self, type_attempt):
        self.type_attempt = type_attempt

    def __str__(self) -> str:
        return f"Filter type '{self.type_attempt}' is unsupported. Supported: contains, startsWith, endsWith, equals"


# FILES


class OSFileNotFound(OSError):
    """Raised when a file can not be found."""

    def __str__(self) -> str:
        return "File can not be found, please check path and file name."


# FORMATTING


class OSInvalidCode(OSError):
    """Raised when code is less than 4 and higher than 6."""

    def __str__(self) -> str:
        return "Code needs to be between 4 and 6 digits."


class OSInvalidWeighting(OSError):
    """Raised when invalid weighted call distribution set."""

    def __str__(self) -> str:
        return "Weighted call distribution is not equal to 100. This weight must add up to 100."


class OSInvalidData(OSError):
    """Raised when data used in request is invalid or incomplete."""

    def __str__(self) -> str:
        return (
            "Data invalid or incomplete, please check data passed to method is correct."
        )


class OSInvalidBroadworkService(OSError):
    """Raised when service given by user is not a valid license of Broadworks."""

    def __str__(self) -> str:
        return "Service invalid, please check the services you have given are valid Broadwork services."


class OSInvalidPasswordType(OSError):
    """Raised when password requested is invalid or not supported."""

    def __str__(self) -> str:
        return "Invalid or unsupported password, please review supported passwords."


#  OS FEATURES


class OSAliasNotFound(OSError):
    """Raised when alias is not found in Broadowks Group."""

    def __str__(self) -> str:
        return "Alias not found, it either does not exist or check alias."


class OSServiceNotAssigned(OSError):
    """Raised a service needed is not assigned to a Broadworks entity."""

    def __str__(self) -> str:
        return "Service not assigend to target Broadworks entity. Please check services assigned."


# RANGE


class OSRangeFault(OSError):
    """Raised when a numeric range is invalid to the context provided,
    E.G: uninitialised range values, disordered range values.
    """

    def __str__(self):
        return "Range fault raised. Please verify integrity of passed range values"


# PARSING


class OSObjectParseError(OSError):
    """Raised when parsing Broadworks Entity fails."""

    def __str__(self) -> str:
        return "Parsing Broadwork Entity failed."
