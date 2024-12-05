from typing import List

from ..exceptions import OSUnsupportedFilter, OSUnsupportedFilterType
from .constants import supported_filters


def check_filters(filters: List[str]) -> bool:
    """
    Check if filters are supported. If supported return True.

    Suppoerted filters:
    - macAddress
    - lastName
    - firstName
    - dn
    - emailAddress
    - userId
    - extension
    """
    for filter_ in filters:
        if filter_ not in supported_filters:
            raise OSUnsupportedFilter(filter_)


def check_filter_type(filter_types: List[str]) -> bool:
    """
    Check if filter types are supported. If supported return True.

    Supported filter types:
    - contains
    - startsWith
    - endsWith
    - equals
    """
    for filter_ in filter_types:
        if filter_ not in supported_filters:
            raise OSUnsupportedFilterType(filter_)


def check_type_filter(filter_: str, filter_type: str) -> None:
    """
    Checks if filter and filter type are supported.
    """
    check_filters([filter_])
    check_filter_type([filter_type])
