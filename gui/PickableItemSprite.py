from gui.EntitySprite import EntitySprite
from game_mechanics.PickableItems import PickableItems
from game_mechanics.Player import Player
from game_mechanics.Position import Position
import pygame

class PickableItemSprite:
    def __init__(self, item: PickableItems, image):
        self.item = item
        self.size, _ = image.get_size() if image != None else (25, 25), 50
        self.image = image
        self.hitbox = self.item.position

    def draw(self, screen):
        self.hitbox = self.item.position
        screen.blit(self.image,  self.item.get_position().to_coords(*self.size))