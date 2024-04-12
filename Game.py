from game_mechanics.Player import Player
from game_mechanics.Dinosaur import Dinosaur
from gui.Entity_presenter import Entity_preseter

class Game:
    def __init__(self, screen):
        self.player = Player()
        self.dinosaurs = []
        self.dinosaur_presenters = []
        self.screen = screen

    
    def run_tick(self):
        for dinosaur in self.dinosaurs:
            dinosaur.move(self.player.position)

        for presenter in self.dinosaur_presenters:
            presenter.draw(self.screen)

    def _add_dinosaur(self, dinosaur:Dinosaur) -> None:
        self.dinosaurs.append(dinosaur)
        self.dinosaur_presenters.append(Entity_preseter(dinosaur, dino=True, width=200, height=200))