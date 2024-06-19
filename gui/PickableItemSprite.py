from gui.EntitySprite import EntitySprite
from game_mechanics.PickableItems import PickableItems
from game_mechanics.Player import Player
from game_mechanics.Position import Position
from game_mechanics.Hitbox import Hitbox
from gui.Sprite import Sprite
import pygame

class PickableItemSprite(Sprite):
    def __init__(self, item: PickableItems, image):        
        super().__init__(item, image)
        self.item = item
        self.hitbox = Hitbox(self.item.position)


    # def draw(self, screen):
    #     screen.blit(self.image, self.item.get_position().to_coords(*self.size))