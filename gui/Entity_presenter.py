from game_mechanics.Entity import Entity
import pygame

class Entity_presenter:
    def __init__(self, entity:Entity, image):
        self.entity = entity
        self.size, _ = image.get_size() if image!=None else 25, 50
        self.image = image

    def draw(self, screen):
        if self.entity.facing_right:
            rotated_image = pygame.transform.flip(self.image, True, False)
            screen.blit(rotated_image, self.entity.get_position().to_coords(*self.size))
        else:
            screen.blit(self.image,  self.entity.get_position().to_coords(*self.size))

    def _get_entity(self):
        return self.entity
    
