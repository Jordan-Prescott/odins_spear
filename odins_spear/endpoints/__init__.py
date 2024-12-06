# endpoints/__init__.py

from .administrators import Administrators
from .call_records import CallRecords
from .users import Users

__all__ = [
    "Administrators",
    "CallRecords",
    "Users",
]
