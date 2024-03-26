from game_mechanics.Entity import Entity
from game_mechanics.Dinosaur_type import Dinosaur_type
import random

class Dinosaur(Entity):
    def __init__(self, type = Dinosaur_type.STEGOSAUR , friendly = False, position=[100, 100]):
        super().__init__(statistics = type.value["statistics"], position=position)
        self.type = type
        self.ally = friendly

        self.statistics.speed += random.uniform(-1, 1)

    def move(self, player_position):
        if not self.ally:
            move_vector = [player_position[0] - self.position[0], player_position[1] - self.position[1]]
            normalized_move_vector = super()._normalize_vector(move_vector)
            move_vector = list(map(lambda x: x * self.statistics.speed, normalized_move_vector))
            self.position = [move_vector[0] + self.position[0], move_vector[1] + self.position[1]]