from game_mechanics.Entity import Entity
from game_mechanics.Statistics import Statistics

class Player(Entity):
    def __init__(self):
        super().__init__(statistics=Statistics(speed=10))
