from enum import Enum
from game_mechanics.Statistics import Statistics

class DinosaurType(Enum):
    STEGOSAUR = {"statistics": Statistics(speed=1, hp=20), "facing_right": False, "exp": 2}
    TRICERATOPS = {"statistics": Statistics(speed=2, hp=12), "facing_right": False, "exp": 4}
    SILESAURUS = {"statistics": Statistics(speed=3, hp=2), "facing_right": False, "exp": 1}
    VELOCIRAPTOR = {"statistics":  Statistics(speed=4, hp=5), "facing_right": False, "exp": 4}
    TYRANOSAUR = {"statistics": Statistics(speed=5, hp=30), "facing_right": True, "exp": 8}
    POLONOSUCHUS = {"statistics": Statistics(speed=2, hp=10), "facing_right":False, "exp": 3}