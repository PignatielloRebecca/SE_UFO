from dataclasses import dataclass
from model.state import State

@dataclass
class Neighbor:
    state1: State
    state2: State