from game_mechanics.PickableItems import PickableItems
from game_mechanics.Hitbox import Hitbox
from gui.Sprite import Sprite
import pygame

class PickableItemSprite(Sprite):
    def __init__(self, item: PickableItems, image):        
        super().__init__(item, image)
        self.item = item
        self.hitbox = Hitbox(self.item.position)