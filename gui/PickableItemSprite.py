from gui.EntitySprite import EntitySprite
from game_mechanics.PickableItems import PickableItems
from game_mechanics.Player import Player
from game_mechanics.Position import Position
import pygame

IMAGE = pygame.image.load('resources/gold_coin.png')

SIZE_OF_IMAGE = [30, 30]

class PickableItemSprite:
    def __init__(self, item: PickableItems):
        self.item = item
        image = pygame.transform.scale(IMAGE, SIZE_OF_IMAGE)
        self.size = image.get_size()
        self.image = image
        self.hitbox = (Position(self.item.position.x - self.size[0] / 2, self.item.position.y - self.size[1] / 2),
                       Position(self.item.position.x + self.size[0] / 2, self.item.position.y + self.size[1] / 2))

    def draw(self, screen):
        self.hitbox = (Position(self.item.position.x - self.size[0] / 2, self.item.position.y - self.size[1] / 2),
                       Position(self.item.position.x + self.size[0] / 2, self.item.position.y + self.size[1] / 2))
        screen.blit(self.image,  self.item.get_position().to_coords(*self.size))