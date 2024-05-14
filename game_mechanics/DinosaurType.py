from enum import Enum
from game_mechanics.Statistics import Statistics

class DinosaurType(Enum):
    STEGOSAUR = {"statistics": Statistics(speed=1), "facing_right": False, "exp": 5}
    TRICERATOPS = {"statistics": Statistics(speed=2), "facing_right": False, "exp": 5}
    SILESAURUS = {"statistics": Statistics(speed=3), "facing_right": False, "exp": 5}
    VELOCIRAPTOR = {"statistics":  Statistics(speed=4), "facing_right": False, "exp": 5}
    TYRANOSAUR = {"statistics": Statistics(speed=5), "facing_right": True, "exp": 8}