from dataclasses import dataclass
from _datetime import datetime

@dataclass
class Sighting:
    id: int
    s_datetime: datetime
    shape: str
    latitude:float
    longitude:float

    def __str__(self):
        return f"{self.id}, {self.s_datetime},{self.shape}, {self.latitude}, {self.longitude}"

    def __hash__(self):
        return hash(self.id)