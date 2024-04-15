from game_mechanics.Player import Player
from game_mechanics.Dinosaur import Dinosaur
from gui.Player_presenter import Player_presenter
from gui.Dinosaur_presenter import Dinosaur_presenter
from gui. Attack_presenter import Attack_preseter
from game_mechanics.Attack import Attack
from game_mechanics.Position import Position
from game_mechanics.Weapon import Weapon

class Game:
    def __init__(self, screen):
        self.player = Player()
        self.dinosaurs = []
        self.dinosaur_presenters = []
        self.screen = screen
        self.projectiles = []
        self.projectiles_presenters = []
        self.player_presenter = Player_presenter(self.player)
        self.attack_interval = 0
        self.invincibility_frames = 100
        self.weapon = Weapon(self.player)

    def run_tick(self):
        self.player._use_up_invincibility()

        # automatic attack
        self.attack_interval += 1
        if self.attack_interval == self.player.statistics.attack_speed:
            self.attack_interval = 0
            self.player_attack()
        self.check_colisions()


        for i,dinosaur in enumerate(self.dinosaurs):
            dinosaur.move(self.player.position)
            if dinosaur.statistics.hp <= 0:
                self.dinosaurs[i] = None
                self.dinosaur_presenters[i] = None
        # remove dinosaurs that disappeared
        self.dinosaur_presenters = [d for d in self.dinosaur_presenters if d != None]
        self.dinosaurs = [d for d in self.dinosaurs if d != None]

        self.player_presenter.draw(self.screen)

        for presenter in self.dinosaur_presenters:
            presenter.draw(self.screen)

        for i, projectile in enumerate(self.projectiles):
            if projectile.range <= 0:
                self.projectiles[i] = None
                self.projectiles_presenters[i] = None
            else:
                projectile.fly()
        # remove projectiles that disappeared/
        self.projectiles_presenters = [p for p in self.projectiles_presenters if p != None]
        self.projectiles = [p for p in self.projectiles if p != None]

        for presenter in self.projectiles_presenters:
            presenter.draw(self.screen)

    def compare_hitbox(self, colision_point, hitbox):
        """
        Checks whether projectile collides with dinosaru
        :param colision_point: "arrowhead" of projectile
        :type colision_point: Position
        :param hitbox: two vertices(upper left and lower right) of dinosaur's collision rectangle
        :type hitbox: (Position, Position)
        :return:
        """
        if colision_point.following(hitbox[0]) and colision_point.proceeding(hitbox[1]):
            return True
        return False

    def check_colisions(self):
        """
        Check whether any projectile or Player hit any Dinosaur
        """
        for dinosaur in self.dinosaur_presenters:
            rect1 = dinosaur.hitbox
            rect2 = self.player_presenter.hitbox
            if not (rect1[0].x > rect2[1].x or rect2[0].x > rect1[1].x or
                    rect1[0].y > rect2[1].y or rect2[0].y > rect1[1].y):
                self.player._receive_damage(dinosaur.entity.statistics.contact_damage,self.invincibility_frames)
                dinosaur.entity._receive_damage(self.player.statistics.contact_damage)
                break

        to_del = []

        for i,projectiles_presenter in enumerate(self.projectiles_presenters):
            for dinosaur in self.dinosaur_presenters:
                if (self.compare_hitbox(projectiles_presenter.colision_point, dinosaur.hitbox) and not
                projectiles_presenter.attack.penetrate):
                    dinosaur.entity._receive_damage(projectiles_presenter.attack.calculate_dammage())
                    to_del.append(i)
                    break
        self.projectiles_presenters = [p for i, p in enumerate(self.projectiles_presenters) if i not in to_del]
        self.projectiles = [p for i, p in enumerate(self.projectiles) if i not in to_del]

    def _add_dinosaur(self, dinosaur: Dinosaur) -> None:
        self.dinosaurs.append(dinosaur)
        self.dinosaur_presenters.append(Dinosaur_presenter(dinosaur, self.player))

    def player_attack(self) -> None:
        """
        Use current weapon to generate projectiles and add them to view.
        """
        if self.dinosaurs:
            nearest_dinosaur = min(self.dinosaurs, key=lambda dino: self.player.position.distance(dino.position))

            projectiles = self.weapon.fire_attack(nearest_dinosaur.position)
            self.projectiles += projectiles
            self.projectiles_presenters += [Attack_preseter(p) for p in projectiles]
