from game_mechanics.Position import Position
from random import randint

class PickableItems:
    def __init__(self, position):
        self.position = position + Position(randint(0,5),randint(0,5))

    def get_position(self):
        return self.position

    def move(self, player_position: Position):
        move_vector = player_position - self.position
        move_vector.normalized()
        move_vector *= 12
        self.position += move_vector

    def on_pick(self, game):
        pass