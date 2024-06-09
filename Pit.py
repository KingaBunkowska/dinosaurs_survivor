from game_mechanics.Player import Player
from GameMode import GameMode
from gui.ShopKeeperSprite import ShopKeeperSprite
from game_mechanics.ShopKeeper import ShopKeeper
from gui.PlayerSprite import PlayerSprite
from gui.ShopInterface import ShopInterface

class Pit:
    def __init__(self, screen):
        self.player = Player()
        self.player_sprite = PlayerSprite(self.player)
        self.screen = screen
        self.keeper = ShopKeeper()
        self.keeper_sprite = ShopKeeperSprite()
        self.shop_interface = ShopInterface(self.keeper)

    def run_tick(self):
        self.keeper_sprite.draw(self.screen)
        self.player_sprite.draw(self.screen)


        if not (self.player_sprite.hitbox[0].x > self.keeper_sprite.hitbox[1].x or self.keeper_sprite.hitbox[0].x > self.player_sprite.hitbox[1].x or
                self.player_sprite.hitbox[0].y > self.keeper_sprite.hitbox[1].y or self.keeper_sprite.hitbox[0].y > self.player_sprite.hitbox[1].y):
            self.shop_interface.draw(self.screen)

    def check_gamemode_change(self):
        if self.player.get_position().x >= self.screen.get_width() - 100: return GameMode.GAME
        return None