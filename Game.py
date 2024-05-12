from game_mechanics.Player import Player
from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.active_abilities.Dash import Dash
from gui.HealthBar import HealthBar
from gui.ActivatableRect import ActivatableRect
from gui.PlayerSprite import PlayerSprite
from gui.DinosaurSprite import DinosaurSprite
from gui.AttackSprite import AttackSprite
from game_mechanics.Attack import Attack
from game_mechanics.Position import Position
from game_mechanics.Weapon import Weapon
from game_mechanics.Coin import Coin
from gui.PickableItemSprite import PickableItemSprite

class Game:
    def __init__(self, screen):
        self.player = Player()
        self.dinosaur_sprites = []
        self.screen = screen
        self.projectiles_sprites = []
        self.player_sprite = PlayerSprite(self.player)
        self.coin_sprites = []
        self.attack_interval = 0
        self.invincibility_frames = 100
        self.weapon = Weapon(self.player)
        self.time_of_contact_damage = 10

        self.active_ability = Dash(self.player)
        self.active_ability_gui = ActivatableRect(800, 20, screen)

        self.health_bar_gui = HealthBar(20, 20, self.player.statistics.max_hp, self.screen)

    def run_tick(self):
        self.player._use_up_invincibility()

        self.active_ability.tick_actions()
        self.active_ability_gui.set_image(self.active_ability.name)
        self.draw_gui()

        # automatic attack
        self.attack_interval += 1
        if self.attack_interval == self.player.statistics.attack_speed:
            self.attack_interval = 0
            self.player_attack()
        self.check_collisions()

        enemy_dinosaurs = [dinosaur_sprite for dinosaur_sprite in self.dinosaur_sprites if not dinosaur_sprite.dinosaur.ally]

        for i,dino in enumerate(self.dinosaur_sprites):
            dino.entity.move(self.player.position, [dino_sprite.dinosaur for dino_sprite in enemy_dinosaurs])
            if dino.entity.statistics.hp <= 0:
                self.coin_sprites.append(dino.entity.DropItems())
                self.dinosaur_sprites[i] = None
        # remove dinosaurs that disappeared
        self.dinosaur_sprites = [d for d in self.dinosaur_sprites if d != None]

        self.dinosaur_sprites = [dinosaur_sprite for dinosaur_sprite in self.dinosaur_sprites if dinosaur_sprite.dinosaur.statistics.hp >= 0]


        self.player_sprite.draw(self.screen)

        self.dinosaur_sprites.sort(key=lambda presenter: presenter.entity.get_position().to_coords()[1])

        for presenter in self.dinosaur_sprites:
            presenter.draw(self.screen)

        self.coin_sprites = [c for c in self.coin_sprites if c != None]

        for coin in self.coin_sprites:
            if self.player.position.distance(coin.item.position) <= self.player.statistics.pickup_range:
                coin.item.move(self.player.position)
            coin.draw(self.screen)


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
        :type colision_point: Position
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

        enemy_sprites = [dino_sprite for dino_sprite in self.dinosaur_sprites if not dino_sprite.dinosaur.ally]
        ally_sprites = [dino_sprite for dino_sprite in self.dinosaur_sprites if dino_sprite.dinosaur.ally]

        for dinosaur in enemy_sprites:
            if dinosaur.dinosaur.ally == False:
                rect1 = dinosaur.hitbox
                rect2 = self.player_sprite.hitbox
                if not (rect1[0].x > rect2[1].x or rect2[0].x > rect1[1].x or
                        rect1[0].y > rect2[1].y or rect2[0].y > rect1[1].y):
                    self.player._receive_damage(dinosaur.entity.statistics.contact_damage, self.invincibility_frames)
                    dinosaur.entity._receive_damage(self.player.statistics.contact_damage)
                    break

        self.time_of_contact_damage += 1
        if self.time_of_contact_damage % 40 == 0:
        
            for ally_sprite in ally_sprites:
                rect1 = ally_sprite.hitbox

                dinosaurs_hitted = 0
                
                for enemy_sprite in enemy_sprites:
                    rect2 = enemy_sprite.hitbox
                    if (not (rect1[0].x > rect2[1].x or rect2[0].x > rect1[1].x or
                            rect1[0].y > rect2[1].y or rect2[0].y > rect1[1].y) and
                            dinosaurs_hitted<3):
                        dinosaurs_hitted += 1
                        enemy_sprite.dinosaur._receive_damage(ally_sprite.dinosaur.statistics.contact_damage)

        for i,coin in enumerate(self.coin_sprites):
            if self.compare_hitbox(coin.hitbox,self.player_sprite.hitbox):
                coin.item.onPick(self.player)
                self.coin_sprites[i] = None

        to_del = []
        for i, projectiles_presenter in enumerate(self.projectiles_sprites):
            for dinosaur in enemy_sprites:
                if (self.compare_hitbox(projectiles_presenter.colision_point, dinosaur.hitbox) and not projectiles_presenter.attack.penetrate):
                    dinosaur.entity._receive_damage(projectiles_presenter.attack.calculate_dammage(dinosaur.entity))
                    to_del.append(i)
                    break
        self.projectiles_sprites = [p for i, p in enumerate(self.projectiles_sprites) if i not in to_del]

    def _add_dinosaur(self, dinosaur: Dinosaur) -> None:
        self.dinosaur_sprites.append(DinosaurSprite(dinosaur, self.player))

    def player_attack(self) -> None:
        """
        Use current weapon to generate projectiles and add them to view.
        """

        enemy_dinosaurs = [dino_sprite for dino_sprite in self.dinosaur_sprites if not dino_sprite.dinosaur.ally]

        if enemy_dinosaurs:
            nearest_dinosaur = min(enemy_dinosaurs, key=lambda dino: self.player.position.distance(dino.entity.position))

            projectiles = self.weapon.fire_attack(nearest_dinosaur.entity.position)
            self.projectiles_sprites += [AttackSprite(p) for p in projectiles]

    def draw_gui(self) -> None:
        self.health_bar_gui.update_max_health(self.player.statistics.max_hp)
        self.active_ability_gui.draw(self.active_ability.percent_of_cooldown())
        self.health_bar_gui.draw(self.player.statistics.hp)
