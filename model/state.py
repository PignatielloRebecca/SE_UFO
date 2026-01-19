from dataclasses import dataclass, field
@dataclass
class State:
    id: int
    name: str
    lat: float
    lng: float


    def __repr__(self):
        return f" {self.id}, {self.name}, {self.lat}, {self.lng}"

    def __hash__(self):
        return hash(self.id)
