from enum import Enum
from game_mechanics.Statistics import Statistics

class Dinosaur_type(Enum):
    STEGOSAUR = {"name": "stegosaur", "statistics": Statistics(speed=3)}
    TRICERATOPS = {"name": "triceratops", "statistics": Statistics(speed=4)}
    TYRANOSAUR = {"name": "tyranosaur", "statistics": Statistics(speed=7)}