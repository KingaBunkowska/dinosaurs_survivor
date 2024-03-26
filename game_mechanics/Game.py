from game_mechanics.Player import Player
from game_mechanics.Dinosaur import Dinosaur

class Game:
    def __init__(self):
        self.player = Player()
        self.dinosaurs = []

        # for tests purposes
        self.dinosaurs.append(Dinosaur(position=[700, 700]))
        self.dinosaurs.append(Dinosaur(position=[100, 100]))

    
    def run_tick(self):
        for dinosaur in self.dinosaurs:
            dinosaur.move(self.player.position)
