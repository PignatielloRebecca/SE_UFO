from dataclasses import dataclass, field
@dataclass
class State:
    id: int
    name: str
    capital: str
    lat: float
    lng: float
    area: int
    population: int
    neighbors: list= field(default_factory=list)


    def __repr__(self):
        return f" {self.id}, {self.name}, {self.capital}, {self.lat}, {self.lng}, {self.area}, {self.population}, {self.neighbors}"

    def __hash__(self):
        return hash(self.id)
