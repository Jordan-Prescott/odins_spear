from dataclasses import dataclass, field
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
    first_name: str
    last_name: str
    extension: str
    userId: str
    feature_packs: list
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

    @classmethod
    def from_dict(cls, first_name, last_name, extension, data):
        return cls(
            first_name=first_name,
            last_name=last_name,
            extension=extension,
            userId=data.get("userId"),
            feature_packs=data.get("servicePackServices"),
            total=data.get("total"),
            totalAnsweredAndMissed=str(data.get("totalAnsweredAndMissed")),
            answeredTotal=data.get("answeredTotal"),
            missedTotal=data.get("missedTotal"),
            busyTotal=data.get("busyTotal"),
            redirectTotal=data.get("redirectTotal"),
            receivedTotal=data.get("receivedTotal"),
            receivedMissed=data.get("receivedMissed"),
            receivedAnswered=data.get("receivedAnswered"),
            placedTotal=data.get("placedTotal"),
            placedMissed=data.get("placedMissed"),
            placedAnswered=data.get("placedAnswered"),
        )
