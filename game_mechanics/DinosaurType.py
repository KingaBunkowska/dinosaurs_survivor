from enum import Enum
from game_mechanics.Statistics import Statistics

class DinosaurType(Enum):
    STEGOSAUR = {"name": "stegosaur", "statistics": Statistics(speed=1)}
    TRICERATOPS = {"name": "triceratops", "statistics": Statistics(speed=2)}
    TYRANOSAUR = {"name": "tyranosaur", "statistics": Statistics(speed=5)}