from game_mechanics.Entity import Entity
import pygame

class Entity_preseter:
    def __init__(self, entity:Entity):
        self.entity = entity

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.entity.position, [25, 25]))

