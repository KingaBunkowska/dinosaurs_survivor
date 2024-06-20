from game_mechanics.Player import Player
from GameMode import GameMode
from game_mechanics.active_abilities.Dash import Dash
from game_mechanics.active_abilities.Fire import Fire
from game_mechanics.active_abilities.Heal import Heal
from game_mechanics.active_abilities.PutSpikes import PutSpikes
from game_mechanics.active_abilities.SlowDownTime import SlowDownTime
from gui.ActivatableRect import ActivatableRect
from gui.ShopKeeperSprite import ShopKeeperSprite
from game_mechanics.ShopKeeper import ShopKeeper
from gui.PlayerSprite import PlayerSprite
from gui.ShopInterface import ShopInterface


class Pit:
    def __init__(self, screen, inventory):
        self.player = Player()
        self.inventory = inventory
        self.inventory.new_player(self.player)
        self.player_sprite = PlayerSprite(self.player)
        self.screen = screen
        self.keeper = ShopKeeper(self.inventory)
        self.keeper_sprite = ShopKeeperSprite()
        self.shop_interface = ShopInterface(self.keeper)

        self.abilities_rects = [ActivatableRect(x, 100, screen, Dash(self.player, None)) for x in [350, 450, 700, 800, 1050]]
        self.player_abilities = [Dash, Heal, Fire, PutSpikes, SlowDownTime]
        [ability.set_image(self.player_abilities[i]) for i, ability in enumerate(self.abilities_rects)]
        self.abilities_chosen = [1, 1, 0, 0, 0]
        self.last_chosen_i = 1

    def run_tick(self):
        self.keeper_sprite.draw(self.screen)
        self.player_sprite.draw(self.screen)
        [rect.draw(((self.abilities_chosen[i]+1)%2)*100) for i, rect in enumerate(self.abilities_rects)]

        if self.player_sprite.hitbox.collide(self.keeper_sprite.hitbox):
            self.shop_interface.draw(self.screen)
        else:
            self.check_abilities_collision()

    def check_gamemode_change(self):
        if self.player.get_position().x >= self.screen.get_width() - 100: return GameMode.GAME
        return None

    def click_buttons(self, click_pos):
        if self.player_sprite.hitbox.collide(self.keeper_sprite.hitbox):
            for i, offer in enumerate(self.shop_interface.offers):
                if offer.button_rect.collidepoint(click_pos):
                    self.shop_interface.apply_choice(i)

    def check_abilities_collision(self):
        for i, ability_rect in enumerate(self.abilities_rects):
            if self.player_sprite.hitbox.collide(ability_rect.hitbox) and self.abilities_chosen[i] == 0:
                self.check_ability(i)

    def check_ability(self, chosen_i):
        for i in range(len(self.player_abilities)):
            if self.abilities_chosen[i] == 1 and self.last_chosen_i != i and i!=chosen_i:
                self.abilities_chosen[i] = 0
                break

        self.abilities_chosen[chosen_i] = 1
        self.last_chosen_i = chosen_i

