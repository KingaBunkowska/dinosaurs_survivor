from game_mechanics.Player import Player
from game_mechanics.Dinosaur import Dinosaur
from gui.Entity_presenter import Entity_preseter
from gui. Attack_presenter import Attack_preseter
from game_mechanics.Attack import Attack
from game_mechanics.Position import Position
import pygame


class Game:
    def __init__(self, screen):
        self.player = Player()
        self.dinosaurs = []
        self.dinosaur_presenters = []
        self.screen = screen
        self.projectiles = []
        self.projectiles_presenters = []

    def run_tick(self):
        self.check_colisions()

        for dinosaur in self.dinosaurs:
            dinosaur.move(self.player.position)

        for presenter in self.dinosaur_presenters:
            presenter.draw(self.screen)

        for projectile in self.projectiles:
            projectile.fly()

        for presenter in self.projectiles_presenters:
            presenter.draw(self.screen)

    def compare_hitbox(self,rect1,rect2):
        """
        Function tells whether rectangles 1 and 2 colide
        :param rect1: First rectangle
        :param rect2:
        :return: boolean
        """
        if (rect1[0].x > rect2[1].x or rect2[0].x > rect1[1].x or
                rect1[0].y > rect2[1].y or rect2[0].y > rect1[1].y):
            return False
        else:
            return True

    def check_colisions(self):
        """
        Check whether any projectile hit any Entity.
        """
        to_del = []
        for i in range(len(self.projectiles_presenters)):
            for dinosaur in self.dinosaur_presenters:
                v2 = Position(self.projectiles_presenters[i].attack.position.x + self.projectiles_presenters[i].width,
                              self.projectiles_presenters[i].attack.position.y + self.projectiles_presenters[i].height)
                v4 = Position(dinosaur.entity.position.x + dinosaur.width, dinosaur.entity.position.y + dinosaur.height)

                # TODO : In projectile presenter calculate (and store) the "arrowhead"
                rect1 = (self.projectiles_presenters[i].attack.position, v2)
                rect2 = (dinosaur.entity.position, v4)

                if (self.compare_hitbox(rect1, rect2)): #PLACEHOLDER
                    print("Ale urwał! Ale to było dobre! (chociaż można terz wywołać jakąś funkcje)")
                    to_del.append(i)
        self.projectiles_presenters = [p for i, p in enumerate(self.projectiles_presenters) if i not in to_del]


    def _add_dinosaur(self, dinosaur: Dinosaur) -> None:
        self.dinosaurs.append(dinosaur)
        self.dinosaur_presenters.append(Entity_preseter(dinosaur, dino=True, width=200, height=200))

    def player_attack(self) -> None:
        if self.dinosaurs:
            nearest_dinosaur = min(self.dinosaurs, key=lambda dino: self.player.position.distance(dino.position))

            projectile = Attack(nearest_dinosaur.position, self.player)
            self.projectiles.append(projectile)
            self.projectiles_presenters.append(Attack_preseter(projectile))
        else:
            print(" Ludzie, przecież tu nikogo nie ma. Nikt nie atakuje Jasnej Góry. Co wy pierd****** za głupoty!")