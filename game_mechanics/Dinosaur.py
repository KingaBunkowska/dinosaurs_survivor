from game_mechanics.Entity import Entity
from game_mechanics.DinosaurType import DinosaurType
from game_mechanics.Position import Position
import random


class Dinosaur(Entity):
    def __init__(self, type = DinosaurType.STEGOSAUR, friendly = False, position=Position(100, 100)):
        super().__init__(statistics = type.value["statistics"].changed_by(speed = random.normalvariate(0, 0.1)), position=position, facing_right=type.value["facing_right"])

        self.type = type
        self.ally = friendly

    def move(self, player_position:Position, dinosaurs):
        if not self.ally:
            move_vector = player_position - self.position
        else:
            if dinosaurs:
                move_vector = min(dinosaurs, key = lambda dino: self.position.distance(dino.position)).position - self.position
            else: 
                move_vector = Position(0, 0)

        super().move(move_vector)