from game_mechanics.Position import Position
from gui.Sprite import Sprite
import pygame

class ShopKeeperSprite(Sprite):
    def __init__(self):
        self.hitbox = (Position(230,230),Position(380,380))
    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,255),[230,230,150,150])
