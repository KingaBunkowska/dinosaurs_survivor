from game_mechanics.Entity import Entity
from game_mechanics.Dinosaur_type import Dinosaur_type

class Dinosaur(Entity):
    def __init__(self, type = Dinosaur_type.STEGOSAUR , friendly = False):
        super().__init__(type.value["statistics"])
        self.type = type
        self.ally = friendly