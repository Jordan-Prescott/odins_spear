# endpoints/__init__.py

from .administrators import Administrators
from .alternate_numbers import AlternateNumbers
from .auto_attendant import AutoAttendants
from .call_records import CallRecords
from .users import Users

__all__ = [
    "Administrators",
    "AlternateNumbers",
    "AutoAttendants",
    "CallRecords",
    "Users",
]
