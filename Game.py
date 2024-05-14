from game_mechanics.Player import Player
from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.active_abilities.Dash import Dash
from game_mechanics.active_abilities.Fire import Fire
from game_mechanics.active_abilities.Heal import Heal
from game_mechanics.active_abilities.SlowDownTime import SlowDownTime
from gui.GameOver import GameOver
from gui.AbilitySprite import AbilitySprite
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
from gui.LevelUpMenu import LevelUpMenu
from game_mechanics.Weapons.Pistol import Pistol
from game_mechanics.Weapons.Pickaxe import Pickaxe
from game_mechanics.Weapons.Rifle import Rifle
from game_mechanics.Weapons.Shotgun import Shotgun
from game_mechanics.PickableWeapon import PickableWeapons
from gui.PickableWeaponSprite import PickableWeaponSprite

class Game:
    def __init__(self, screen):
        self.player = Player()
        self.dinosaur_sprites = []
        self.screen = screen
        self.projectiles_sprites = []
        self.player_sprite = PlayerSprite(self.player)
        self.pickable_sprites = []
        self.invincibility_frames = 100
        self.weapon = Pistol(self.player)
        self.time_of_contact_damage = 10

        self.option = None
        self.active_abilities = [SlowDownTime(self.player, self), Dash(self.player)]
        self.active_abilities_gui = [ActivatableRect(800 + 50 * i, 20, screen, self.active_abilities[i])
                                     for i in range(2)]

        for i, gui in enumerate(self.active_abilities_gui):
            gui.set_image(self.active_abilities[i])

        self.health_bar_gui = HealthBar(20, 20, self.player.statistics.max_hp, self.screen)
        
        self.ability_sprites_and_duration = []

        self.delayed_actions = []

        self.running = True

    def run_tick(self):
        self.check_game_over()

        if self.running:
            self.player._use_up_invincibility()
            self.do_delayed_actions()
            self.draw_abilities()
            self.draw_gui()

        self.player_attack()
        self.check_collisions()

         enemy_dinosaurs = [dinosaur_sprite for dinosaur_sprite in self.dinosaur_sprites if not dinosaur_sprite.dinosaur.ally]

        for i,dino in enumerate(self.dinosaur_sprites):
            dino.entity.move(self.player.position, [dino_sprite.dinosaur for dino_sprite in enemy_dinosaurs])
            if dino.entity.statistics.hp <= 0:
                self.pickable_sprites.append(dino.entity.DropItems())
                self.dinosaur_sprites[i] = None
                if self.player.get_experience(dino.entity.give_exp()):
                    self.make_option()
        # remove dinosaurs that disappeared
        self.dinosaur_sprites = [d for d in self.dinosaur_sprites if d != None]

            self.dinosaur_sprites = [dinosaur_sprite for dinosaur_sprite in self.dinosaur_sprites if dinosaur_sprite.dinosaur.statistics.hp >= 0]


            self.player_sprite.draw(self.screen)

            self.dinosaur_sprites.sort(key=lambda presenter: presenter.entity.get_position().to_coords()[1])

            for presenter in self.dinosaur_sprites:
                presenter.draw(self.screen)

        self.pickable_sprites = [c for c in self.pickable_sprites if c != None]

        for pickable in self.pickable_sprites:
            if self.player.position.distance(pickable.item.position) <= self.player.statistics.pickup_range:
                pickable.item.move(self.player.position)
            pickable.draw(self.screen)


            for i, projectile in enumerate(self.projectiles_sprites):
                if projectile.attack.range <= 0:
                    self.projectiles_sprites[i] = None
                else:
                    projectile.attack.fly()

            # remove projectiles that disappeared
            self.projectiles_sprites = [p for p in self.projectiles_sprites if p != None]

            for presenter in self.projectiles_sprites:
                presenter.draw(self.screen)

        if self.option != None:
            self.option.draw(self.screen)

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

        for i,pickable in enumerate(self.pickable_sprites):
            if self.compare_hitbox(pickable.hitbox,self.player_sprite.hitbox):
                pickable.item.onPick(self)
                self.pickable_sprites[i] = None

        to_del = []
        for i, projectiles_presenter in enumerate(self.projectiles_sprites):
            for dinosaur in enemy_sprites:
                if self.compare_hitbox(projectiles_presenter.colision_point, dinosaur.hitbox):
                    dinosaur.entity._receive_damage(projectiles_presenter.attack.calculate_dammage(dinosaur.entity))
                    if not projectiles_presenter.attack.penetrate: to_del.append(i)
                    break
        self.projectiles_sprites = [p for i, p in enumerate(self.projectiles_sprites) if i not in to_del]

    def _add_dinosaur(self, dinosaur: Dinosaur) -> None:
        self.dinosaur_sprites.append(DinosaurSprite(dinosaur, self.player))

    def player_attack(self) -> None:
        """
        Use current weapon to generate projectiles and add them to view.
        """
        if self.weapon.check_interval():
            enemy_dinosaurs = [dino_sprite for dino_sprite in self.dinosaur_sprites if not dino_sprite.dinosaur.ally]

            if enemy_dinosaurs:
                nearest_dinosaur = min(enemy_dinosaurs, key=lambda dino: self.player.position.distance(dino.entity.position))

                projectiles, projectiles_type = self.weapon.fire_attack(nearest_dinosaur.entity.position)
                self.projectiles_sprites += [AttackSprite(p,attack_type=projectiles_type) for p in projectiles]

    def make_option(self):
        self.option = LevelUpMenu(self.player.level)
    def resolve_option(self,option):
        if self.player.level == 5:
            if option == 1:
                # self.weapon = Rifle(self.player)
                self.pickable_sprites.append(PickableWeaponSprite(PickableWeapons(Position(100,100),Rifle(self.player))))
            if option == 2:
                # self.weapon = Pickaxe(self.player)
                self.pickable_sprites.append(
                    PickableWeaponSprite(PickableWeapons(Position(100, 100), Pickaxe(self.player))))
        if self.player.level == 10:
            if self.weapon.__class__ == Pickaxe:
                if option == 1:
                    self.weapon = Pistol(self.player)
                if option == 2:
                    self.weapon = Pickaxe(self.player)
            if self.weapon.__class__ == Rifle:
                if option == 1:
                    self.weapon = Pistol(self.player)
                if option == 2:
                    self.weapon = Shotgun(self.player)
            print(self.weapon.accuracy, self.weapon.attack_nr)
        if self.player.level != 5 and self.player.level != 10:
            self.player.stat_up(5,option)
        self.option = None

    def draw_gui(self) -> None:
        self.health_bar_gui.update_max_health(self.player.statistics.max_hp)
        self.health_bar_gui.draw(self.player.statistics.hp)

        for i in range(len(self.active_abilities)):
            self.active_abilities[i].tick_actions()
            self.active_abilities_gui[i].set_image(self.active_abilities[i])
            self.active_abilities_gui[i].draw(self.active_abilities[i].percent_of_cooldown())

    def draw_abilities(self):

        self.ability_sprites_and_duration = [ability_and_duration for ability_and_duration in self.ability_sprites_and_duration if ability_and_duration[1]>0]
        
        for i, (sprite, duration) in enumerate(self.ability_sprites_and_duration):
            sprite.draw(self.screen)
            self.ability_sprites_and_duration[i][1] -= 1

    def use_ability(self, i):
        if self.active_abilities[i].can_use():
            self.active_abilities[i].use()

            if self.active_abilities[i].name == "fire":
                self.ability_sprites_and_duration.append([AbilitySprite(self.player.position, self.active_abilities[i].name), 30])

            elif self.active_abilities[i].name == "heal":
                self.ability_sprites_and_duration.append([AbilitySprite(self.player.position, self.active_abilities[i].name, player=self.player, move_with_player=True), 30])

            elif self.active_abilities[i].name == "slow_down_time":
                self.ability_sprites_and_duration.append([AbilitySprite(self.player.position, self.active_abilities[i].name, player=self.player, move_with_player=True), self.active_abilities[i].duration])
                self.delayed_actions.append([self.active_abilities[i].deactivate, self.active_abilities[i].duration])

    def do_delayed_actions(self):
        for i, (delayed_action, ticks_to_activation) in enumerate(self.delayed_actions):
            if ticks_to_activation == 0:
                delayed_action()

            self.delayed_actions[i][1] -= 1

        self.delayed_actions = [action_and_dur for action_and_dur in self.delayed_actions if action_and_dur[1]>=0]

    def check_game_over(self):
        if self.player.statistics.hp <= 0:
            GameOver().draw(self.screen)
            self.running = False
