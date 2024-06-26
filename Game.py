import random
from game_mechanics.Boss import Boss
from game_mechanics.DinosaurType import DinosaurType
from game_mechanics.Player import Player
from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.active_abilities.Dash import Dash
from game_mechanics.active_abilities.Fire import Fire
from game_mechanics.active_abilities.Heal import Heal
from game_mechanics.active_abilities.PutSpikes import PutSpikes
from game_mechanics.active_abilities.SlowDownTime import SlowDownTime
from game_mechanics.structures.Bush import Bush
from gui.StructureSprite import StructureSprite
from gui.BossSprite import BossSprite
from gui.GameOver import GameOver
from gui.AbilitySprite import AbilitySprite
from gui.HealthBar import HealthBar
from gui.ActivatableRect import ActivatableRect
from gui.PlayerSprite import PlayerSprite
from gui.DinosaurSprite import DinosaurSprite
from gui.AttackSprite import AttackSprite
from game_mechanics.Position import Position
from gui.LevelUpMenu import LevelUpMenu
from game_mechanics.Weapons.Pistol import Pistol
from game_mechanics.Weapons.Pickaxe import Pickaxe
from game_mechanics.Weapons.Rifle import Rifle
from game_mechanics.Weapons.Shotgun import Shotgun
from game_mechanics.PickableWeapon import PickableWeapons
from gui.PickableWeaponSprite import PickableWeaponSprite
from game_mechanics.Weapons.Blowtorch import Blowtorch
from game_mechanics.Weapons.Laser import Laser
from game_mechanics.Weapons.Chakra import Chakra
from GameMode import GameMode
from utils.PositionGenerator import PositionGenerator


class Game:
    def __init__(self, screen, inventory, abilities):
        self.player = Player()
        self.inventory = inventory
        self.inventory.new_player(self.player)
        self.dinosaur_sprites = []
        self.screen = screen
        self.projectiles_sprites = []
        self.enemy_projectiles_sprites = []
        self.player_sprite = PlayerSprite(self.player)
        self.pickable_sprites = []
        self.invincibility_frames = 100
        self.option_cooldown_frames = 0

        self.weapon = Pistol(self.player)
        self.inventory.pistol_upgrade(self.weapon)

        self.time_of_contact_damage = 10

        self.option = []

        self.player_abilities = [Dash, Heal, Fire, PutSpikes, SlowDownTime]

        self.active_abilities = [ability(self.player, self) for i, ability in enumerate(self.player_abilities) if abilities[i]]
        self.active_abilities_gui = [ActivatableRect(800 + 50 * i, 20, screen, self.active_abilities[i])
                                     for i in range(2)]

        for i, gui in enumerate(self.active_abilities_gui):
            gui.set_image(self.active_abilities[i])

        self.health_bar_gui = HealthBar(50, 30, self.player.statistics.max_hp, self.screen)
        self.ability_sprites_and_duration = []
        self.delayed_actions = []  # elem [method, ticks_from_now_to_use]
        self.running = True

        self.structures_sprites = []

        self.delayed_actions.append([self.spawn_boss, 10800])  # spawn boss after 3 minutes
        # self.delayed_actions.append([self.spawn_boss, 240]) # presentation
        self.ticks_from_start = 0
        self.ticks_from_spawn = 0

        [self.add_dinosaur(
            Dinosaur(DinosaurType.SILESAURUS, False, position=PositionGenerator.generate_near_border_position())) for _
         in range(2)]
        self.spawn_dinosaur()


    @property
    def friendly_dinosaurs(self):
        return [dinosaur_sprite for dinosaur_sprite in self.dinosaur_sprites if dinosaur_sprite is not None and dinosaur_sprite.dinosaur.ally]
    
    def run_tick(self):
        if self.running:
            self.ticks_from_start += 1
            self.ticks_from_spawn += 1
            self.option_cooldown_frames += 1
            self.player.use_up_invincibility()
            self.do_delayed_actions()
            self.draw_abilities()
            self.draw_gui()
            self.player_attack()
            self.check_collisions()

            for dinosaur_sprite in self.dinosaur_sprites:
                dinosaur_sprite.dinosaur.use_up_invincibility()



            enemy_dinosaurs_sprites = [dinosaur_sprite for dinosaur_sprite in self.dinosaur_sprites if
                                       not dinosaur_sprite.dinosaur.ally]
            enemy_dinosaurs = [dinosaur_sprite.dinosaur for dinosaur_sprite in enemy_dinosaurs_sprites]
            
            if random.randint(300, 600) < self.ticks_from_spawn or len(enemy_dinosaurs_sprites) == 0:
                self.spawn_dinosaur()
                if len(self.structures_sprites)<10:
                    self.spawn_bushes()
                self.ticks_from_spawn = 0

            for i, dino in enumerate(self.dinosaur_sprites):
                dino.entity.move(self.player.position,
                                 enemy_dinosaurs)
                if dino.entity.statistics.hp <= 0:
                    self.pickable_sprites.append(dino.entity.drop_items(self))
                    self.dinosaur_sprites[i] = None
                    if self.player.get_experience(dino.entity.give_exp()):
                        self.make_option()
            # remove dinosaurs that disappeared
            self.dinosaur_sprites = [d for d in self.dinosaur_sprites if d is not None]

            self.dinosaur_sprites = [dinosaur_sprite for dinosaur_sprite in self.dinosaur_sprites if
                                     dinosaur_sprite.dinosaur.statistics.hp >= 0]

            self.player_sprite.draw(self.screen)

            self.dinosaur_sprites.sort(key=lambda presenter: presenter.entity.get_position().to_coords()[1])

            for presenter in self.dinosaur_sprites:
                presenter.draw(self.screen)

            self.pickable_sprites = [c for c in self.pickable_sprites if c is not None]

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
            self.projectiles_sprites = [p for p in self.projectiles_sprites if p is not None]

            for i, projectile in enumerate(self.enemy_projectiles_sprites):
                if projectile.attack.range <= 0:
                    self.projectiles_sprites[i] = None
                else:
                    projectile.attack.fly()

            # remove projectiles that disappeared
            self.enemy_projectiles_sprites = [p for p in self.enemy_projectiles_sprites if p is not None]

            for sprite in self.projectiles_sprites:
                sprite.draw(self.screen)

            for sprite in self.enemy_projectiles_sprites:
                sprite.draw(self.screen)


            if self.option:
                self.option[0].draw(self.screen)

            self.trigger_structures()
            self.clean_structures()
            self.draw_structures()

    def check_collisions(self):
        """
        Check whether any projectile or Player hit any Dinosaur
        """

        enemy_sprites = [dino_sprite for dino_sprite in self.dinosaur_sprites if not dino_sprite.dinosaur.ally]
        ally_sprites = [dino_sprite for dino_sprite in self.dinosaur_sprites if dino_sprite.dinosaur.ally]

        for dinosaur in enemy_sprites:
            if not dinosaur.dinosaur.ally:
                if dinosaur.hitbox.collide(self.player_sprite.hitbox):
                    self.player.receive_damage(dinosaur.entity.statistics.contact_damage, self.invincibility_frames)
                    dinosaur.entity.receive_damage(self.player.statistics.contact_damage, self.player)
                    break

        self.time_of_contact_damage += 1
        # if self.time_of_contact_damage % 40 == 0:

        for ally_sprite in ally_sprites:

            dinosaurs_hitted = 0

            for enemy_sprite in enemy_sprites:
                if ally_sprite.hitbox.collide(enemy_sprite.hitbox) and dinosaurs_hitted < 3:
                    dinosaurs_hitted += 1
                    enemy_sprite.dinosaur.receive_damage(ally_sprite.dinosaur.statistics.contact_damage,
                                                         ally_sprite.dinosaur)

        for i,pickable in enumerate(self.pickable_sprites):
            if pickable.hitbox.collide(self.player_sprite.hitbox):
                pickable.item.on_pick(self)
                self.pickable_sprites[i] = None

        to_del = []
        for i, projectiles_sprite in enumerate(self.projectiles_sprites):
            for dinosaur in enemy_sprites:
                if projectiles_sprite.hitbox.collide(dinosaur.hitbox):
                    dinosaur.entity.receive_damage(projectiles_sprite.attack.calculate_damage(dinosaur.entity))
                    if not projectiles_sprite.attack.penetrate: to_del.append(i)
                    break
        self.projectiles_sprites = [p for i, p in enumerate(self.projectiles_sprites) if i not in to_del]

        to_del = []
        for i, projectiles_sprite in enumerate(self.enemy_projectiles_sprites):
            if projectiles_sprite.hitbox.collide(self.player_sprite.hitbox):
                self.player.receive_damage(projectiles_sprite.attack.calculate_damage(self.player), self.invincibility_frames)
                to_del.append(i)
        self.enemy_projectiles_sprites = [p for i,p in enumerate(self.enemy_projectiles_sprites) if i not in to_del]

    def add_dinosaur(self, dinosaur: Dinosaur) -> None:
        self.dinosaur_sprites.append(DinosaurSprite(dinosaur, self.player))

    def player_attack(self) -> None:
        """
        Use current weapon to generate projectiles and add them to view.
        """
        if self.weapon.check_interval():
            enemy_dinosaurs = [dino_sprite for dino_sprite in self.dinosaur_sprites if not dino_sprite.dinosaur.ally]

            if enemy_dinosaurs:
                nearest_dinosaur = min(enemy_dinosaurs,
                                       key=lambda dino: self.player.position.distance(dino.entity.position))

                projectiles, projectiles_type = self.weapon.fire_attack(nearest_dinosaur.entity.position)
                self.projectiles_sprites += [AttackSprite(p, attack_type=projectiles_type) for p in projectiles]

    def make_option(self):
        self.option.append(LevelUpMenu(self.player.level))

    def resolve_option(self, nr):
        x, y = self.screen.get_size()
        x, y = x // 2, y // 2


        if self.option and not ((self.option[0].level == 5 or self.option[0].level == 10) and nr == 3) and self.option_cooldown_frames > 30:
            self.option_cooldown_frames = 0
            option = self.option.pop(0)
            lvl = option.level

            if lvl == 5:
                if nr == 1:
                    rifle = Rifle(self.player)
                    self.inventory.rifle_upgrade(rifle)
                    self.pickable_sprites.append(PickableWeaponSprite(PickableWeapons(Position(x, y), rifle)))
                if nr == 2:
                    pickaxe = Pickaxe(self.player)
                    self.inventory.pickaxe_upgrade(pickaxe)
                    self.pickable_sprites.append(
                        PickableWeaponSprite(PickableWeapons(Position(x, y), pickaxe)))

            if lvl == 10:
                if self.weapon.__class__ == Pickaxe:
                    if nr == 1:
                        blowtorch = Blowtorch(self.player)
                        self.inventory.blowtorch_upgrade(blowtorch)
                        self.pickable_sprites.append(
                            PickableWeaponSprite(PickableWeapons(Position(x, y), blowtorch)))
                    if nr == 2:
                        chakra = Chakra(self.player)
                        self.inventory.chakra_upgrade(chakra)
                        self.pickable_sprites.append(
                            PickableWeaponSprite(PickableWeapons(Position(x, y), chakra)))
                if self.weapon.__class__ == Rifle:
                    if nr == 1:
                        laser = Laser(self.player)
                        self.inventory.laser_upgrade(laser)
                        self.pickable_sprites.append(
                            PickableWeaponSprite(PickableWeapons(Position(x, y), laser)))
                    if nr == 2:
                        shotgun = Shotgun(self.player)
                        self.inventory.shotgun_upgrade(shotgun)
                        self.pickable_sprites.append(
                            PickableWeaponSprite(PickableWeapons(Position(x, y), shotgun)))
                print(self.weapon.accuracy, self.weapon.attack_nr)


            if lvl != 5 and lvl != 10:
                self.player.stat_up(10, nr)


    def draw_gui(self) -> None:
        self.health_bar_gui.update_max_health(self.player.statistics.max_hp)
        self.health_bar_gui.draw(self.player.statistics.hp)

        for i in range(len(self.active_abilities)):
            self.active_abilities[i].tick_actions()
            self.active_abilities_gui[i].set_image(self.active_abilities[i])
            self.active_abilities_gui[i].draw(self.active_abilities[i].percent_of_cooldown())

    def draw_abilities(self):
        self.ability_sprites_and_duration = [ability_and_duration for ability_and_duration in
                                             self.ability_sprites_and_duration if ability_and_duration[1] > 0]

        for i, (sprite, duration) in enumerate(self.ability_sprites_and_duration):
            sprite.draw(self.screen)
            self.ability_sprites_and_duration[i][1] -= 1

    def use_ability(self, i):
        if self.active_abilities[i].can_use():
            self.active_abilities[i].use()

            if self.active_abilities[i].name == "fire":
                self.ability_sprites_and_duration.append(
                    [AbilitySprite(self.player.position, self.active_abilities[i].name), 30])

            elif self.active_abilities[i].name == "heal":
                self.ability_sprites_and_duration.append([AbilitySprite(self.player.position,
                                                                        self.active_abilities[i].name,
                                                                        player=self.player, move_with_player=True), 30])

            elif self.active_abilities[i].name == "slow_down_time":
                self.ability_sprites_and_duration.append([AbilitySprite(self.player.position,
                                                                        self.active_abilities[i].name,
                                                                        player=self.player, move_with_player=True),
                                                          self.active_abilities[i].duration])
                self.delayed_actions.append([self.active_abilities[i].deactivate, self.active_abilities[i].duration])

    def do_delayed_actions(self):
        for i, (delayed_action, ticks_to_activation) in enumerate(self.delayed_actions):
            if ticks_to_activation == 0:
                delayed_action()

            self.delayed_actions[i][1] -= 1

        self.delayed_actions = [action_and_dur for action_and_dur in self.delayed_actions if action_and_dur[1] >= 0]

    def manage_game_over(self):
        if self.player.statistics.hp <= 0:
            GameOver().draw(self.screen)
            self.running = False

    def check_gamemode_change(self):
        if self.player.statistics.hp <= 0: return GameMode.PIT
        return None

    def click_buttons(self, click_pos):
        pass

    def add_structure(self, structure):
        if structure is None or structure.name is None:
            raise ValueError("Structure do not exist or do not have name value")
        
        self.structures_sprites.append(StructureSprite(structure))


    def trigger_structures(self):
        for structure_sprite in self.structures_sprites:
            structure = structure_sprite.structure
            structure.trigger(self.player)
            [structure.trigger(dino_sprite.dinosaur) for dino_sprite in self.dinosaur_sprites]

    def draw_structures(self):
        [structure.draw(self.screen) for structure in self.structures_sprites]

    def clean_structures(self):
        self.structures_sprites = [structure_sprite for structure_sprite in self.structures_sprites if
                                   structure_sprite.structure.exist]

    def spawn_boss(self):
        self.dinosaur_sprites.append(BossSprite(Boss(self)))

    def spawn_dinosaur(self):
        available_types = [d for d in DinosaurType if d != DinosaurType.POLONOSUCHUS]
        for i in range(random.randint(1, 3)):
            self.add_dinosaur(
                Dinosaur(type=random.choice(available_types), position=PositionGenerator.generate_near_border_position()))

    def spawn_random_dinosaur_at_location(self, position, friendly = False):
        available_types = [d for d in DinosaurType if d != DinosaurType.POLONOSUCHUS]
        self.add_dinosaur(Dinosaur(type=random.choice(available_types), position=position, friendly=friendly))

    def spawn_bushes(self):
        for i in range(random.randint(0,2)):
            self.add_structure(Bush(position=PositionGenerator.generate_position(), is_health_bush=random.randint(0, 1), game=self))
