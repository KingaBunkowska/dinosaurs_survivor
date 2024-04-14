from game_mechanics.Entity import Entity
from game_mechanics.Dinosaur_type import Dinosaur_type
from game_mechanics.Position import Position
import random


class Dinosaur(Entity):
    def __init__(self, type = Dinosaur_type.STEGOSAUR , friendly = False, position=Position(100, 100)):
        super().__init__(statistics = type.value["statistics"].changed_by(speed = random.normalvariate(0, 0.1)), position=position)

        self.type = type
        self.ally = friendly

    def move(self, player_position:Position):
        if not self.ally:
            move_vector = player_position - self.position
            super().move(move_vector)