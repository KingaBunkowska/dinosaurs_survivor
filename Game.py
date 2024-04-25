from game_mechanics.Player import Player
from game_mechanics.Dinosaur import Dinosaur
from gui.PlayerSprite import PlayerSprite
from gui.DinosaurSprite import DinosaurSprite
from gui.AttackSprite import AttackSprite
from game_mechanics.Attack import Attack
from game_mechanics.Position import Position
from game_mechanics.Weapon import Weapon

class Game:
    def __init__(self, screen):
        self.player = Player()
        self.dinosaur_sprites = []
        self.screen = screen
        self.projectiles_sprites = []
        self.player_presenter = PlayerSprite(self.player)
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
        self.check_collisions()


        for i,dinosaur in enumerate(self.dinosaur_sprites):
            dinosaur.entity.move(self.player.position)
            if dinosaur.entity.statistics.hp <= 0:
                self.dinosaur_sprites[i] = None
        # remove dinosaurs that disappeared
        self.dinosaur_sprites = [d for d in self.dinosaur_sprites if d != None]

        self.player_presenter.draw(self.screen)

        self.dinosaur_sprites.sort(key=lambda presenter: presenter._get_entity().get_position().to_coords()[1])

        for presenter in self.dinosaur_sprites:
            presenter.draw(self.screen)

        for i, projectile in enumerate(self.projectiles_sprites):
            if projectile.attack.range <= 0:
                self.projectiles_sprites[i] = None
            else:
                projectile.attack.fly()
        # remove projectiles that disappeared
        self.projectiles_sprites = [p for p in self.projectiles_sprites if p != None]

        for presenter in self.projectiles_sprites:
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

    def check_collisions(self):
        """
        Check whether any projectile or Player hit any Dinosaur
        """
        for dinosaur in self.dinosaur_sprites:
            rect1 = dinosaur.hitbox
            rect2 = self.player_presenter.hitbox
            if not (rect1[0].x > rect2[1].x or rect2[0].x > rect1[1].x or
                    rect1[0].y > rect2[1].y or rect2[0].y > rect1[1].y):
                self.player._receive_damage(dinosaur.entity.statistics.contact_damage,self.invincibility_frames)
                dinosaur.entity._receive_damage(self.player.statistics.contact_damage)
                break

        to_del = []

        for i,projectiles_presenter in enumerate(self.projectiles_sprites):
            for dinosaur in self.dinosaur_sprites:
                if (self.compare_hitbox(projectiles_presenter.colision_point, dinosaur.hitbox) and not
                projectiles_presenter.attack.penetrate):
                    dinosaur.entity._receive_damage(projectiles_presenter.attack.calculate_dammage())
                    to_del.append(i)
                    break
        self.projectiles_sprites = [p for i, p in enumerate(self.projectiles_sprites) if i not in to_del]

    def _add_dinosaur(self, dinosaur: Dinosaur) -> None:
        self.dinosaur_sprites.append(DinosaurSprite(dinosaur, self.player))

    def player_attack(self) -> None:
        """
        Use current weapon to generate projectiles and add them to view.
        """
        if self.dinosaur_sprites:
            nearest_dinosaur = min(self.dinosaur_sprites, key=lambda dino: self.player.position.distance(dino.entity.position))

            projectiles = self.weapon.fire_attack(nearest_dinosaur.entity.position)
            self.projectiles_sprites += [AttackSprite(p) for p in projectiles]
