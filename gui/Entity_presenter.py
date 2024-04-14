from game_mechanics.Entity import Entity
import pygame
from game_mechanics.Dinosaur_type import Dinosaur_type

class Entity_presenter:
    def __init__(self, entity:Entity, image):
        self.entity = entity
        self.width, self.height = image.get_size() if image!=None else 50, 100
        self.image = image


    def draw(self, screen):
        if self.entity.facing_right:
            rotated_image = pygame.transform.flip(self.image, True, False)
            screen.blit(rotated_image, self.entity.get_position().to_coords())
        else:
            screen.blit(self.image,  self.entity.get_position().to_coords())

    def _get_entity(self):
        return self.entity
    
