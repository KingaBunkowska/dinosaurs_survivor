from game_mechanics.Entity import Entity
import pygame

class Entity_preseter:
    def __init__(self, entity:Entity, color = (255, 0, 0), width=50, height=100):
        self.entity = entity
        self.color = color
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.entity.position, [self.width, self.height]))

