from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class call_flow:
    name: str
    nodes: List = field(default_factory=list)


@dataclass
class external_number:
    id: str    
    
@dataclass
class call_records_statistics:
    extension: str
    userId: str
    total: int
    totalAnsweredAndMissed: str
    answeredTotal: str
    missedTotal: str
    busyTotal: str
    redirectTotal: str
    receivedTotal: str
    receivedMissed: str
    receivedAnswered: str
    placedTotal: str
    placedMissed: str
    placedAnswered: str
    
    def replace_none_with_0(self):
        for field in fields(self):
            value = getattr(self, field.name)
            # Replace None with 0
            if value is None or value == 'None':
                setattr(self, field.name, 0)

    @classmethod
    def from_dict(cls, extension, data):
        return cls(
            extension = extension,
            userId= data.get("userId"),
            total= data.get("total"), 
            totalAnsweredAndMissed= str(data.get("totalAnsweredAndMissed")),
            answeredTotal= data.get("answeredTotal"),
            missedTotal= data.get("missedTotal"),
            busyTotal= data.get("busyTotal"),
            redirectTotal= data.get("redirectTotal"),
            receivedTotal= data.get("receivedTotal"),
            receivedMissed= data.get("receivedMissed"),
            receivedAnswered= data.get("receivedAnswered"),
            placedTotal= data.get("placedTotal"),
            placedMissed= data.get("placedMissed"),
            placedAnswered= data.get("placedAnswered")
        )
