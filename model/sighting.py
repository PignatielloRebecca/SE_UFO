from dataclasses import dataclass
from _datetime import datetime

@dataclass
class Sighting:
    id: int
    s_datetime: datetime
    city: str
    state: str
    country: str
    shape: str
    duration: int
    duration_hm: float
    comments: str
    date_posted:datetime
    latitude:float
    longitude:float

    def __str__(self):
        return f"{self.id}, {self.s_datetime}, {self.city}, {self.state}, {self.country}, {self.shape}, {self.duration}, {self.duration_hm}, {self.comments}, {self.date_posted}, {self.latitude}, {self.longitude}"

    def __hash__(self):
        return hash(self.id)