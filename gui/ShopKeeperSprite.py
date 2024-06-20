from game_mechanics.Position import Position
from gui.Sprite import Sprite
from game_mechanics.Hitbox import Hitbox
from utils.ImageLoader import ImageLoader
import pygame

class ShopKeeperSprite(Sprite):
    def __init__(self):
        self.image = ImageLoader.get_keeper()
        self.hitbox = Hitbox(Position(180,274),(150,150),(0,0))
    def draw(self,screen):
        screen.blit(self.image,self.hitbox.position.to_coords())

