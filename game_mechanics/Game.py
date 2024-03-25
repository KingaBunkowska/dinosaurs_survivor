from game_mechanics.Player import Player
from game_mechanics.Dinosaur import Dinosaur

class Game:
    def __init__(self):
        self.player = Player()
        self.dinosaurs = []

        # for tests purposes
        self.dinosaurs.append(Dinosaur())
