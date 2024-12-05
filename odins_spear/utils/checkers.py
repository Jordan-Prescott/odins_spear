from ..exceptions import OSUnsupportedFilter, OSUnsupportedFilterType
from .constants import supported_filters, supported_filter_types


def check_type_filter(filter_by: str, filter_type: str) -> None:
    """Checks if the filter and filter type is supported by the API.

    Args:
        filter_by (str): The data you would like to filter by e.g. firstName
        filter_type (str): The type of filter you would like to apply e.g. equal to

    Raises:
        OSUnsupportedFilter: Raised when the filter is not supported by the API
        OSUnsupportedFilterType: Raised when the filter type is not supported by the API

    Supported filters:
    - macAddress
    - lastName
    - firstName
    - dn
    - emailAddress
    - userId
    -extension

    Supported filter types:
    - equal to
    - starts with
    - contains
    """

    if filter_by not in supported_filters:
        raise OSUnsupportedFilter(filter_by)
    if filter_type not in supported_filter_types:
        raise OSUnsupportedFilterType(filter_type)
