from dataclasses import dataclass, field
from typing import List, Type

@dataclass
class call_flow:
    name: str
    nodes: List = field(default_factory=list)


@dataclass
class external_number:
    id: str    